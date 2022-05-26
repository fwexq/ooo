from django.contrib import admin
from main.models.post.models import Post
from main.models.user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'password', 'avatar', 'api_key', 'created_at', 'updated_at')

admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'status', 'published', 'photo')

admin.site.register(Post, PostAdmin)

