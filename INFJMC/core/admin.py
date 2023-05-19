from django.contrib import admin
from core.models import Carrera
from core.models import Profesores

# Register your models here.

class CarreraAdmin(admin.ModelAdmin):
    pass

admin.site.register(Carrera,CarreraAdmin)

class ProfesoresAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profesores,ProfesoresAdmin)