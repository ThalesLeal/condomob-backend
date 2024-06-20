from django.core import serializers
from rest_framework import serializers

from core.models import *


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = "__all__"