from django.contrib import admin
from .models import School, Curriculum, Stream, Test, Level

# Register your models here.
admin.site.register(School)
admin.site.register(Curriculum)
admin.site.register(Level)
admin.site.register(Stream)
admin.site.register(Test)