from django.contrib import admin
from .models import Post
#from post.models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ["title", "published_date"]      # Ekranda neler görünsün.
    list_display_links = ["title", "published_date"]
    list_filter = ["published_date"]
    search_fields = ["title", "text"]
    # list_editable = ["title"]



    class Meta:
        model = Post



admin.site.register(Post, PostAdmin)
