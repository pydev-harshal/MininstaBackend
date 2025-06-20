from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from users_app.models import User, Profile

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )


@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()
    if instance.email:
        instance.email = instance.email.lower()