from django.db import models

class Comment(models.Model):
    text = models.CharField(max_length=255, verbose_name=u'Текст',)
    user_name = models.CharField(max_length=255, verbose_name=u'ФИО',)
    rating = models.IntegerField(verbose_name=u'Рэйтинг',)
    img = models.ImageField(upload_to='img/',blank=True)
    avalible = models.BooleanField(default=False, verbose_name=u'Показать на сайте',)

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name=u'Отзыв'
        verbose_name_plural=u'Отзывы'

