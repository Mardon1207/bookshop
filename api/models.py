from django.db import models
from django.core.validators import MinValueValidator


class Customer(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    username=models.CharField(max_length=64,unique=True)
    password=models.CharField(max_length=512)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self) -> str:
        return self.full_name
    

class Contact(models.Model):
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE)
    email=models.CharField(max_length=64)
    address=models.CharField(max_length=512)
    phone=models.CharField(max_length=13)

    def __str__(self) -> str:
        return f"{self.customer.full_name} - {self.phone}"


class Publisher(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    lang = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.lang


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    bio = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(limit_value=0.00)])
    quantity = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
    isbn = models.IntegerField()
    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    pages = models.IntegerField(validators=[MinValueValidator(limit_value=0)])
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    pubished_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title