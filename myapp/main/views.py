from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings
from . models import Contact,Image,Headings,navItems,buttonText,paragraph,spareParts,galleryImages
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm
from cart.cart import Cart
import time

from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm



# def base(request):
#     images = Image.objects.all()
#     image3 =  images[3] 
#     return render(request,'base.html',{'images':images,'image3':image3})

'''--------------------------Main Funtions---------------------------'''
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
# from django.contrib.auth.decorators import login_required

# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.add(product=product)
    return redirect("spareparts")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


# @login_required(login_url="/users/login")
def cart_detail(request):
    cart_items = request.session.get('cart', {})
    is_empty = len(cart_items) == 0

    context = {
        'cart_items': cart_items,
        'is_empty': is_empty,
    }

    return render(request, 'cart.html', context)



#--- checkout 
def checkout(request):
    host = request.get_host()

    timestamp = str(int(time.time()))
    invoice_number = f"INVOICE_NO-{timestamp}"
    
    paypal_dict = {
    'business': settings.PAYPAL_RECEIVER_EMAIL,
    'amount': '50',
    'item_name': "Order-Item-No-5",
    'invoice': f"INVOICE_NO-{invoice_number}",
    'currency_code': "USD",
    'notify_url': f'http://{host}{reverse("paypal-ipn")}',
    'return_url': f'http://{host}{reverse("payment-successful")}',
    'cancel_url': f'http://{host}{reverse("payment-failed")}'
    }

    paypal_payment_button =  PayPalPaymentsForm(initial=paypal_dict)

    
    # Retrieve the selected spare part based on the provided ID
    return render(request, 'checkout.html',{'paypal_payment_button':paypal_payment_button})




# ===========================================
# checkout
# def checkout(request):
#     host = request.get_host()

#     timestamp = str(int(time.time()))
#     invoice_number = f"INVOICE_NO-{timestamp}"

#     # Retrieve the cart items and total amount from the cart_detail view
#     cart_items = request.session.get('cart', {})
#     total_amount = request.session.get('total_amount', 0)

#     # Generate the invoice content
#     invoice_content = f"""
#         Invoice Number: {invoice_number}

#         Order Items:
#         --------------
#     """

#     for key, value in cart_items.items():
#         item_name = value['name']
#         item_price = value['price']
#         item_quantity = value['quantity']
#         item_total = item_price * item_quantity

#         invoice_content += f"{item_name} - ${item_price} x {item_quantity} = ${item_total}\n"

#     invoice_content += f"\nTotal Amount: ${total_amount}"

#     # Prepare PayPal payment details
#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': str(total_amount),
#         'item_name': "Order",
#         'invoice': invoice_number,
#         'currency_code': "USD",
#         'notify_url': f'http://{host}{reverse("paypal-ipn")}',
#         'return_url': f'http://{host}{reverse("payment-successful")}',
#         'cancel_url': f'http://{host}{reverse("payment-failed")}'
#     }

#     paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

#     # Pass the invoice content, total amount, and PayPal payment button to the template
#     return render(request, 'checkout.html', {
#         'invoice_number': invoice_number,
#         'invoice_content': invoice_content,
#         'total_amount': total_amount,
#         'paypal_payment_button': paypal_payment_button,
#     })
# ===========================================
#--- product_detail 
def product_detail(request, product_id):
    product = get_object_or_404(spareParts, id=product_id)
    
    context = {
        'product': product,
    }
    return render(request, 'productDetailPage.html', context)



# paypal payment successful page
def payment_completed_view(request):
    return render(request, 'payment_successful.html')

# payment failed
def payment_failed_view(request):
    return render(request, 'payment_failed.html')



# just to test
def test(request):
    return render(request, 'test.html')


