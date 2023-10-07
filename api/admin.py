from django.contrib import admin

from .models import Post

# Registering the models in the django admin
admin.site.register(Post)
