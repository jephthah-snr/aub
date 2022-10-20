from django.contrib import admin
from . models import timetable, blog,event

# Register your models here.
admin.site.register(timetable)
admin.site.register(blog)
admin.site.register(event)