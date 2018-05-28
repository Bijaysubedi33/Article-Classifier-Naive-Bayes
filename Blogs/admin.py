from django.contrib import admin

# Register your models here.
from Blogs.models import Post
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
admin.site.register(Post,AuthorAdmin)