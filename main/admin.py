from django.contrib import admin
from .models import Gallery, Goods


class GalleryInline(admin.TabularInline):
    fk_name = 'good'
    model = Gallery


admin.site.register(Gallery)


class GoodsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


admin.site.register(Goods)

