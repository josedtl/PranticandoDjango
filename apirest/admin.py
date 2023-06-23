from django.contrib import admin
from .models import Task
from .models import Catalogo_Persona
from .models import Catalogo_TipoDocumento
# Register your models here.
admin.site.register(Task)
admin.site.register(Catalogo_Persona)
admin.site.register(Catalogo_TipoDocumento)