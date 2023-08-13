from django.contrib import admin
from . models import Contact,navItems,Image,Headings,buttonText,Instantquote,paragraph,spareParts,galleryImages,Order,videoFiles
# Register your models here.

admin.site.register(spareParts)
admin.site.register(Contact)
admin.site.register(navItems)
admin.site.register(paragraph)
admin.site.register(buttonText)
admin.site.register(Headings)
admin.site.register(Image)
admin.site.register(galleryImages)
admin.site.register(Order)
admin.site.register(Instantquote)
admin.site.register(videoFiles)