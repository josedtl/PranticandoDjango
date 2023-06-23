from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from apirest import views
from .views import GetPersonasView
from .views import GetPersonaSoloNombreView
from .views import GetPersonaSoloNombreView
from .views import GuardadoView,GuardadoCabeceraView

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")
router.register(r"TipoDocumentos", views.TipoDocumentoView, "TipoDocumentos")
# router.register(r"Guardado", views.GuardadoView, "Guardado")

urlpatterns = [
    path("api/", include(router.urls)),
    # path("api/TipoDocumento/", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API")),
    path("api/Persona/GetPersona", GetPersonasView.as_view(), name="get_personas"),
    path(
        "api/Persona/GetPersonaSoloNombre",
        GetPersonaSoloNombreView.as_view(),
        name="get_personasSoloNombre",
    ),
    path("api/Persona/Guardar", GuardadoView.as_view(), name="Post_Guardado"),
        path("api/Persona/GuardarCabecera", GuardadoCabeceraView.as_view(), name="Post_GuardadoCabecera"),
]
