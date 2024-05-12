from django.db import models

# Create your models here.
class movieapp(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)
    year=models.IntegerField()
    image=models.ImageField(upload_to='movieapp/image',null=True,blank=True)

    def __str__(self):
        return self.title