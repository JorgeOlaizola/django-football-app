from datetime import date

from django.utils import timezone
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)

    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age
    
    def __str__(self):
        return f"{self.name} {self.last_name}"