from django.db import models

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    about_me = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='cover_pics/', blank=True, null=True)

    def __str__(self):
        return self.name