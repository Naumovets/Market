from celery import shared_task
from django.core.mail import send_mail

from orders.models import Order


@shared_task
def order_created(order_id):
    """
    Задание по отправке на электронную почту,
    после успешного создания заказа
    """

    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер {order.id}'
    message = f'Уважаемый {order.first_name}, \n\n' \
              f'Ваш заказ успешно создан.\n' \
              f'ID вашего заказа - {order.id}'
    mail_sent = send_mail(subject, message, 'admin@market.ru', [order.email])
    return mail_sent
