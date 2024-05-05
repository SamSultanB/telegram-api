from django.db import models


class Users(models.Model):
    phoneNumber = models.CharField(verbose_name="Phone Number", max_length=50)

    def __str__(self):
        return f'{self.phoneNumber}'
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True, upload_to="img", blank=True)
    about = models.CharField(max_length=500)
    contacts = models.ManyToManyField("Contact", null=True, related_name="contact", blank=True)

    def __str__(self):
        return self.user_name
    


class Contact(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.name