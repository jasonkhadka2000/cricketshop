from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('balls/',views.balls,name="balls"),
    path('kits/',views.kits,name="kits"),
    path('jerseys/',views.jerseys,name="jerseys"),
    path('bowlingmachines/',views.bowlingmachines,name="bowlingmachines"),
    path('viewproduct/<int:id1>',views.viewproduct,name="viewproduct"),
    path('handlelogin/',views.handlelogin,name="login"),
    path('handlesignup/',views.handlesignup,name="signup"),
    path('handlelogout/',views.handlelogout,name="logout"),  
    path('cart/',views.cart,name="cart"),
    path('updatecart/<int:id2>',views.updatecart,name="updatecart"),
    path('removefromcart/<int:id3>',views.removefromcart,name="removefromcart"),
    path('checkout/',views.checkout,name="checkout"),
    path('confirmorder/',views.confirmorder,name="confirmorder"),
    path('ordertracker/',views.ordertracker,name="ordertracker"),
    path('updateprofileform/',views.updateprofileform,name="updateprofileform"),
    path('updateprofile/',views.updateprofile,name="update"),
    path('updatepasswordform/',views.updatepasswordform,name="updatepasswordform"),
    path('updatepassword/',views.updatepassword,name="updatepassword"),
    path('cancelorder/<int:id>',views.cancelorder,name="cacncelorder"),


]