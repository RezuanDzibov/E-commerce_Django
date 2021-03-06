from django.db.models.signals import post_save
from django.dispatch import receiver

from src.order.tasks import send_delivery_status
from src.order.models import Order


@receiver(post_save, sender=Order)
def send_order_delivery_status(sender, instance, created, **kwargs):
    if not created and instance.delivery_status != "unpaid":
        send_delivery_status.delay(
            subject=f"{instance.customer.first_name} {instance.customer.last_name}",
            order_id=instance.id,
            delivery_status=instance.delivery_status,
            receiver_email=instance.customer.email
        )
