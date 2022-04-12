from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from famplan.accounts.models import UserProfile

'''
Signals are used for:
1. Creating profile model for User
2. Send email after user register
    - Welcome email
    - Verification email
'''

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
        )
        profile.save()
