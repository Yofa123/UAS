from django.db import models


class Menu(models.Model):
    makanan = models.CharField(max_length=100)
    burger = models.CharField(max_length=100)
    minuman = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.makanan}"

class Index(models.Model):
    Menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    about = models.CharField(max_length=100)
    service = models.TextField()
    booking = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    testimonial = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.about}"

