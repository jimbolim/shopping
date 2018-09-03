from django.shortcuts import render
from goods.models import Goods,GoodsType,GoodsType_detail,Theme_img1,Theme_img2,Theme_img3

def home(request):
    goodss = Goods.objects.all()[:30]
    imgs = []
    goods_names = []
    for goods in goodss:
        goods_names.append(goods)
        img_urls = goods.imgs_set.all()#可以使用related_name
        imgs.append(img_urls[0].img)

    goods_types = GoodsType.objects.all()
    goodstypes = []
    goods_detail_types = []
    for goodstype in goods_types:
        goodstypes.append(goodstype)
        goods_detail_type = goodstype.goodstype_detail_set.all()
        goods_detail_types.append(goods_detail_type)

    context = {}
    context['goodss'] = dict(zip(goods_names,imgs))
    context['goods_detail_type'] = dict(zip(goodstypes,goods_detail_types))
    context['theme_img1'] = Theme_img1.objects.get(id=1)
    context['theme_img2'] = Theme_img2.objects.get(id=1)
    context['theme_img3'] = Theme_img3.objects.get(id=1)
    return render(request, 'home.html', context)
