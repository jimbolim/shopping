from django.shortcuts import render,get_object_or_404
from .models import Goods,Imgs,GoodsType_detail


def goods_list(request,goods_type_pk):
	goodss = Goods.objects.filter(goods_type=goods_type_pk)
	imgs = []
	goods_names = []
	for goods in goodss:
		goods_names.append(goods)
		img_urls = goods.imgs_set.all()#可以使用related_name
		imgs.append(img_urls[0].img)
	context = {}
	context['goodss'] = dict(zip(goods_names,imgs))
	context['goods_detail_type'] = GoodsType_detail.objects.filter(GoodsType_id=goods_type_pk)
	return render(request, 'goods/goods_list.html', context)


def goods_list_detail(request, detail_name_pk):
	goodss = Goods.objects.filter(goods_type_detail_id=detail_name_pk)
	imgs = []
	goods_names = []
	for goods in goodss:
		goods_names.append(goods)
		img_urls = goods.imgs_set.all()#可以使用related_name
		imgs.append(img_urls[0].img)
	context = {}
	context['detail_goodss'] = dict(zip(goods_names,imgs))
	return render(request, 'goods/goods_list_detail.html', context)


def goods_detail(request, goods_pk):
	context = {}
	context['imgs'] = Imgs.objects.filter(goods_name_id=goods_pk)
	context['goods'] = get_object_or_404(Goods, id=goods_pk)
	return render(request, 'goods/goods_detail.html', context)



