from django.db import models

class GoodsType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Goods(models.Model):
    name = models.CharField(max_length=30)
    img_url = models.ImageField(upload_to='goods')
    goods_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE)
    #级联删除
    content = models.TextField()
    #created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<Goods: %s>" % self.name


