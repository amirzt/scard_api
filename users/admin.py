from django.contrib import admin

from users.models import CustomUser, Shop, Offer, HomeMessage, Support


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'expire_date', 'date_joint')
    search_fields = ('phone__startswith',)
    fields = ('phone', 'is_visible', 'is_active', 'is_staff', 'app_type', 'version', 'expire_date')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name__startswith',)
    fields = ('name', 'description', 'banner', 'phone', 'address', 'location', 'is_active', 'score')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'shop')
    search_fields = ('title__startswith',)
    fields = ('shop', 'title', 'description', 'discount', 'is_active')


@admin.register(HomeMessage)
class HomeMessageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title', 'content',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('phone',)
    # search_fields = ('title__startswith',)
    fields = ('phone', 'email', 'telegram')
