from datetime import time

from django.db import models

CHOICES_RESTAURANT_TYPE = (
    ('kor', 'Korean'),
    ('chn', 'Chinese'),
    ('jpn', 'Japanese'),
    ('mex', 'Mexican'),
    ('amc', 'American'),
    ('tha', 'Thai'),
    ('med', 'Mediterranean'),
    ('ita', 'Italian'),
    ('vtn', 'Vietnamese'),
    ('spn', 'Spanish'),
    ('ind', 'Indian'),
    ('etc', 'Etc'),
)
CHOICES_PRICE = (
    ('c', 'Cheap'),
    ('n', 'Normal'),
    ('e', 'Expensive'),
    ('v', 'Very Expensive'),
)
CHOICES_TIME = (
    (time(9, 00, 00), '9시'),
    (time(10, 00, 00), '10시'),
    (time(11, 00, 00), '11시'),
    (time(12, 00, 00), '12시'),
    (time(13, 00, 00), '13시'),
    (time(14, 00, 00), '14시'),
    (time(15, 00, 00), '15시'),
    (time(16, 00, 00), '16시'),
    (time(17, 00, 00), '17시'),
    (time(18, 00, 00), '18시'),
    (time(19, 00, 00), '19시'),
    (time(20, 00, 00), '20시'),
    (time(20, 00, 00), '21시'),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=5)
    district = models.CharField(max_length=5)
    detail_address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=11)
    joined_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    restaurant_type = models.CharField(max_length=3, choices=CHOICES_RESTAURANT_TYPE)
    average_price = models.CharField(max_length=1, choices=CHOICES_PRICE)
    thumbnail = models.ImageField()
    owner = models.ForeignKey('members.User')

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    restaurant = models.ForeignKey('Restaurant')

    def __str__(self):
        return f'{self.restaurant.name} - {self.name}'


class ImageForRestaurant(models.Model):
    image = models.ImageField(upload_to='restaurant')
    restaurant = models.ForeignKey(Restaurant)


class ReservationTable(models.Model):
    table_size = models.PositiveSmallIntegerField()
    restaurant = models.ForeignKey('Restaurant', related_name='tables')


class ReservationInfo(models.Model):
    table = models.ForeignKey('ReservationTable', related_name='reservations')
    time = models.CharField(max_length=1, choices=CHOICES_TIME)
    date = models.DateField()
