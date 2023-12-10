from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# natural key
class UserManager(models.Manager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    rooms = models.ManyToManyField('Room', through='Booking')

    objects = UserManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.email


class Room(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    max_guests = models.IntegerField()
    bookings = models.ManyToManyField('User', through='Booking')

    TYPE_CHOICES = (
        ('d', 'Double'),
        ('t', 'Triple'),
        ('q', 'Quad'),
        ('s', 'Suite'),
    )

    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='d', blank=False, null=False)

    def __str__(self):
        return self.type


class Booking(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    extra_bed = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=500, null=False)
    date = models.DateField(null=False)
    
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, blank=False, null=False)

    def __str__(self):
        return self.review
