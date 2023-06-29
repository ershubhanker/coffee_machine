from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.core.mail import EmailMessage
from . models import Contact,Image,Headings,navItems,buttonText,paragraph,spareParts,galleryImages
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm
# from twilio.rest import Client



# account_sid = 'AC94ff742162c27fabbf8bf7d7cabac83b'
# auth_token = 'b53922bcc5e8b9f1988cc98df117cc58'
# whatsapp_number = 'whatsapp:+14155238886'

# def send_whatsapp_message(to,email,subject, message):
#     client = Client(account_sid, auth_token)
#     body = f"Email: {email}\nSubject: {subject}\nMessage: {message}"
#     message = client.messages.create(
#         from_=whatsapp_number,
#         body=body,
#         to=to
#     )

# Create your views here.
# from whatsapp_api import WhatsApp












# def base(request):
#     images = Image.objects.all()
#     image3 =  images[3] 
#     return render(request,'base.html',{'images':images,'image3':image3})

'''--------------------------Main Funtions---------------------------'''

def home(request):


    para = paragraph.objects.all()
    
    btnText = buttonText.objects.all()
    

    headings = Headings.objects.all()
    

    

    images = Image.objects.all()
    
    return render(request, 'index.html',{'images': images,
                                         'headings':headings,
                                         'btnText':btnText,
                                         'para':para,})


def about(request):

    

    images = Image.objects.all()
    


    para = paragraph.objects.all()
    
    

    


    btnText = buttonText.objects.all()

    headings = Headings.objects.all()
    

    return render(request,'about.html',{'para':para,
                                        'btnText':btnText,
                                        'headings':headings,
                                        'images':images,})


def coffee(request):
    
    # navcontext = navbar()

    headings = Headings.objects.all()
    
    
    btnText = buttonText.objects.all()

    para = paragraph.objects.all()
    # our existence
   

    
    images = Image.objects.all()
    

    return render(request,'coffee.html',{
                                         'btnText':btnText,
                                         'para':para,
                                         'images':images,
                                         'headings':headings,})


def gallery(request):
    galyimg = galleryImages.objects.all()

    return render(request, 'gallery.html',{'galyimg':galyimg})



def shoproaster(request):

    images = Image.objects.all()
    


    btnText = buttonText.objects.all()
    

    para = paragraph.objects.all()
    
    

    headings = Headings.objects.all()
   
    

    return render(request,'shop.html',{
                                       'images':images,
                                       'btnText':btnText,
                                       'headings':headings,
                                         'para':para,})




def blog(request):


    para = paragraph.objects.all()
    

    
    return render(request,'news.html',{
'para':para                                       })






def contact(request):
    # navcontext = navbar()

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



def spareparts(request):

    headings = Headings.objects.all()
    
    

    # Retrieve the selected category from the query string
    category = request.GET.get('Category')
    
    # Filter the spare parts based on the selected category
    if category:
        spare = spareParts.objects.filter(toolCategory=category)
    else:
        spare = spareParts.objects.all()


    return render(request,'spareparts.html',{'spare': spare,
                                              
                                               'headings': headings})


def checkout(request):

    # Retrieve the selected spare part based on the provided ID
    return render(request, 'checkout.html')


def product_detail(request, product_id):
    product = get_object_or_404(spareParts, id=product_id)
    
    

    context = {
        'product': product,
    }
    return render(request, 'productDetailPage.html', context)




def comparison(request):

    images = Image.objects.all()
    
    return render(request,'roasterComparison.html',{'images':images})


def instantquote(request):
    return render(request, 'instantquote.html')
 

def sentinelxr20(request):

    images = Image.objects.all()

    return render(request, 'sentinelxr20.html',{'images':images})

def wardenxr30(request):

    images = Image.objects.all()

    return render(request, 'warden-xr30.html',{'images':images})

def ravenxr15(request):

    images = Image.objects.all()

    return render(request, 'raven-xr15.html',{'images':images})


def rangerxr5(request):
   

    images = Image.objects.all()

    return render(request, 'ranger-xr5.html',{'images':images})


def genesisxr3(request):

    images = Image.objects.all()

    return render(request, 'genesis-xr3.html',{'images':images})
# def test(request):
#     return render(request, 'cart.html')




# --------------------cart functions---------------------
# from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = spareParts.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


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
    
    return render(request, 'cart.html')