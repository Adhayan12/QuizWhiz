from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name
