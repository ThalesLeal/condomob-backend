import pandas as pd
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import viewsets, permissions
from core.models import *
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication)
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.serializers import *


class DocumentoViewSet(LoggingMixin,viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    authentication_classes =[
        JWTAuthentication,
        SessionAuthentication,
        BasicAuthentication,
        ]
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


    def create(self, request):
        import pdb; pdb.set_trace()