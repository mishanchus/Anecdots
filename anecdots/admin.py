from django.contrib import admin
from .models import Anecdot, Category, Comments

class AnecdotAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'like', 'dislike', 'category', 'is_published')
    list_filter = ('category','is_published')
    search_fields = ('text',)


admin.site.register(Anecdot, AnecdotAdmin)
admin.site.register(Category)
admin.site.register(Comments)
