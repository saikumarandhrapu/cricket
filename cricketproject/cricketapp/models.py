from django.db import models

# Create your models here.
class Team(models.Model):
    team_name=models.CharField(max_length=50)
    state=models.CharField(max_length=10)
    team_logo=models.ImageField(upload_to='team_logo',blank=True)
