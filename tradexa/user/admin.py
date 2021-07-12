from django.contrib import admin
from.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
        

        list_display = ('id', 'username', 'text','created_at','updated_at')
        list_display_links = ('username', 'id')
        search_fields = ('username', 'text')
        list_filter = ('username',)
        
admin.site.register(Post,PostAdmin)