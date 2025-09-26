# Ex02 Django ORM Web Application
## Date: 13/09/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from.models import car_DB,car_DB_Admin
admin.site.register(car_DB,car_DB_Admin)
```

## OUTPUT
<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/eee76c5c-ab65-4cc1-9084-c02e30a87844" />


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
