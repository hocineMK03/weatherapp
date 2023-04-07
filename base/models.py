from django.db import models

# Create your models here.


class countries_all(models.Model):
    name=models.CharField(max_length=20)
    capital=models.CharField(max_length=20)
    region=models.CharField(max_length=20)
    code=models.CharField(max_length=10)

class provinces(models.Model):
    country_name=models.ForeignKey(countries_all,on_delete=models.CASCADE)
    province_name=models.CharField(max_length=20)