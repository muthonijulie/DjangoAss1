from django.contrib import admin
from .models import Post

class PostModel(admin.ModelAdmin):
    list_display=['title','content','author']
    search_fields=['author','title']
    
# Register your models here.
admin.site.register(Post,PostModel)