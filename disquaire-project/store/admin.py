from django.contrib import admin
from .models import Album, Artist


admin.site.register(Artist)
admin.site.register(Album)

