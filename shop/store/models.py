from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
import datetime, time
import locale


class Product(models.Model):
    header = models.CharField('Название товара', max_length = 225, null=False, blank=False)
    description = models.TextField('Описание товара')
    image = models.ImageField('Фото товара', upload_to='images/', null=True, blank=True)
    price = models.PositiveIntegerField('Цена товара')
    vendor_code = models.CharField('Артикул', max_length = 100, default='CX'+str(time.time())+'H01' )
    create_date = models.DateTimeField('Дата публикации', default=timezone.now)
    
    def floatfract(self, length=2):
        sf = "%.{length}f".format(length=length) % self
        return sf.split('.')[1] # self.price|floatfract:5
    
    def price_format(self):
        return mark_safe(u'<strong>{0:,} &#8381;</strong>'.format(self.price).replace(",", ", "))
    price_format.short_description = 'Цена товара'
    price_format.allow_tags = True
    
    def header_link(self):
        return mark_safe(u'<a href="/admin/store/product/{0}/change/">{1}</a>'.format(self.id, self.header))
    header_link.short_description = 'Наименование товара'
    header_link.allow_tags = True    
    
    def settings(self):
        message = 'Удалить этот товар безвозвратно ?'
        return mark_safe(u'<a href="/admin/store/product/{0}/delete/" onclick="return confirm( {2} {1} );" style="color:red;">&#10006;</a> <a href="/admin/store/product/{0}/change/">&#9998;</a>'.format(self.id, message, self.header))
    settings.short_description = 'Управление'
    settings.allow_tags = True
            
    def image_img(self):
        if self.image:
            return mark_safe(u'<img src="/{0}" style="width:50px;height:70px;"/>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
    
        
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    

class Basket(models.Model):
    customer = models.OneToOneField(get_user_model(), primary_key=True, null=False, blank=False, on_delete=models.CASCADE)
    chekout = models.ForeignKey(Product, on_delete = models.CASCADE)
    pub_date = models.DateTimeField('Дата добавления')
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары в корзине'