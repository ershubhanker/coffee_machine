from django.db import models
import datetime
from django_countries.fields import CountryField

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from PIL import Image as PILImage
from django import forms  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

# ----------User model
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        error_messages={'exists': 'This email is already registered.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
# ------------login model
class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


# --------------contact model
class Contact(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.email}'
    

# ---------------navitems
class navItems(models.Model):
    items = models.CharField(max_length=50)
    def __str__(self):
        return self.items
    
    
# -----------------paragraph
class paragraph(models.Model):
    para = models.TextField()
    def __str__(self):
        return f'{self.para}'


# --------------------button text
class buttonText(models.Model):
    btn_txt = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.btn_txt}'


# ----------------headings
class Headings(models.Model):
    head_text = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.head_text}'

# ---------------------video------------
class videoFiles(models.Model):
    video = models.FileField(upload_to='media')
    video_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.video_name

    
# -----------------images upload and compressed---------------------
class Image(models.Model):
    image = models.ImageField(upload_to='media')
    sequence = models.AutoField(primary_key=True)

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.image:
            # Open the image using Pillow
            img = PILImage.open(self.image)
            # Compress the image
            compressed_image = self.compress_image(img)
            # Generate a unique name for the compressed image file
            compressed_image_name = f"compressed_{self.image.name}"
            # Create an in-memory stream for the compressed image
            compressed_image_stream = BytesIO()
            # Save the compressed image to the in-memory stream based on its format
            compressed_image_format = self.get_image_format()
            compressed_image.save(compressed_image_stream, format=compressed_image_format)
            # Create an InMemoryUploadedFile for the compressed image
            compressed_image_file = InMemoryUploadedFile(
                compressed_image_stream,
                None,
                compressed_image_name,
                'image/' + compressed_image_format.lower(),
                sys.getsizeof(compressed_image_stream),
                None
            )
            # Update the image field with the compressed image
            self.image = compressed_image_file
        super().save(*args, **kwargs)
    def get_image_format(self):
        # Get the image format based on the file extension
        format_mapping = {
            'JPEG': 'JPEG',
            'JPG': 'JPEG',
            'PNG': 'PNG',
            'GIF': 'GIF',
            # Add more image formats and their corresponding Pillow format names if needed
        }
        file_extension = self.image.name.split('.')[-1].upper()
        return format_mapping.get(file_extension, 'JPEG')  # Default to JPEG format if not found

    @staticmethod
    def compress_image(image):
        # Define the desired maximum size for the compressed image
        max_size = (800, 800)  # Adjust according to your needs
        # Resize the image while maintaining the aspect ratio
        image.thumbnail(max_size, PILImage.ANTIALIAS)
        # Return the compressed image
        return image
    



# -----------------sparepart model
class spareParts(models.Model):
    toolCategory = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=30)
    toolDesc = models.TextField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - ${self.price} / {self.toolCategory}'



class galleryImages(models.Model):
    galleryImage = models.ImageField(upload_to='media')



# --------------------Order model
class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)
    address = models.CharField(max_length=300,null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

    image = models.ImageField(upload_to='media/',null=True, blank=True)
    product = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    date = models.DateField(default=datetime.datetime.today, null=True, blank=True)


    def __str__(self):
        return f'{self.product} - {self.user}'
    


# -----------------------------instaquote model
class Instantquote(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dnf = (('Yes','Yes'),('No','No'))
    do_you_need_financing = models.CharField(max_length=100, choices=dnf)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    rti = (('Yes','Yes'),('No','No'))
    roaster_trade_in = models.CharField(max_length=100, choices=rti)
    srs1 = (('Genesis-Xr3','Genesis-Xr3'),('Ranger-Xr5','Ranger-Xr5'),('Raven-Xr15','Raven-Xr15'),('Sentinel-Xr20','Sentinel-Xr20'),('Warden-Xr30','Warden-Xr30'),)
    select_roaster_size1 = models.CharField(max_length=100, choices=srs1)
    volt = (('110 V','110 V'),('220 V','220 V'))
    voltage = models.CharField(max_length=100, choices=volt)
    srt = (('Barley Roaster','Barley Roaster'),('Cacao Roaster','Cacao Roaster'),('Chili Roaster','Chili Roaster'),('Coffee Roaster','Coffee Roaster'),('Grape Seed Roaster','Grape Seed Roaster'),('Hemp Roaster','Hemp Roaster'),('Millet Roaster','Millet Roaster'),('Noodle Roaster','Noodle Roaster'),('Nut Roaster','Nut Roaster'),('Sesame Seed Roaster','Sesame Seed Roaster'),('Woodchip Roaster','Woodchip Roaster'))
    select_roaster_type = models.CharField(max_length=100, choices=srt)
    col = (('Gloss Black','Gloss Black'),('Gloss White','Gloss White'),('Matte Black','Matte Black'),('Matte White','Matte White'),('Design Package ($2450.00 USD*)','Design Package ($2450.00 USD*)'),)
    color = models.CharField(max_length=100,choices=col)
    gas = (('Natural Gas','Natural Gas'),('Propane ($300.00 USD*)','Propane ($300.00 USD*)'))
    gas_type = models.CharField(max_length=100,choices=gas)
    fr = (('Yes','Yes'),('No','No'))
    first_responder = models.CharField(max_length=100,choices=fr)
    


