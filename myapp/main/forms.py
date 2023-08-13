from django import forms  
from phonenumber_field.formfields import PhoneNumberField
from .models import Order,Contact,Instantquote



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','pincode','address','phone','country']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone','email','subject','message']

class InstaquoteForm(forms.ModelForm):
    class Meta:
        model = Instantquote
        fields = '__all__'
    