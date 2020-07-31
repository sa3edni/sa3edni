from django.contrib import admin
from .models import Student, News, University,Major,Subject
# Register your models here.
admin.site.register(News)
admin.site.register(Student)
admin.site.register(University)
admin.site.register(Major)
admin.site.register(Subject)