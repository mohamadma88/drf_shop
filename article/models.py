from django.db import models
from product.models import Category
from account.models import User
from django_jalali.db import models as jmodels


class Article(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده',blank=True,null=True)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی ها')
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='عنوان مقاله')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    img = models.ImageField(verbose_name='عکس مقاله')
    text = models.TextField(null=True, blank=True, verbose_name='متن مقاله')
    slug = models.SlugField(blank=True, null=True)
    publish = models.BooleanField(default=True, verbose_name='منتشر بشود؟')

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'مقالات'
        verbose_name = 'مقاله'

    def __str__(self):
        return self.title
