from django.contrib import admin
from .models import Bodega, Vino, Reseña, Page, Profile

admin.site.register(Bodega)
admin.site.register(Vino)
admin.site.register(Reseña)
admin.site.register(Page)
admin.site.register(Profile)

# Register your models here.
