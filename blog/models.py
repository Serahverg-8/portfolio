from django.db import models

# Create your models here.
class Blog(models.Model):
    title= models.CharField("Title",max_length=100)
    pub_date=models.DateTimeField(blank=True)
    details=models.TextField()
    img=models.ImageField(upload_to='images/')

    def summary(self):

       return self.details[:100]+"..."