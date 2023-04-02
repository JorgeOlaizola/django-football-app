from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    foundation_date = models.DateField()
    
    def __str__(self):
        return self.name
