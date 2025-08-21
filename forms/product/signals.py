from .models import Products, ProductLog
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender = Products)
def log_product_creation(sender, instance, created, **kwargs):
    if created:
        ProductLog.objects.create(
            product = instance,
            message = f'product {instance.product_name} was created '
        )


@receiver(post_save, sender = Products)
def log_product_update(sender, instance, created, **kwargs):
    if not created:
        ProductLog.objects.create(
            product = instance,
            message = f'product {instance.product_name} was updated '
        )