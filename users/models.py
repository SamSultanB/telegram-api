from django.db import models


class Users(models.Model):

    firstName = models.CharField(verbose_name="First Name", max_length=50)
    lastName = models.CharField(verbose_name="Last Name", max_length=50)
    nick = models.CharField(verbose_name="Nick", max_length=50)
    password = models.CharField(verbose_name="Password", max_length=16)
    email = models.EmailField(verbose_name="Email", max_length=50)
    phoneNumber = models.CharField(verbose_name="Phone Number", max_length=50)

    def __str__(self):
        return f'{self.firstName} - {self.lastName}'