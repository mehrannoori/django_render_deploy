from django.db import models

class People(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.firstname