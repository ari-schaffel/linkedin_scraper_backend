from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    url = models.TextField(default='',blank=True)
    location = models.TextField(default='',blank=True)
    about_description = models.TextField(default='',blank=True)
    company_name = models.TextField(default='',blank=True)
    professional_description =models.TextField(default='',blank=True)


    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.name


class Simple(models.Model):

    name = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name