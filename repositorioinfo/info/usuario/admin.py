from django.contrib import admin
from usuario.models import Usuario, Producto
# Register your models here.

def modificar_email(ModelAdmin,request,queryset):
	queryset.update(email='email@test.com')


class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'email')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto)

