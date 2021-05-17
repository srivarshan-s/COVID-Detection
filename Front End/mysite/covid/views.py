from django.shortcuts import render, redirect
from .forms import UserForm, ImageForm, DoctorForm
from django.contrib.auth.models import User
from .models import UserProfile, UserImage, Doctor
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .predictFromModel import load_model, make_prediction
from .getDist import getCoords
from .aiRecommend import getNearestPlace, getUserPlace
# from .binaryTree import aiRecommend

# Create your views here.


def home(request):
    return render(request, "covid/home.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("covid:upload")
        else:
            messages.info(request, "Username or Password is incorrect")
            return redirect("covid:login")
    else:
        return render(request, "covid/login.html")


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            location = form.cleaned_data.get("location")
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            UserObject = User.objects.get(username=username)
            coords = getCoords(location)
            xcoord = coords[0]
            ycoord = coords[1]
            UserProfileObject = UserProfile(
                user=UserObject,
                username=UserObject.username,
                location=location,
                xcoord=xcoord,
                ycoord=ycoord,
                fee=0,
            )
            UserProfileObject.save()
            return redirect("covid:upload")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = UserForm()

    return render(request, "covid/signup.html", {"form": form})


@login_required(login_url="covid:login")
def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            if UserImage.objects.filter(name="image"):
                ImageObject = UserImage.objects.get(name="image")
                ImageObject.image = image
            else:
                ImageObject = UserImage.objects.create(
                    name="image",
                    image=image
                )
            ImageObject.save()
            print(ImageObject)
            print("Image Uploaded")
            return redirect("covid:predict")
    else:
        form = ImageForm()
    return render(request, "covid/upload.html", {"form": form})


@login_required(login_url="covid:login")
def predict(request):
    prediction = "TEST"
    load_model()
    ImageObject = UserImage.objects.get(name="image")
    img_path = ImageObject.image.url
    img_path = img_path[1:]
    print(img_path)
    # img_path = 'covid/static/covid/userImage/image.jpg'
    prediction = make_prediction(img_path)
    context = {
        "prediction": prediction,
    }
    return render(request, "covid/predict.html", context)


@login_required(login_url="covid:login")
def recommend(request):
    current_user = request.user.username
    userPlace = UserProfile.objects.get(username=current_user)
    # nearestDoc = aiRecommend(userPlace)
    # print(nearestDoc)
    userPlace = userPlace.__dict__
    getUserPlace(userPlace)
    nearestDoc = getNearestPlace()
    print(nearestDoc)
    context = {
        'nearestDoc': nearestDoc,
    }
    return render(request, "covid/recommend.html", context)


def doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        print(form.errors)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            location = form.cleaned_data.get("location")
            fee = form.cleaned_data.get("fee")
            coords = getCoords(location)
            xcoord = coords[0]
            ycoord = coords[1]
            DoctorObject = Doctor.objects.create(
                name=name,
                location=location,
                xcoord=xcoord,
                ycoord=ycoord,
                fee=fee
            )
            DoctorObject.save()
            print(DoctorObject)
            print("Doctor Database Updated")
            return redirect("covid:home")
    else:
        form = DoctorForm()
    return render(request, "covid/doctor.html", {"form": form})
