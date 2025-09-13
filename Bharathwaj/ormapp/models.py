from django.db import models
from django.contrib import admin
class car_DB(models.Model):
    car_Name=models.CharField(max_length=10)
    reg_no=models.IntegerField(primary_key=True)
    carowner_email=models.EmailField()
    carmanufature_date=models.DateField()
    car_mileage=models.FloatField()
class car_DB_Admin(admin.ModelAdmin):
    list_display=["car_Name","reg_no","carowner_email","carmanufature_date","car_mileage"]