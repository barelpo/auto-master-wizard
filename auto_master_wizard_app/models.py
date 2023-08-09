from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Manufacturer(models.Model):

    manufacturer_name = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'manufacturers'


class Model(models.Model):

    model_name = models.CharField(max_length=128, unique=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.RESTRICT, related_name='models')

    class Meta:
        db_table = 'models'


class SubModel(models.Model):

    sub_model_code = models.CharField(max_length=128, unique=True)
    model = models.ForeignKey('Model', on_delete=models.RESTRICT, related_name='sub_models')

    class Meta:
        db_table = 'sub_models'


class Trim(models.Model):

    trim_code = models.CharField(max_length=128, unique=True)
    sub_model = models.ForeignKey('SubModel', on_delete=models.RESTRICT, related_name='trims')
    users = models.ManyToManyField(User, through='Favourite', related_name='favourite_trims')

    class Meta:
        db_table = 'trims'


class Favourite(models.Model):

    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='favourites')
    trim = models.ForeignKey('Trim', on_delete=models.RESTRICT, related_name='favourites')

    class Meta:
        db_table = 'favourites'


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    img_url = models.CharField(max_length=1024, null=True)

    class Meta:
        db_table = 'profiles'


class Content(models.Model):

    title = models.CharField()
    uploaded_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='contents', null=True)
    trim = models.ForeignKey('Trim', on_delete=models.RESTRICT, related_name='contents')
    content_type = models.CharField()
    source = models.CharField(max_length=256, null=True)
    url = models.CharField()
    projects = models.ManyToManyField('Project', through='ProjectContent', related_name='project_contents')

    class Meta:
        db_table = 'contents'


class Project(models.Model):

    title = models.CharField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='projects')
    contents = models.ManyToManyField('Content', through='ProjectContent', related_name='content_projects')

    class Meta:
        db_table = 'projects'


class ProjectContent(models.Model):

    project = models.ForeignKey('Project', on_delete=models.RESTRICT)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_contents'




