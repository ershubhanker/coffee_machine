from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffee/', views.coffee, name='coffee'),
    path('gallery/',views.gallery, name='gallery'),
    path('shoproaster/', views.shoproaster, name='shoproaster'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('spare-parts/',views.spareparts, name='spareparts'),
    path('spare-parts/<int:product_id>/', views.product_detail, name='product_detail'),
    path('roaster-comparison/',views.comparison, name='comparison'),
    path('instant-quote/',views.instantquote, name='instantquote'),
    
    path('sentinelxr20/',views.sentinelxr20, name='sentinelxr20'),
    path('wardenxr30/',views.wardenxr30, name='wardenxr30'),
    path('ravenxr15/',views.ravenxr15, name='ravenxr15'),
    path('rangerxr5/',views.rangerxr5, name='rangerxr5'),
    path('genesisxr3/',views.genesisxr3, name='genesisxr3'),


    # path('test/',views.test, name='test'),
    # path('service/', views.service, name='service'),
    # path('reservation/', views.reservation, name='reservation'),
    # path('testimonial/', views.testimonial, name='testimonial'),
    # path('gallery/', views.gallery, name='gallery'),

]