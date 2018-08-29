from django.shortcuts import render
from goods.models import Goods,GoodsType

def home(request):
    context = {}
    context['img'] = Goods.objects.all()[:30]
    context['goods_types'] = GoodsType.objects.all()
    return render(request, 'home.html', context)
