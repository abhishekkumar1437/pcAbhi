

from products import views
from django.urls import path

urlpatterns = [
 
    path('',views.home,name='home'),
    path('category/<int:pkid>/',views.show_category,name='show_category'),
    path("pay/", views.order_payment, name="pay"),
    path("payment/", views.payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]
