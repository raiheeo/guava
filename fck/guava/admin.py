from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

from .views import ProductListViewSet


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1

admin.site.register(UserProfile)
admin.site.register(ProductPhoto)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Rating)



@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductPhotoInline]


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }