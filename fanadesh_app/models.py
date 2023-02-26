from django.db import models




class Home(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True)


    def __str__(self):
        return f"{self.title} - {self.description}"

class About(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True)


    def __str__(self):
        return f"{self.title} - {self.description}"
        

class Admission(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True)


    def __str__(self):
        return f"{self.title} - {self.description}"
        

class WhyUs(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True)


    def __str__(self):
        return f"{self.title} - {self.description}"
        

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    phone_number = models.FloatField(max_length=15)
    message = models.TextField(max_length=255)


    def __str__(self):
        return f"{self.name} - {self.message}"
        


class SocialLink(models.Model):
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)