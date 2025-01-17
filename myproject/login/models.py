from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    card_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
