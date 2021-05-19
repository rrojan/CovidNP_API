from django.contrib import admin
from .models import Daily, Total, DistrictWise

class DataAdmin(admin.ModelAdmin):
    readonly_fields = ('date_updated',)

admin.site.register(Daily, DataAdmin)
admin.site.register(Total, DataAdmin)
admin.site.register(DistrictWise, DataAdmin)