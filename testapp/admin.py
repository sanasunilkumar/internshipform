from django.contrib import admin
from testapp.models import Empmodel
# Register your models here.
class Empadmin(admin.ModelAdmin):
    list_display=['name','year','branch','domain','mode']
admin.site.register(Empmodel,Empadmin)