from django.contrib import admin
from .models import JumiaItem, PriceLog
# Register your models here.


class PriceLogInline(admin.StackedInline):
    readonly_fields = ('date', )
    model = PriceLog
    extra = 1

class JumiaItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'latest_price' ,'brand', 'sku',)
    inlines = (PriceLogInline,)
    search_fields = ('name', )
    # list_filter = ('latest_price',)

    def get_ordering(self, request):
        return ['latest_price']


admin.site.register(JumiaItem, JumiaItemAdmin)

admin.site.site_title = "Best Prices 🔥🔥"
admin.site.site_header = "Best Prices 🔥🔥"
