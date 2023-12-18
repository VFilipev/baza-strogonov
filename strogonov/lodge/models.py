from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Lodge(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=u'Название',
                            )
    num = models.CharField(max_length=255,
                            verbose_name=u'Номер дома',
                            )
    sub_name = models.CharField(max_length=255,
                            verbose_name=u'Название для части дома',
                                blank=True,
                            )

    description = models.TextField(
                            verbose_name=u'Описание',
                            blank=True,
                            )    
    short_description = models.TextField(
                            verbose_name=u'Короткое описание',
                            blank=True,
                            )
    
    conveniences = models.TextField(
                            verbose_name=u'Удобства',
                            blank=True,
                            )
    
    availability = models.TextField(
                            verbose_name=u'Удобства',
                            blank=True,
                            null=True
                            )
    
    include = models.TextField(
                            verbose_name=u'Включено в проживание',
                            blank=True,
                            )


    maxP = models.IntegerField(
                            verbose_name=u'Вместительность',
                            )
    
    cost_per_unit = models.IntegerField(
                            verbose_name=u'Цена от',
                            blank=True,
                            null=True,
                            )

    img = ThumbnailerImageField(upload_to='img/',
                            verbose_name=u'фото',
                            blank=True,
                            null=True,
                            )
    img_small = models.ImageField(upload_to='img/',
                            verbose_name=u'превью',
                            blank=True,
                            null=True,
                            )

    plan1 = ThumbnailerImageField(upload_to='img/',
                            verbose_name=u'первый этаж',
                            blank=True,
                            null=True,
                            )
    plan2 = ThumbnailerImageField(upload_to='img/',
                            verbose_name=u'второй этаж',
                            blank=True,
                            null=True,
                            )
    uslugi = models.TextField(
                            verbose_name=u'услуги',
                            )
    slug = models.SlugField(verbose_name=u'URL страницы',
                            help_text=u'Например, uslugi',
                            blank=True,
                            unique=False)
    lodge_main = models.ForeignKey('Lodge'
                                   ,verbose_name="Главный дом",
                                   blank=True,
                                   null=True,
                                   on_delete=models.PROTECT)
    avalible = models.BooleanField(default=True,blank=True)
    
    def get_preview(self):
        return self.img['preview'].url
    def __str__(self):
        return self.name
    def min_cost(self):
        return self.price_set.all().order_by('cost')[0].cost

    class Meta:
        verbose_name=u'Дом'
        verbose_name_plural=u'Дома'

class Availability(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название',)
    lodge = models.ForeignKey('Lodge', blank=True,null=True, on_delete = models.DO_NOTHING,
                                related_name='availability_set'
                              )
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name=u'Доступность'
        verbose_name_plural=u'Доступность'

class Photogroup(models.Model):
    name = models.CharField(max_length=255)
    abstract = models.TextField(
                            verbose_name=u'Описание',
                            )
    keywords = models.TextField(
                            verbose_name=u'ключевые слова',
                            )

    preview = models.ForeignKey('Photos', blank=True,null=True, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name=u'Фотогруппа'
        verbose_name_plural=u'Фотогруппы'

class Photos(models.Model):
    name = models.CharField(max_length=255, blank=True)

    lodge = models.ForeignKey(Lodge,blank=True,null=True, on_delete = models.DO_NOTHING,
                              related_name='photo_gallery_set')
    group = models.ForeignKey(Photogroup,blank=True,null=True, on_delete = models.DO_NOTHING)

    img = ThumbnailerImageField(upload_to='img/')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)

    class Meta:
        verbose_name=u'Фото'
        verbose_name_plural=u'Фото'

class Price(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=u'Название',
                            )
    date_init = models.DateField(auto_now_add=True,
                            verbose_name=u'Дата создание',
                            )
    days = models.CharField(max_length=255,
                            verbose_name=u'Дни',
                            )

    lodge = models.ForeignKey(Lodge,
                            verbose_name=u'Дом',
                            on_delete = models.DO_NOTHING,
                            related_name='price_set'
                            )
    cost = models.FloatField(
                            verbose_name=u'Цена',
                            )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name=u'Цена'
        verbose_name_plural=u'Цены'

class Special_price(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=u'Название',
                            )
    date_init = models.DateField(auto_now_add=True,
                            verbose_name=u'дата заказа',
                            )
    date = models.DateField(
                            verbose_name=u'Дата',
                            )
    date_end = models.DateField(
                            verbose_name=u'Дата завершения',
                            blank=True,
                            null=True
                            )
    lodge = models.ForeignKey(Lodge,
                            verbose_name=u'Дом',
                            on_delete = models.DO_NOTHING,
                            related_name='special_price_set'
                            )
    cost = models.FloatField(
                            verbose_name=u'Цена',
                            )
    active = models.BooleanField(default = True,blank=True)
    def __str__(self):
        name = self.date.strftime(' %d, %b %Y')
        if self.date_end:
            name = name + ' - '+self.date_end.strftime(' %d, %b %Y')

        return name

    class Meta:
        verbose_name=u'Особая цена'
        verbose_name_plural=u'особые цены'

class UslugiGroup(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=u'Название',
                            )
    img = ThumbnailerImageField(upload_to='img/',blank=True)

    description = models.TextField(blank=True)    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=u'Группа услуг'
        verbose_name_plural=u'Группы услуг'


class Uslugi(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=u'Название',
                            )
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='img/',blank=True)

    cost = models.FloatField(
                            verbose_name=u'Будни',
                            default = -1,
                            )
    cost_wk = models.FloatField(
                            verbose_name=u'Выходные',
                            default = -1,
                            )

    group = models.ForeignKey(UslugiGroup, blank=True, null=True, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name=u'Продукты'
        verbose_name_plural=u'Продукты'




