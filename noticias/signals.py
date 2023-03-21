from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Autor

@receiver(post_save, sender=User)
def criar_autor(sender, instance, created, **kwargs):
    if created:
        Autor.objects.create(nome=instance.username, user=instance)