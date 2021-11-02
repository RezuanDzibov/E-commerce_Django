from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from . import models

Customer = get_user_model()


@receiver(post_save, sender=Customer)
def init_cart(sender, instance, created, **kwargs):
    """ The signal that initialize cart for registered customer  """
    if created:
        models.Cart.objects.create(customer=instance)


@receiver(pre_delete, sender=Customer)
def delete_cart(sender, instance, **kwargs):
    """ The signal that remove cart for deleted customer  """
    cart = models.Cart.objects.get(customer__email=instance.email)
    cart.delete()
