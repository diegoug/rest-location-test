from django.contrib import admin


from .models import Driver, Service, Workshop

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    pass
