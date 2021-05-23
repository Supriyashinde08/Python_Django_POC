from django.db import models


# Create your models here.
class Productdetails(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.IntegerField()
    # product_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name
