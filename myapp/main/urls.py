from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffee/', views.coffee, name='coffee'),
    path('shoproaster/', views.shoproaster, name='shoproaster'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('spare-parts/',views.spareparts, name='spareparts'),
    # path('test/',views.test, name='test'),
    # path('service/', views.service, name='service'),
    # path('reservation/', views.reservation, name='reservation'),
    # path('testimonial/', views.testimonial, name='testimonial'),
    # path('gallery/', views.gallery, name='gallery'),

]