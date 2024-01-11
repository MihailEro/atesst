from django.contrib import admin
from django.utils.html import format_html

from suppliers.models import Participant, Contacts, Product


@admin.register(Participant)
class SupplierAdmin(admin.ModelAdmin):

    readonly_fields = ('get_supplier_link',)
    list_filter = ('contacts__city',)
    actions = ['clear_debt_to_supplier']

    def get_supplier_link(self, obj):

        if obj.supplier:
            return format_html('<a href="/admin/suppliers/participant/{}/">{}</a>', obj.supplier.id, obj.supplier)
        return '-'

    get_supplier_link.short_description = 'Ссылка на поставщика'

    def clear_debt_to_supplier(self, request, queryset):

        queryset.update(debt=0)

    clear_debt_to_supplier.short_description = 'Очистить задолженность'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_model', 'release_date')


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number', 'supplier')
