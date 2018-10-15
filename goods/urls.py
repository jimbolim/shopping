from django.urls import path
from .views import goods_detail,goods_list

urlpatterns = [
	path('<int:goods_pk>', goods_detail, name='goods_detail'),
	path('type/<int:goods_type_pk>', goods_list, name='goods_list')
]