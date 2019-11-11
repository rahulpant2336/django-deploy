from django.db import models
import requests

# Create your models here.
class ProjectCategory(models.Model):
    project_category = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_category


class ProjectSubCategory(models.Model):
    project_sub_category = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_sub_category


class HomePageProject(models.Model):
    project_name = models.CharField(max_length=200)
    project_category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    project_sub_category = models.ForeignKey(ProjectSubCategory, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='project_image/homepage/%Y/%m/%d/', null=True, blank=True)
    project_demo_link = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name


class Supervised(models.Model):
    project_name = models.CharField(max_length=200)
    project_sub_category = models.ForeignKey(ProjectSubCategory, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='project_image/innerpage/%Y/%m/%d/', null=True, blank=True)
    project_demo_link = models.URLField(max_length=250)
    project_short_descr = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name


class Unsupervised(models.Model):
    project_name = models.CharField(max_length=200)
    project_sub_category = models.ForeignKey(ProjectSubCategory, on_delete=models.CASCADE)
    project_image = models.ImageField(upload_to='project_image/innerpage/%Y/%m/%d/', null=True, blank=True)
    project_demo_link = models.URLField(max_length=250)
    project_short_descr = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name
