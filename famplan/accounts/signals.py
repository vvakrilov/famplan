from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import UserProfile

'''
Signals are used for:
1. Creating profile model for User
2. Send email after user register
    - Welcome email
    - Verification email
'''


@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
