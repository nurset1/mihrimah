from django.db import models


# Create your models here.


class Message(models.Model):
    name_message = models.CharField(max_length=50,verbose_name="İsim")
    email_message = models.CharField(max_length=100,verbose_name="Eposta")
    phone_message = models.CharField(max_length=10,verbose_name="Telefon")
    content_message = models.CharField(max_length=200,verbose_name="İçerik")
    date_message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_message
    
    