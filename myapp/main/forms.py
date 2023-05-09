from django import forms  

class ContactForm(forms.Form):
    # name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(label='Subject',max_length=100)
    # subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea,max_length=2500)

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not email.endswith('@example.com'):
    #         raise forms.ValidationError('Invalid email address')
    #     return email
