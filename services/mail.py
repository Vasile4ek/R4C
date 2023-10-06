from django.dispatch import receiver
from django.db.models.signals import post_save
from robots.models import Robot
from orders.models import Order
from customers.models import Customer

from django.core.mail import send_mail



@receiver(post_save, sender=Robot)
def send_mail_to_customer(sender, instance, created, **kwargs):
    orders = Order.objects.filter(serial=instance.serial)
    message = f"""Добрый день!
Недавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}. 
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"""
    for order in orders:
        send_mail(order.customer.email, instance.model, instance.version)
        send_mail(
            "Добрый день!",
            message,
            "from@example.com",
            [order.customer.email],
            fail_silently=False,
        )

