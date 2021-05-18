from django.contrib import admin
from .models import Last24Hours, Total

class DataAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated',)

admin.site.register(Last24Hours, DataAdmin)
admin.site.register(Total, DataAdmin)