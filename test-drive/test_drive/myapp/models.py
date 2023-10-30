from django.db import models

class Task(models.Model):
    name = models.CharField('Имя', max_length=100)
    task = models.TextField('Комментарий')
    phone_num = models.TextField('Номер телефона')
    mail = models.TextField('почта')
    name_car = models.TextField('Название машины')

    def __str__(self):
        return self.name