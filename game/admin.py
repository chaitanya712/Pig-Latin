from django.contrib import admin

from .models import user_details ,Movie ,Song

admin.site.register(user_details)
admin.site.register(Movie)
admin.site.register(Song)
# Register your models here.
