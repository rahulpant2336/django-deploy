from django.contrib import admin

from .models import ProjectCategory, ProjectSubCategory, HomePageProject, Supervised, Unsupervised

# Register your models here.
admin.site.register(ProjectCategory)
admin.site.register(ProjectSubCategory)
admin.site.register(HomePageProject)
admin.site.register(Supervised)
admin.site.register(Unsupervised)
