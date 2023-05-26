from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ["hostname", "management_ip", "slots",]
    search_fields = ["hostname",]

@admin.register(TapePool)
class TapePoolAdmin(admin.ModelAdmin):
    list_display = ["name", "library"]
    autocomplete_fields = ["library",]
    search_fields = ["name",]

@admin.register(Tape)
class TapeAdmin(admin.ModelAdmin):
    list_display = ["barcode", "pool", "data_expiration", "full",]
    autocomplete_fields = ["pool",]
    search_fields = ["barcode",]
