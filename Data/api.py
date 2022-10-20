from rest_framework import viewsets, permissions
from .models import Seccion, Asistencia, User, Matricula, Asignatura, Carrera
from .serializers import User_Serializers, Seccion_Serializers, Asistencia_Serializers, Matricula_Serializers, Asignatura_Serializers, Carrera_Serializers
from ApiQR import settings


class SeccionViewSet(viewsets.ModelViewSet):

    queryset = Seccion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Seccion_Serializers


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Asistencia_Serializers


class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(tipo='P')
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(tipo='A')
    permission_classes = [permissions.AllowAny]
    serializer_class = User_Serializers


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Matricula_Serializers


class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Asignatura_Serializers


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Carrera_Serializers
