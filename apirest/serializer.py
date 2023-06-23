from rest_framework import serializers
from .models import Task, Catalogo_Persona, Catalogo_TipoDocumento


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id', 'title', 'description', 'done')
        fields = "__all__"


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo_TipoDocumento
        fields = "__all__"


class CatalogoPersonaSerializer(serializers.ModelSerializer):
    NomTipoDumento = serializers.ReadOnlyField(source="tipodocumentoId.nombre")

    class Meta:
        model = Catalogo_Persona
        fields = ["PersonaId", "NomTipoDumento", "nombres", "apellido"]


class GetPersonaSoloNombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo_Persona
        fields = [
            "PersonaId",
            "nombres",
        ]


from .models import Cabecera, Detalle


class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = ["detalleId", "CabeceraId", "Nombre"]


class CabeceraSerializer(serializers.ModelSerializer):
    detalles = DetalleSerializer(many=True)

    class Meta:
        model = Cabecera
        fields = ["CabeceraId", "Nombre", "detalles"]

    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        cabecera = Cabecera.objects.create(**validated_data)
        for detalle_data in detalles_data:
            detalle_data["CabeceraId"]=cabecera.CabeceraId
            Detalle.objects.create(cabeceraId=cabecera, **detalle_data)
        return cabecera


from .models import CabeceraProfesores, DetalleAlumnos


class DetalleAlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleAlumnos
        fields = ["cabecera_id", "Nombre"]


class CabeceraProfesoresSerializer(serializers.ModelSerializer):
    detalles = DetalleAlumnosSerializer(many=True)

    class Meta:
        model = CabeceraProfesores
        fields = ["id", "Nombre", "detalles"]

    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles",[])
        cabecera = CabeceraProfesores.objects.create(**validated_data)
        cabecera.Nombre = "Dta"
        for detalle_data   in detalles_data:
            detalle_data["Nombre"]="DDDDD"
            DetalleAlumnos.objects.create(cabecera=cabecera, **detalle_data)
        return cabecera


# class DetalleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Detalle
#         fields = ['detalleId', 'CabeceraId', 'Nombre']


# class AutorConCalificacionesListadoSerializer(serializers.ModelSerializer):
#     detalles = DetalleSerializer(
#         many=True, source='cabecera_detalle')

#     class Meta:
#         model = Cabecera
#         fields = ['CabeceraId', 'Nombre', 'detalles']


# class AutorConCalificacionesSerializer(AutorConCalificacionesListadoSerializer):
#     detalles = DetalleSerializer(many=True)

#     def create(self, validated_data):
#         val_detalles = validated_data.pop('detalles')

#         # Convertir y guardar el modelo Master (Autor)
#         autor_nuevo = Cabecera(**validated_data)
#         autor_nuevo.save()

#         # Guardar los detalles (Calificaciones)
#         detalles = []
#         for calificacion_datos in val_detalles:
#             calificacion_nueva = Detalle.objects.create(
#                 CabeceraId=autor_nuevo.CabeceraId, **calificacion_datos)

#             detalles.append(calificacion_nueva)

#         # Armando un diccionario con los datos guardados
#         dict_autor = autor_nuevo.__dict__
#         dict_autor['detalles'] = detalles

#         return dict_autor
