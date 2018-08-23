from django.shortcuts import render,get_object_or_404
from .models import Goods,GoodsType


def goods_list(request,goods_type_pk):
	context = {}
	context['goodss'] = Goods.objects.filter(goods_type=goods_type_pk)
	return render(request, 'goods/goods_list.html', context)


def goods_detail(request, goods_pk):
	context = {}
	context['goods'] = get_object_or_404(Goods, id=goods_pk)
	return render(request, 'goods/goods_detail.html', context)



