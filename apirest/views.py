from rest_framework import viewsets,generics
from .serializer import TaskSerializer
from .models import Task,Catalogo_TipoDocumento
from .models import Catalogo_Persona
from .serializer import CatalogoPersonaSerializer,GetPersonaSoloNombreSerializer,TipoDocumentoSerializer
# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TipoDocumentoView(viewsets.ModelViewSet):
    serializer_class = TipoDocumentoSerializer
    queryset = Catalogo_TipoDocumento.objects.all()    

class GetPersonasView(generics.ListAPIView):
    queryset = Catalogo_Persona.objects.all()
    serializer_class = CatalogoPersonaSerializer

class GetPersonaSoloNombreView(generics.ListAPIView):
    queryset = Catalogo_Persona.objects.all()
    serializer_class = GetPersonaSoloNombreSerializer

from .serializer import CabeceraSerializer
# from .serializer import AutorConCalificacionesSerializer

class GuardadoCabeceraView(generics.CreateAPIView):
    serializer_class = CabeceraSerializer

from .serializer import CabeceraProfesoresSerializer

class GuardadoView(generics.CreateAPIView):
    serializer_class = CabeceraProfesoresSerializer