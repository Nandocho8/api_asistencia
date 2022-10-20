from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Seccion, Asistencia, User, Matricula, Asignatura, Carrera
from rest_framework import viewsets, permissions


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    email = data['email']
    password = data['password']

    try:
        user = User.objects.get(email=email)
    except:
        return Response('Usuario Invalido')

    pass_valido = check_password(password, user.password)

    if not pass_valido:
        return Response('Password incorrecta')

    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key,
                    "id": user.id,
                     "tipo": user.tipo})
