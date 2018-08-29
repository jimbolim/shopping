from django.db import models

class GoodsType(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name

class Goods(models.Model):
    name = models.CharField(max_length=30)
    img_url = models.ImageField(upload_to='goods')
    #img_url1 = models.ImageField(upload_to='goods', null=True, blank=True)
    #img_url2 = models.ImageField(upload_to='goods', null=True, blank=True)
    goods_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE)
    #级联删除
    #created_time = models.DateTimeField(auto_now_add=True)
    style_number = models.CharField(max_length=50,null=True, blank=True)
    item_name = models.CharField(max_length=50,null=True, blank=True)
    Fabric_content = models.CharField(max_length=50,null=True, blank=True)
    size = models.CharField(max_length=50,null=True, blank=True)
    weight = models.CharField(max_length=50,null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return "<Goods: %s>" % self.name


'''
    def img1(self):
        if self.img_url1 and hasattr(self.img_url1, 'url'):
            return self.img_url1.url

    def img2(self):
        if self.img_url2 and hasattr(self.img_url2, 'url'):
            return self.img_url2.url
'''

