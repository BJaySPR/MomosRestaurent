from django.contrib import admin
from .models import Get_in_touch
# Register your models here.
@admin.register(Get_in_touch)
class Get_in_touchAdmin(admin.ModelAdmin):
    list_display =['id','name','email','phone_no','message']