from django.contrib import admin
from .models import Anecdot, Category

class AnecdotAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'like', 'dislike', 'category')
    list_filter = ('category',)
    search_fields = ('text',)


admin.site.register(Anecdot, AnecdotAdmin)
admin.site.register(Category)

