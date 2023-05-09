from django.db import models

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

class Image(models.Model):
    image = models.ImageField(upload_to='media')
    sequence = models.AutoField(primary_key=True)

    def __str__(self):
        return self.image.name
    

class spareParts(models.Model):
    toolImage = models.ImageField(upload_to='media')
    toolTitle = models.CharField(max_length=30)
    toolPrice = models.FloatField()

    def __str__(self):
        return f'{self.toolTitle}-{self.toolPrice}'