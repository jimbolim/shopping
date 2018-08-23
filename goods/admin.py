from django.contrib import admin
from .models import GoodsType,Goods
# Register your models here.

@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'goods_type', 'img_url')
