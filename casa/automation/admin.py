from django.contrib import admin

from .models import Banner, SubNav, SubNavContent

# Register your models here.


@admin.register(SubNav)
class SubNavAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'icon', 'is_active']
    list_display_links = 'title', 'url', 'icon', 'is_active'
    search_fields = 'title', 'url', 'icon', 'is_active'
    list_filter = 'title', 'url', 'icon', 'is_active'


@admin.register(SubNavContent)
class SubNavContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content',
                    'subcontent', 'function_button', 'is_active']
    list_display_links = 'title', 'content', 'subcontent', 'function_button', 'is_active'
    search_fields = 'title', 'content', 'subcontent', 'function_button', 'is_active'
    list_filter = 'title', 'content', 'subcontent', 'function_button', 'is_active'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle',
                    'title_highlight', 'title_finish', 'is_active']
    list_display_links = 'title', 'subtitle', 'title_highlight', 'title_finish', 'is_active'
    search_fields = 'title', 'subtitle', 'title_highlight', 'title_finish', 'is_active'
    list_filter = 'title', 'subtitle', 'title_highlight', 'title_finish', 'is_active'
