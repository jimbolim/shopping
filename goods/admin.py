from django.contrib import admin
from .models import GoodsType,Goods,Imgs,GoodsType_detail,Theme_img1,Theme_img2,Theme_img3
# Register your models here.

@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(GoodsType_detail)
class GoodsType_detailAdmin(admin.ModelAdmin):
    list_display = ('id', 'detail_name')

class ImgsInline(admin.TabularInline):
    model = Imgs

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    inlines = [ImgsInline]
    list_display = ('id', 'name', 'goods_type', 'goods_type_detail', 'style_number', 'item_name', 'Fabric_content', 'size', 'weight', 'other_details', 'retail_price', 'trade_price')


@admin.register(Imgs)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')

@admin.register(Theme_img1)
class Theme_img1Admin(admin.ModelAdmin):
    list_display = ('id', 'theme_img')

@admin.register(Theme_img2)
class Theme_img2Admin(admin.ModelAdmin):
    list_display = ('id', 'theme_img')

@admin.register(Theme_img3)
class Theme_img3Admin(admin.ModelAdmin):
    list_display = ('id', 'theme_img')
