from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

from .models import Goods,Imgs,GoodsType_detail,GoodsType

EACH_PAGE_GOODS_NUMBER = 21


def get_goods_list(request, goodss):
    paginator = Paginator(goodss, EACH_PAGE_GOODS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_goods = paginator.get_page(page_num)
    currentr_page_num = page_of_goods.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    goodss = page_of_goods.object_list
    imgs = []
    goods_names = []
    for goods in goodss:
        goods_names.append(goods)
        img_urls = goods.imgs_set.all()#可以使用related_name
        try:
            imgs.append(img_urls[0].img)
        except:
            imgs.append('')

    goods_types = GoodsType.objects.all()
    goodstypes = []
    goods_detail_types = []
    for goodstype in goods_types:
        goodstypes.append(goodstype)
        goods_detail_type = goodstype.goodstype_detail_set.all()
        goods_detail_types.append(goods_detail_type)

    context = {}
    context['goods_detail_type'] = dict(zip(goodstypes,goods_detail_types))
    context['goodss'] = dict(zip(goods_names,imgs))
    context['page_of_goods'] = page_of_goods
    context['page_range'] = page_range
    #context['goods_detail_type'] = GoodsType_detail.objects.filter(GoodsType_id=goods_type_pk)
    return context

def goods_list(request,goods_type_pk):
    goodss = Goods.objects.filter(goods_type=goods_type_pk)
    goods_type = GoodsType.objects.filter(id=goods_type_pk)
    context = get_goods_list(request,goodss)
    context['goods_type'] = goods_type[0].type_name
    return render(request, 'goods/goods_list.html', context)


def goods_list_detail(request,goods_type_detail_pk):
    goodss = Goods.objects.filter(goods_type_detail=goods_type_detail_pk)
    goods_type = GoodsType_detail.objects.filter(id=goods_type_detail_pk)
    context = get_goods_list(request,goodss)
    context['goods_type'] = goods_type[0].detail_name
    return render(request, 'goods/goods_list.html', context)


def goods_detail(request, goods_pk):
    context = {}
    context['imgs'] = Imgs.objects.filter(goods_name_id=goods_pk)
    context['goods'] = get_object_or_404(Goods, id=goods_pk)
    return render(request, 'goods/goods_detail.html', context)



