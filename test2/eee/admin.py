from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser



admin.site.register(CustomUser)

