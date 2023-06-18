from django.db import models

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from PIL import Image as PILImage

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name}'
    

class navItems(models.Model):
    items = models.CharField(max_length=50)
    def __str__(self):
        return self.items
    
    
class paragraph(models.Model):
    para = models.TextField()
    def __str__(self):
        return f'{self.para}'


class buttonText(models.Model):
    btn_txt = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.btn_txt}'

class Headings(models.Model):
    head_text = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.head_text}'


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
    
# ---------------------------------



class spareParts(models.Model):
    toolCategory = models.CharField(max_length=100,null=True,blank=True)
    toolImage = models.ImageField(upload_to='media')
    toolTitle = models.CharField(max_length=30)
    toolDesc = models.TextField(null=True, blank=True)
    toolPrice = models.FloatField()

    def __str__(self):
        return f'{self.toolTitle} - ${self.toolPrice} / {self.toolCategory}'