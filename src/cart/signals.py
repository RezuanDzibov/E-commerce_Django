from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from src.cart.models import Cart

Customer = get_user_model()


@receiver(post_save, sender=Customer)
def init_cart(sender, instance, created, **kwargs):
    """Initialize cart for registered customer."""
    if created:
        Cart.objects.create(customer=instance)


@receiver(post_delete, sender=Customer)
def delete_cart(sender, instance, **kwargs):
    """Remove cart for deleted customer."""
    cart = Cart.objects.get(customer__email=instance.email)
    cart.delete()
