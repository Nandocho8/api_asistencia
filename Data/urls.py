from rest_framework import routers
from django.urls import path, include
from .api import SeccionViewSet, AsistenciaViewSet, ProfesorViewSet, AlumnoViewSet, MatriculaViewSet, AsignaturaViewSet, CarreraViewSet

router = routers.DefaultRouter()

router.register('api/seccion', SeccionViewSet, 'seccion')
router.register('api/asistencia', AsistenciaViewSet, 'asistencia')
router.register('api/profesor', ProfesorViewSet, 'profesor')
router.register('api/alumno', AlumnoViewSet, 'alumno')
router.register('api/matricula', MatriculaViewSet, 'matricula')
router.register('api/asignatura', AsignaturaViewSet, 'asignatura')
router.register('api/carrera', CarreraViewSet, 'carrera')

# urlpatterns = [
#     path('api/login', login, 'login'),
# ]

urlpatterns = router.urls
