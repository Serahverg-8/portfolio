from django.db import models

# Create your models here.
class Job(models.Model):
    #url images/  first goes to media folder and then images in media because of specifying media root in the settings
    image=models.ImageField(upload_to='images/')
    #requires pillow so install pillow
    summary=models.CharField(max_length=200)
