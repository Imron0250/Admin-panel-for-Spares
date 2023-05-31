from django.db import models

class Spares(models.Model):
    TYPES = (
        ('b/y','b/y'),
        ('new','new'),   
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    kg = models.CharField(max_length=255)
    status = models.CharField(
        max_length=3,
        choices=TYPES,
        default='new')

class Featured_Products(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

class Helpers_Task(models.Model):
    title = models.CharField(max_length=255)

class Helper(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    year = models.IntegerField()
    paycheck = models.IntegerField()
    task = models.ForeignKey(Helpers_Task, on_delete=models.CASCADE)
    work_time = models.CharField(max_length=255)

class Partner(models.Model):
    company = models.CharField(max_length=255)
    what_spares = models.CharField(max_length=255)

class Info(models.Model):
    tel = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.ImageField()

class Debt(models.Model):
    people_name = models.CharField(max_length=255)
    a_thing_for_collateral = models.CharField(max_length=255)
    debt_price = models.IntegerField()

class Earning_Info(models.Model):
    earnings= models.IntegerField()
    
class Machine(models.Model):
    what_produces = models.CharField(max_length=255)
    price = models.CharField(max_length=255)


class The_deliveryman(models.Model):
    name = models.CharField(max_length=255)
    paychek = models.CharField(max_length=255)
    the_city_he_goes = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)

class cleaning_location(models.Model):
    location_name = models.CharField(max_length=255)

class Cleaner(models.Model):
    name = models.CharField(max_length=255)
    cleaning_location = models.ForeignKey(cleaning_location, on_delete=models.CASCADE)
    paychek = models.IntegerField()
    cleaning_days = models.CharField(max_length=255)




     


