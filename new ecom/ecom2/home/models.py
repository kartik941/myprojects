from django.db import models

class product(models.Model):
    name = models.CharField(max_length= 255)
    price = models.IntegerField()
    img = models.ImageField(null=True,blank=True)


    @property
    def imgurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# Create your models here.
