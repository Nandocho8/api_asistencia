from rest_framework import serializers
from .models import Seccion, Asistencia, Matricula, Carrera, Asignatura, User


class User_Serializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'tipo')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tipo=validated_data['tipo'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class Carrera_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'


class Asignatura_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'code': instance.code_asignatura,
            'nombre': instance.nombre_asignatura,
            'id_carrera': instance.id_carrera.id_carrera,
            'nombre_carrera': instance.id_carrera.nombre_carrera,
            'id_profesor': instance.profesores.id,
            'nombre_profesor': f'{instance.profesores.first_name} {instance.profesores.last_name}'
        }


class Seccion_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'nombre seccion': instance.nom_seccion,
            'codigo asignatura': instance.asignatura.code_asignatura,
            'nombre asignatura': instance.asignatura.nombre_asignatura,
            'nombre profesor': f'{instance.asignatura.profesores.first_name} {instance.asignatura.profesores.last_name}'
        }


class Matricula_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class Asistencia_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'
