from django.contrib import auth
from django.contrib.messages.api import success
from django.shortcuts import redirect, render, resolve_url
from .models import Order, Product
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import EditProfileForm
import json
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
cart_pprice=dict()
cart_pname=dict()
cart_pquantity=dict()
count=0

def updatecount():
    global cart_dict
    global count
    count=count+1
    
    
def home(request):
    if request.user.is_authenticated:
        product=Product.objects.filter(pcategory="bat")
        return render(request,'shop/products.html',{"Products":product,"title":"home page"})
    else:
        return redirect('index')

def index(request):
    global cart_pname,cart_pquantity,cart_price
    global count
    count=0
    cart_pname={}
    cart_pquantity={}
    cart_price={}
    totalusers=User.objects.count()
    totalproducts=Product.objects.count()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,"shop/index.html",{"totalusers":totalusers,"totalproducts":totalproducts})

def viewproduct(request,id1):
    product=Product.objects.filter(id=id1)
    placeholder=1
    for obj in product:
        idproduct=obj.id
    if idproduct in cart_pquantity.keys():
        placeholder=cart_pquantity[idproduct]
    return render(request,'shop/viewproduct.html',{"Products":product,"productsquantity":cart_pquantity,"placeholder":placeholder,"title":"viewproduct"})
    

def balls(request):
    product=Product.objects.filter(pcategory="ball")
    return render(request,'shop/products.html',{"Products":product,"title":"Balls"})

def kits(request):
    product=Product.objects.filter(pcategory="kit")
    return render(request,'shop/products.html',{"Products":product,"title":"kits"})

def jerseys(request):
    product=Product.objects.filter(pcategory="jersey")
    return render(request,'shop/products.html',{"Products":product,"title":'Jerseys'})

def bowlingmachines(request):
    product=Product.objects.filter(pcategory="bowlingmachine")
    return render(request,'shop/products.html',{"Products":product,"title":"bowling machines"})

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('username','default')
        password=request.POST.get('password','default')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid credentials")
            return redirect('index')

def handlesignup(request):
    if request.method=="POST":
        username=request.POST.get('username','default')
        fname=request.POST.get('fname','default')
        lname=request.POST.get('lname','default')
        password=request.POST.get('password','default')
        cpassword=request.POST.get('cpassword','default')
        email=request.POST.get('email','default')

        if password==cpassword:
            new_user=User.objects.create_user(username,email,password,first_name=fname,last_name=lname)

            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        
        else:
            messages.error(request,"wrong passwords combination")
            return HttpResponse("error 404")



def handlelogout(request):
    logout(request)
    return redirect('index')


def cart(request):
    # return HttpResponse(cart_pid)
    return render(request,"shop/cart.html",{"productsquantity":cart_pquantity,"productsname":cart_pname,"title":"MyCart"})


def checkout(request):
    global cart_pprice
    global cart_pname
    global cart_pquantity
    total=0
    quantities=[]
    rates=[]
    total1=[]
    a=""
    
    for key,values in cart_pquantity.items():
        quantities.append(values)
    for key,values in cart_pprice.items():
        rates.append(values)
    for num1, num2 in zip(quantities, rates):
        total1.append(int(num1) * int(num2))    
    
    total=sum(total1)
    
    # return HttpResponse("checking out mrjk")
    return render(request,"shop/orderform.html",{"productsquantity":cart_pquantity,"productsname":cart_pname,"productsprice":cart_pprice,"total":total,"title":"Checkout"})
    
def updatecart(request,id2):
    global cart_pprice
    global cart_pname
    global cart_pquantity
    global count
    updatecount()
    quantity=request.POST.get('quantity','1')
    cart_pquantity[id2]=quantity
    p=Product.objects.filter(id=id2)
    for obj in p:
        price=obj.pprice
        name=obj.pname
        cart_pname[id2]=name
        cart_pprice[id2]=price
    messages.success(request,"Item added to cart")
    return redirect('/viewproduct/'+str(id2))

def removefromcart(request,id3):
    global cart_pname,cart_pquantity
    del cart_pname[id3]
    del cart_pquantity[id3]

    return redirect('cart')

        
def confirmorder(request):
    global cart_pname
    global cart_pprice
    global cart_pquantity
    if request.method=="POST":
        result = json.dumps(cart_pquantity)
        order_firstname=request.user.first_name
        order_lastname=request.user.last_name
        order_username=request.user.username
        order_id=request.user.id
        order_contact1=request.POST.get('contact1',"")
        order_contact2=request.POST.get('contact2',"")
        order_email=request.user.email
        order_location=request.POST.get('location',"")
        order_allorders=result
        if order_contact1!="" and order_location!="":
            new_order=Order(order_firstname=order_firstname,order_lastname=order_lastname,order_username=order_username,order_id=order_id,order_contact1=order_contact1,order_contact2=order_contact2,order_email=order_email,order_location=order_location,order_allorders=order_allorders)
            new_order.save()
            cart_pprice={}
            cart_pname={}
            cart_pquantity={}
            messages.success(request,"Your order has been received")
            return redirect('home')
        else:
            return HttpResponse("fill out the form")

def ordertracker(request):
    id=request.user.id
    orders=Order.objects.filter(order_id=id)
    orders_dict_with_key_int={}
    for order in orders:
        allorders_dict=json.loads(order.order_allorders)
        for value in allorders_dict.values():
            product_id=int(value)
            p=Product.objects.get(id=product_id)
            orders_dict_with_key_int[product_id]=p.pname      
        order.order_allorders=orders_dict_with_key_int
        orders_dict_with_key_int={}
        print(order.order_allorders)

    return render(request,"shop/ordertracker.html",{"orders":orders,"title":"MyOrders"})


def updateprofileform(request):
    fm=EditProfileForm(instance=request.user)
    return render(request,"shop/updateprofileform.html",{"form":fm,"title":"Update my profile"})

def cancelorder(request,id):
    order=Order.objects.get(id=id)
    order.delete()
    messages.success(request,"order cancelled")
    return redirect('ordertracker')

def updateprofile(request):
    if request.method=="POST":
        fm=EditProfileForm(request.POST, instance=request.user)
        if fm.is_valid():
            messages.success(request,"Data updated")
            fm.save()
            return redirect('updateprofileform')
        else:
            messages.success(request,"invalid credentials")
            return redirect('updateprofileform')
    else:
        return redirect('updateprofileform')

        
def updatepasswordform(request):
    if request.user.is_authenticated:
        fm=PasswordChangeForm(user=request.user)
        return render(request,"shop/updatepasswordform.html",{"form":fm,"title":"Update password"})
    else:
        messages.success(request,"Need to login again after password change")
        return redirect('logout')

def updatepassword(request):
    print('here')
    if request.method=="POST":
        fm=PasswordChangeForm(request.user,request.POST)
        print(fm)
        if fm.is_valid():
            print("valid")           
            fm.save()
            logout(request)
            return redirect('updatepasswordform')
            
        else:
            print('invalid')
            messages.success(request,"invalid credentials")
            return redirect('updatepasswordform')
    else:
        messages.success("could not updatepassword")
        return redirect('updatepasswordform')
