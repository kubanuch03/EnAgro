from django.core.mail import send_mail
from config.celery import app
@app.task(bind=True)
def send_welcome_email(self, email):
    subject = 'Enagro'
    message = (
        'Subject: Добро пожаловать на наш сайт!\n\n'
        'Привет, дорогой читатель!\n\n'
        'Добро пожаловать на наш сайт! Мы рады видеть вас здесь. Надеемся, что вы найдете у нас много интересных книг, которые добавят вдохновения и удовольствия в вашу жизнь.\n\n'
        'Если у вас есть какие-либо вопросы или вам нужна помощь, не стесняйтесь связаться с нами. Мы всегда готовы помочь.\n\n'
        'Спасибо за то, что выбрали нас. Приятного чтения!\n\n'
        'С наилучшими пожеланиями,\n'
        'Команда book.com'
    )

    from_email = 'sadyr.top@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return 'Done'