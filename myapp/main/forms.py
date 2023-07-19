from django import forms  
from phonenumber_field.formfields import PhoneNumberField
from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone', 'country', 'pincode']

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(label='Subject',max_length=100)
    phone = PhoneNumberField(label='Phone')
    message = forms.CharField(widget=forms.Textarea,max_length=2500)

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not email.endswith('@example.com'):
    #         raise forms.ValidationError('Invalid email address')
    #     return email
