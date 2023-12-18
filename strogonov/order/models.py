from django.db import models
from lodge.models import Lodge, Special_price, Price, Uslugi
from datetime import timedelta
import datetime as dt
# from customerApp.models import Customer

class Order(models.Model):

    number = models.CharField(max_length=255,
                                blank=True,
                                verbose_name=u'Номер договора'
                                )

    # customer_FK= models.ForeignKey(Customer,
    #                                blank=True,
    #                                null=True,
    #                                verbose_name=u'Клиент из справочника',
    #                                on_delete = models.DO_NOTHING
    #                                )

    customer = models.CharField(max_length=255,
                                verbose_name=u'ФИО'
                                )
    company  = models.CharField(max_length=255,
                                blank=True,
                                verbose_name=u'название организации'
                                )

    phone = models.CharField(max_length=255,
                             verbose_name=u'Телефон'
                             )

    email = models.EmailField()

    order_date = models.DateTimeField(auto_now_add=True,
                                  verbose_name=u'заказ оформлен'
                                  )

    STATUS_CHOICE = (('WT', u'ожидает'),
                     ('DF', u'подтвержден'),
                     ('PP', u'Внесена предоплата'),
                     ('PM', u'оплачен'),
                     ('CP', u'завершeн'),)

    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICE,
                              verbose_name=u'статус',
                              default='WT')

    addres = models.TextField(blank=True,
                              verbose_name=u'адрес'
                              )
    pasport = models.TextField(blank=True,
                               verbose_name=u'поспорт/реквизиты'
                               )
    dogovor = models.FileField(upload_to='dogovor/',blank=True, null=True)

    TYP_CHOICE = (
        ('NC','Нет договоров'),
        ('HC','Есть договоры'),
        ('WS','Есть договоры(один без подписи)'),
        ('WP','Есть договоры(один без печати)'),
        ('SP','Есть два договора без печати и без подписи'),
    )

    dogovor_status = models.CharField(choices=TYP_CHOICE,max_length=2, verbose_name="Статус договора", null=True, blank=True)

    ul = models.BooleanField(default=False,verbose_name='Юридическое лицо')

    event_status= models.BooleanField(default=False,verbose_name=' Внесено в календарь')

    comment = models.TextField(blank=True)

    facimile = models.BooleanField(default=False,verbose_name='Факсимиле')    
    
    def __str__(self):
        return '%i' %self.id +  '|'+self.customer
    
    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

class Service(models.Model):
    order = models.ForeignKey(Order,
                              verbose_name='Сауна',
                              on_delete = models.CASCADE,
                              null = True,
                              blank = True,
                              related_name='services'
                              )
    TYP_CHOICE = (
        ('SN','Баня'),
        ('CH','Чан'),
    )
    name = models.CharField(choices=TYP_CHOICE,max_length=2, verbose_name="Название", null=True, blank=True)
    start_date = models.DateTimeField(null = True,
                                        blank = True)
    end_date = models.DateTimeField(null = True,
                                    blank = True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Product(models.Model):
    order = models.ForeignKey(Order,
                              verbose_name='Заказ',
                              on_delete = models.CASCADE,
                              null = True,
                              blank = True,
                              related_name='products'
                              )
    product = models.ForeignKey(Uslugi,
                              verbose_name='Продукт',
                              on_delete = models.DO_NOTHING,
                              null = True,
                              blank = True,
                              )

    value = models.FloatField(
                              verbose_name=u'Кол-во',
                              null = True,
                              blank = True,
                              )
    cost = models.FloatField(
        verbose_name=u'цена',
        null = True,
        blank = True,
        )
    comment = models.CharField(max_length=255,
                            verbose_name=u'Комментарий',
                            null=True,
                            blank=True
                            )
    pay = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order_lodge(models.Model):
    order = models.ForeignKey(Order,
                              verbose_name='заказ',
                              on_delete = models.CASCADE,
                              null = True,
                              blank = True,
                              #related_name='lodges'
                              )
    lodge = models.ForeignKey(Lodge,
                              verbose_name='Дом',
                              on_delete = models.DO_NOTHING,
                              )
    start_date = models.DateField()

    end_date = models.DateField()
    cost = models.FloatField(
        verbose_name=u'цена'
        )
    class Meta:
        ordering = ['id']    

class Reserv(models.Model):
    lodge = models.ForeignKey(Lodge, on_delete = models.DO_NOTHING)
    date = models.DateField()
    order = models.ForeignKey(Order, blank=True, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.lodge.name


class Payment(models.Model):
    date = models.DateField(auto_now_add=True,
                            verbose_name=u'дата '
                            )
    order = models.ForeignKey(Order,
                              verbose_name=u'заказ',
                              on_delete = models.DO_NOTHING
                              )
    summ = models.FloatField(
        verbose_name=u'сумма'
        )
