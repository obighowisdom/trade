from django.contrib import admin

# Register your models here.
from .models import wallet, contact_request, withdraw_request, crypto_address





admin.site.register(wallet)
admin.site.register(contact_request)
admin.site.register(withdraw_request)
admin.site.register(crypto_address)