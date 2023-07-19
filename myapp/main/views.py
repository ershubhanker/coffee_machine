from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from . models import Contact,Image,Headings,navItems,buttonText,paragraph,spareParts,galleryImages,Order
from .forms import ContactForm,OrderForm

from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from cart.cart import Cart
import time
from .models import UserCreateForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm



# def base(request):
#     images = Image.objects.all()
#     image3 =  images[3] 
#     return render(request,'base.html',{'images':images,'image3':image3})

'''--------------------------Main Funtions---------------------------'''

# signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            print("--------------It works")
            return redirect('home')
    else:
        form = UserCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("step one")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("approved")
                login(request, user)
                return redirect('home')
            else:
                print("triggered")
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')



#--- home 
def home(request):
    para = paragraph.objects.all()
    btnText = buttonText.objects.all()
    headings = Headings.objects.all()
    images = Image.objects.all()
    return render(request, 'index.html',{'images': images,
                                         'headings':headings,
                                         'btnText':btnText,
                                         'para':para,})


#--- about 
def about(request):
    images = Image.objects.all()
    para = paragraph.objects.all()
    btnText = buttonText.objects.all()
    headings = Headings.objects.all()
    return render(request,'about.html',{'para':para,
                                        'btnText':btnText,
                                        'headings':headings,
                                        'images':images,})


#---  coffee
def coffee(request):
    headings = Headings.objects.all()
    btnText = buttonText.objects.all()
    para = paragraph.objects.all()
    images = Image.objects.all()
    return render(request,'coffee.html',{
                                         'btnText':btnText,
                                         'para':para,
                                         'images':images,
                                         'headings':headings,})


#--- shoproaster 
def gallery(request):
    galyimg = galleryImages.objects.all()
    return render(request, 'gallery.html',{'galyimg':galyimg})


#--- shoproaster 
def shoproaster(request):
    images = Image.objects.all()
    btnText = buttonText.objects.all()
    para = paragraph.objects.all()
    headings = Headings.objects.all()
    return render(request,'shop.html',{'images':images,
                                       'btnText':btnText,
                                       'headings':headings,
                                         'para':para,})


#--- blog
def blog(request):
    para = paragraph.objects.all()
    return render(request,'news.html',{'para':para})


#--- contact
def contact(request):
    images = Image.objects.all()
    headings = Headings.objects.all()
    para = paragraph.objects.all()

    # contact form
    if request.method == 'POST':
        print(request.method)
        form = ContactForm(request.POST)
        if form.is_valid():
            print("entered the if block")
            
            email = form.cleaned_data['email']
            print(email)
            phone = form.cleaned_data['phone']
            print(phone)
            subject = form.cleaned_data['subject']
            print(subject)
            message = f"Email: {email}\n\nPhone: {phone}\n\n{form.cleaned_data['message']}"
            print(message)


            # Send the email
            send_mail(
                subject,
                message,
                email,
                ['boredstuff2021@gmail.com'],
            )
            print("sent successfully----------------")

            return redirect('contact')
    else:
        print('nah---------done')
        form = ContactForm()

    return render(request, 'contact.html',{'form':form,
                                           'headings':headings,
                                           'para':para,'images':images})



#--- spareparts
def spareparts(request):

    headings = Headings.objects.all()
    
    # Retrieve the selected category from the query string
    category = request.GET.get('Category')
    
    # Filter the spare parts based on the selected category
    if category:
        spare = spareParts.objects.filter(toolCategory=category)
    else:
        spare = spareParts.objects.all()

    return render(request,'spareparts.html',{'spare': spare,'headings': headings})


#--- comparison 
def comparison(request):

    images = Image.objects.all()
    
    return render(request,'roasterComparison.html',{'images':images})


#--- instantquote 
def instantquote(request):
    return render(request, 'instantquote.html')
 

#--- sentinelxr20 
def sentinelxr20(request):
    images = Image.objects.all()
    return render(request, 'sentinelxr20.html',{'images':images})


#--- wardenxr30 
def wardenxr30(request):
    images = Image.objects.all()
    return render(request, 'warden-xr30.html',{'images':images})


#--- ravenxr15
def ravenxr15(request):
    images = Image.objects.all()
    return render(request, 'raven-xr15.html',{'images':images})


#--- rangerxr5 
def rangerxr5(request):
    images = Image.objects.all()
    return render(request, 'ranger-xr5.html',{'images':images})


#--- genesisxr3
def genesisxr3(request):
    images = Image.objects.all()
    return render(request, 'genesis-xr3.html',{'images':images})



# --------------------cart functions---------------------
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.add(product=product)
    return redirect("spareparts")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    cart_items = request.session.get('cart', {})
    is_empty = len(cart_items) == 0
    form = OrderForm()  # Instantiate OrderForm outside the POST condition

    context = {
        'cart_items': cart_items,
        'is_empty': is_empty,
    }
    print("before if")
    if request.method == "POST":
        print("inside if")
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            address = form.cleaned_data['address']
            print(address)
            phone = form.cleaned_data['phone']
            print(phone)
            country = form.cleaned_data['country']
            print(country)
            pincode = form.cleaned_data['pincode']
            print(pincode)
            cart = request.session.get('cart', {})
            uid = request.session.get('_auth_user_id')
            user = User.objects.get(pk=uid)
            print(name,address,phone,country,pincode,user)

            for i in cart:
                order = Order(
                    user = user,
                    product=cart[i]['name'],
                    price=cart[i]['price'],
                    quantity=cart[i]['quantity'],
                    total=float(cart[i]['price']) * int(cart[i]['quantity']),
                    image=cart[i]['image'],
                    address=address,
                    name=name,
                    phone=phone,
                    country=country,
                    pincode=pincode,
                )
                order.save()
            print("order success-----------------------")
            return redirect('checkout')

        else:
            form = OrderForm()
    
        context['form'] = form
    return render(request, 'cart.html', context)



#--- checkout 
def checkout(request):
    cart_items = request.session.get('cart', {})
    is_empty = len(cart_items) == 0
    total_price = 0
    for item in cart_items.values():
        price = float(item['price'])
        quantity = int(item['quantity'])
        total_price += price * quantity
    context = {
        'cart_items': cart_items,
        'is_empty': is_empty,
        'total_price': total_price,
    }
    
    
    host = request.get_host()
    timestamp = str(int(time.time()))
    invoice_number = f"INVOICE_NO-{timestamp}"

    
    print("------------done level 2")
    paypal_dict = {
    'business': settings.PAYPAL_RECEIVER_EMAIL,
    'amount': str(total_price),
    'item_name': "Order-Item-No-6",
    'invoice': f"INVOICE_NO-{invoice_number}",
    'currency_code': "USD",
    'notify_url': f'http://{host}{reverse("paypal-ipn")}',
    'return_url': f'http://{host}{reverse("payment-successful")}',
    'cancel_url': f'http://{host}{reverse("payment-failed")}'
    }

    paypal_payment_button =  PayPalPaymentsForm(initial=paypal_dict)


    # Retrieve the selected spare part based on the provided ID
    return render(request, 'checkout.html',{'paypal_payment_button':paypal_payment_button,**context})




#--- product_detail 
def product_detail(request, product_id):
    product = get_object_or_404(spareParts, id=product_id)
    
    context = {
        'product': product,
    }
    return render(request, 'productDetailPage.html', context)



# paypal payment successful page
def payment_completed_view(request):
    request.session['cart'] = {}
    return render(request, 'payment_successful.html')

# payment failed
def payment_failed_view(request):
    return render(request, 'payment_failed.html')



# just to test
def test(request):
    return render(request, 'test.html')



def csrf_forbidden(request, reason=""):
    return render(request, 'error_404_page.html', {'reason': reason})