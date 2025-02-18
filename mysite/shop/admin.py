from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductAbout)
admin.site.register(News)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created')
    list_filter = ('created',)
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
