from django.contrib import admin
import Lab09_Solved.models as models
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(models.BlogPost, BlogPostAdmin)