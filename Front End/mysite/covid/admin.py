from django.contrib import admin
from .models import UserProfile, UserImage

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserImage)