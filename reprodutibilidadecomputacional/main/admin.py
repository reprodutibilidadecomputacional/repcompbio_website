from django.contrib import admin

from .models import People

class NewsAdmin(admin.ModelAdmin):
    fields = ["news_title",
              "published_date",
              "news_text"]

# Register your models here.
admin.site.register(People)