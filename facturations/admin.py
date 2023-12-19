from django.contrib import admin
from .models import *

class InvoiceProductInline(admin.TabularInline):
    model = InvoiceProduct
    extra = 1
""" 
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'customer', 'total_amount','payed')
    list_filter = ('customer',)
    search_fields = ('number', 'customer__name')
    inlines = [InvoiceProductInline]
    def total_amount(self,obj):
        return f"{obj.calculate_total_amount()} $" """
    


@admin.register(AgentFileVault)
class AgentFileVaultAdmin(admin.ModelAdmin):
    list_display = ('user_name',)
@admin.register(File)
class FileVaultAdmin(admin.ModelAdmin):
    list_display = ('name',)
""" @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email') """

#admin.site.register(InvoiceProduct)
#admin.site.register(Corporate)
#admin.site.register(Agent)
