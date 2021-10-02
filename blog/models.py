from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog (models.Model):

    title = models.CharField( max_length=50)
    body = models.CharField( max_length=500)
    image = models.ImageField( upload_to="blog/images" )
    author = models.ForeignKey( User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title + " | " + str(self.author)