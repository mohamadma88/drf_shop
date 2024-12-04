from django.conf import settings
from django.db import models
from account.models import User


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category',
                               verbose_name='دسته بندی های دیگر')
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='عنوان دسته بندی ')
    image = models.ImageField(null=True, blank=True, verbose_name='عکس دسته بندی')

    class Meta:
        verbose_name_plural = 'دسته بندی'
        verbose_name = 'دسته بندی'

    def __str__(self):
        return self.title


class AmountCaffeine(models.Model):
    title = models.CharField(max_length=100, verbose_name='میزان کافئین')

    class Meta:
        verbose_name_plural = 'میزان کافئین'
        verbose_name = 'میزان کافئین'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='نام محصول')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی ها')
    caffeine = models.ManyToManyField(AmountCaffeine, related_name='caffeine', verbose_name='میزان کافئین ')
    origin = models.CharField(max_length=200, blank=True, null=True, verbose_name='نام محصول')
    ingredient = models.CharField(max_length=200, blank=True, null=True, verbose_name='مواد تشکیل دهنده')
    image1 = models.ImageField(verbose_name='عکس محصول')
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت محصول')
    discount = models.SmallIntegerField(verbose_name='تخفیف ')
    introduction = models.TextField(verbose_name='توضیحات محصول')
    create = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True, verbose_name='موجود')
    amazingoffers = models.BooleanField(default=False, verbose_name='پیشنهاد شگفت انگیز')

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

    def __str__(self):
        return self.title
