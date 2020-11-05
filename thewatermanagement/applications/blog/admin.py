from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=(
        'text_post',
        'link_post',
        'date_post',
        'author_post',
    )
admin.site.register(Post,PostAdmin)
