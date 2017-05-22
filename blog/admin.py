from django.contrib import admin
from .models import Post, Category, Tag
from blog.models import file

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

    class Media:  
        js = (  
            '/static/blog/js/kindeditor-4.1.10/kindeditor.js',  
            '/static/blog/js/kindeditor-4.1.10/lang/zh_CN.js',  
            '/static/blog/js/kindeditor-4.1.10/config.js'  
        ) 

class filelist(admin.ModelAdmin):
    list_display = ('filename',)

admin.site.register(file,filelist)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)