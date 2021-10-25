from django.db import models

# Create your models here.
class Avto(models.Model):
    manufacturer = models.CharField('Марка автомобиля', max_length=15) # марка автомобиля
    vin = models.CharField('Вин номер автомобиля', max_length=17)
    description = models.TextField('Описание автомобиля', max_length=500)
    date = models.TextField('Дата осмотра автомобиля')
    #title = models.CharField('Заголовок фотографии', max_length=200)
    image = models.ImageField('Фотография', upload_to='images',
                              blank = True, help_text = 'Прикрепите изображения (необязательно)', default='images/1.png')


    def __str__(self): #вывод на экран объект класса?
        return self.vin
