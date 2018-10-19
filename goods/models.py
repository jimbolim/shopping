from django.db import models

class GoodsType(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name

'''
    def __str__(self):
        return str(self.single)

    def __str__(self):  # __str__ on Python 3
        return (self.id,self.img)
'''
class GoodsType_detail(models.Model):
    detail_name = models.CharField(max_length=50)
    GoodsType = models.ForeignKey(GoodsType,on_delete=models.CASCADE)

    def __str__(self):
        return self.detail_name

class Goods(models.Model):
    name = models.CharField(max_length=30)
    goods_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE)
    goods_type_detail = models.ForeignKey(GoodsType_detail, on_delete=models.CASCADE, null=True, blank=True)
    #级联删除
    #created_time = models.DateTimeField(auto_now_add=True)
    style_number = models.CharField(max_length=50,null=True, blank=True)
    item_name = models.CharField(max_length=50,null=True, blank=True)
    Fabric_content = models.CharField(max_length=50,null=True, blank=True)
    size = models.CharField(max_length=50,null=True, blank=True)
    weight = models.CharField(max_length=50,null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)
    retail_price = models.CharField(max_length=50,null=True, blank=True)
    trade_price = models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return "<Goods: %s>" % self.name
'''
    def __str__(self):  # __unicode__ on Python 2
        return (self.id,self.name,self.imgs)


    def img1(self):
        if self.img_url1 and hasattr(self.img_url1, 'url'):
            return self.img_url1.url

    def img2(self):
        if self.img_url2 and hasattr(self.img_url2, 'url'):
            return self.img_url2.url


'''
class Imgs(models.Model):
    img = models.ImageField(upload_to='goods')
    goods_name = models.ForeignKey(Goods, on_delete=models.CASCADE)


class Theme_img1(models.Model):
    theme_img = models.ImageField(upload_to='theme_img/first_slide')
    goods_type = models.OneToOneField(GoodsType, on_delete=models.DO_NOTHING)

class Theme_img2(models.Model):
    theme_img = models.ImageField(upload_to='theme_img/second_slide')
    goods_type = models.OneToOneField(GoodsType, on_delete=models.DO_NOTHING)

class Theme_img3(models.Model):
    theme_img = models.ImageField(upload_to='theme_img/third_slide')
    goods_type = models.OneToOneField(GoodsType, on_delete=models.DO_NOTHING)

