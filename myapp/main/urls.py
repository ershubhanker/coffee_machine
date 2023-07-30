from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('test/', views.test, name='test'),
    path('csrf-forbidden/', TemplateView.as_view(template_name='error_404_page.html'), name='csrf_forbidden'),
    path('csrf-forbidden/', views.csrf_forbidden, name='csrf_forbidden'),

    # signup
    path('signup/',views.signup_view, name='signup'),

    #login
    path('login/',views.login_view, name='login'),

    #logout
    path('logout/',views.logout_view, name='logout'),

    # home
    path('', views.home, name='home'),

    #about
    path('about/', views.about, name='about'),

    #coffee
    path('coffee/', views.coffee, name='coffee'),

    #gallery
    path('gallery/',views.gallery, name='gallery'),

    #shoproaster
    path('shoproaster/', views.shoproaster, name='shoproaster'),

    #blog
    path('blog/', views.blog, name='blog'),

    #contact
    path('contact/', views.contact, name='contact'),

    #spare parts
    path('spare-parts/',views.spareparts, name='spareparts'),

    #product detail page
    path('spare-parts/<int:product_id>/', views.product_detail, name='product_detail'),

    #checkout
    path('checkout', views.checkout, name='checkout'),

    #roaster comparison
    path('roaster-comparison/',views.comparison, name='comparison'),

    #instant quote
    path('instant-quote/',views.instantquote, name='instantquote'),

# ----------------coffee machines-----------------

    # sentinelxr20
    path('sentinelxr20/',views.sentinelxr20, name='sentinelxr20'),

    # wardenxr30
    path('wardenxr30/',views.wardenxr30, name='wardenxr30'),

    #ravenxr15
    path('ravenxr15/',views.ravenxr15, name='ravenxr15'),

    # rangerxr5
    path('rangerxr5/',views.rangerxr5, name='rangerxr5'),

    # genesisxr3
    path('genesisxr3/',views.genesisxr3, name='genesisxr3'),



# ---------------------------------cart urls---------------------------------

    # add item to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),

    # delete the item from cart
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),

    # addition of quantity
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),

    # decreament of quantity
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),

    # delete all
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),

    # total items in cart
    path('cart/cart-detail/',views.cart_detail,name='cart'),


# -----------------paypal payment urls----------------
    # paypal url
    path('paypal/',include('paypal.standard.ipn.urls')),

    # payment successful
    path('payment-completed/',views.payment_completed_view, name='payment-successful'),

    # payment failed
    path('payment-failed/',views.payment_failed_view, name='payment-failed'),

]

