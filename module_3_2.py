def send_email(message, recipient, sender = 'university.help@gmail.com'):
    a = 0
    b = 0
    if recipient.find('.ru') > 0 or recipient.find('.com') > 0 or recipient.find('.net') > 0:
        a = 1
    if sender.find('.ru') > 0  or sender.find('.com') > 0 or sender.find('.net') > 0:
        b = 1
    c = recipient.find('@')
    d = sender.find("@")
    if (c > 0 and d > 0) and a > 0 and b > 0:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
