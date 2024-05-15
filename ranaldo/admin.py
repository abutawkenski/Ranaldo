from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About, Resume, Experience, Skills, Skillss, Awards, Services, Project
# Register your models here.

admin.site.register(About)
admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Skillss)
admin.site.register(Awards)
admin.site.register(Services)
admin.site.register(Project)
