from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_date', 'created_date','is_enable','updated_date']
admin.site.register(Post,PostAdmin)
# Register your models here.
