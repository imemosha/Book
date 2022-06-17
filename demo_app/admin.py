from django.contrib import admin
from demo_app.models import Article, Author, Theme, Comics

# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Theme)
admin.site.register(Comics)
