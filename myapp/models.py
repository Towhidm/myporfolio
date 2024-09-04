from django.db import models

# Create your models here.
# models.py
from django.db import models

class Contact(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.yourname
