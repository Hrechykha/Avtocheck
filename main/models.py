from django.db import models
from django.core.validators import MinLengthValidator

class Avto(models.Model):
    manufacturer = models.CharField('Марка автомобиля', max_length=15) # марка автомобиля
    vin = models.CharField('Вин номер автомобиля', max_length=17, validators=[MinLengthValidator(17)], unique=True)
    description = models.TextField('Описание автомобиля', max_length=500, blank=True)
    date = models.DateField('Дата осмотра автомобиля', blank=False, null=False)
    image = models.ImageField('Фотография', upload_to='images', blank=True, default='images/1.png')

    def __str__(self): #вывод на экран объект класса?
        return self.vin
