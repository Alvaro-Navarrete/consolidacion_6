from django.contrib import admin
from .models import CustomerUser, Vehiculos, Categorias, Marcas
from django.contrib.auth.admin import UserAdmin


@admin.register(Vehiculos)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('id', 'marca')

@admin.register(Marcas)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')

@admin.register(Categorias)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre')

@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('role',)}), # Agrega campos personalizados 
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('role',)}), # Agrega campos personalizados al formulario de creacion
    )
    
    list_display = ['username', 'email', 'first_name','last_name', 'role', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
