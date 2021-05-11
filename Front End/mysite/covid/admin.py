from django.contrib import admin
from .models import UserProfile, UserImage, Doctor

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserImage)
admin.site.register(Doctor)