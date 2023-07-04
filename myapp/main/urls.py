from django.urls import path,include
from . import views


urlpatterns = [
    path('test/', views.test, name='test'),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffee/', views.coffee, name='coffee'),
    path('gallery/',views.gallery, name='gallery'),
    path('shoproaster/', views.shoproaster, name='shoproaster'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('spare-parts/',views.spareparts, name='spareparts'),
    path('spare-parts/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('cart/', views.cart, name='cart'),
    # path('add-to-cart/<int:spare_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:spare_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('roaster-comparison/',views.comparison, name='comparison'),
    path('instant-quote/',views.instantquote, name='instantquote'),
    
    path('sentinelxr20/',views.sentinelxr20, name='sentinelxr20'),
    path('wardenxr30/',views.wardenxr30, name='wardenxr30'),
    path('ravenxr15/',views.ravenxr15, name='ravenxr15'),
    path('rangerxr5/',views.rangerxr5, name='rangerxr5'),
    path('genesisxr3/',views.genesisxr3, name='genesisxr3'),



# ---------------------------------cart urls---------------------------------
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart'),


   
]