from rest_framework.decorators import action
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import viewsets, permissions
from core.models import Documento
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from core.serializers import DocumentoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.http import HttpResponse

import hashlib
import logging
import pandas as pd
import json


logger = logging.getLogger(__name__)

class DocumentoViewSet(LoggingMixin, viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    authentication_classes = [
        JWTAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        file = request.FILES.get('documento')

        if file is None:
            return Response({'error': 'Nenhum arquivo foi enviado'}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.csv'):
            return Response({'error': 'Arquivo não é do tipo CSV'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = pd.read_csv(file, delimiter=',', encoding='utf-8')
            
            columns = [
                'ID_CONDOMINIO', 'ID_UNIDADE', 'VENCIMENTO', 'DATA_DE_COMPETENCIA', 
                'CONTA_BANCARIA', 'NOSSO_NUMERO', 'TOKEN-FACILITADOR', 'TOKEN-CONTA',
                'RECEITA_APROPRIACAO1[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO1[COMPLEMENTO]', 'RECEITA_APROPRIACAO1[VALOR]',
                'RECEITA_APROPRIACAO2[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO2[COMPLEMENTO]', 'RECEITA_APROPRIACAO2[VALOR]',
                'RECEITA_APROPRIACAO3[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO3[COMPLEMENTO]', 'RECEITA_APROPRIACAO3[VALOR]',
                'RECEITA_APROPRIACAO4[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO4[COMPLEMENTO]', 'RECEITA_APROPRIACAO4[VALOR]',
                'RECEITA_APROPRIACAO5[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO5[COMPLEMENTO]', 'RECEITA_APROPRIACAO5[VALOR]',
                'RECEITA_APROPRIACAO6[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO6[COMPLEMENTO]', 'RECEITA_APROPRIACAO6[VALOR]',
                'RECEITA_APROPRIACAO7[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO7[COMPLEMENTO]', 'RECEITA_APROPRIACAO7[VALOR]',
                'RECEITA_APROPRIACAO8[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO8[COMPLEMENTO]', 'RECEITA_APROPRIACAO8[VALOR]',
                'RECEITA_APROPRIACAO9[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO9[COMPLEMENTO]', 'RECEITA_APROPRIACAO9[VALOR]',
                'RECEITA_APROPRIACAO10[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO10[COMPLEMENTO]', 'RECEITA_APROPRIACAO10[VALOR]',
                'RECEITA_APROPRIACAO11[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO11[COMPLEMENTO]', 'RECEITA_APROPRIACAO11[VALOR]',
                'RECEITA_APROPRIACAO12[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO12[COMPLEMENTO]', 'RECEITA_APROPRIACAO12[VALOR]',
                'RECEITA_APROPRIACAO13[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO13[COMPLEMENTO]', 'RECEITA_APROPRIACAO13[VALOR]',
                'RECEITA_APROPRIACAO14[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO14[COMPLEMENTO]', 'RECEITA_APROPRIACAO14[VALOR]',
                'RECEITA_APROPRIACAO15[CONTA_CATEGORIA]', 'RECEITA_APROPRIACAO15[COMPLEMENTO]', 'RECEITA_APROPRIACAO15[VALOR]',
                'TAXA_DE_JUROS', 'TAXA_DE_MULTA', 'TAXA_DE_DESCONTO', 'COBRANCA_EXTRAORDINARIA'
            ]
            
            final_df = pd.DataFrame(columns=columns)
            grouped = data.groupby('ID_VALIDACAO')

            def combine_rows(group):
                row = {
                    'ID_CONDOMINIO': group['ID_CONDOMINIO'].iloc[0],
                    'ID_UNIDADE': group['ID_UNIDADE'].iloc[0],
                    'VENCIMENTO': group['VENCIMENTO'].iloc[0],
                    'DATA_DE_COMPETENCIA': group['DATA_DE_COMPETENCIA'].iloc[0],
                    'CONTA_BANCARIA': group['CONTA_BANCARIA'].iloc[0],
                    'NOSSO_NUMERO': group['NOSSO_NUMERO'].iloc[0],
                    'TOKEN-FACILITADOR': group['TOKEN-FACILITADOR'].iloc[0] if 'TOKEN-FACILITADOR' in group else None,
                    'TOKEN-CONTA': group['TOKEN-CONTA'].iloc[0] if 'TOKEN-CONTA' in group else None,
                    'TAXA_DE_JUROS': group['TAXA_DE_JUROS'].iloc[0],
                    'TAXA_DE_MULTA': group['TAXA_DE_MULTA'].iloc[0],
                    'TAXA_DE_DESCONTO': group['TAXA_DE_DESCONTO'].iloc[0],
                    'COBRANCA_EXTRAORDINARIA': group['COBRANCA_EXTRAORDINARIA'].iloc[0] if 'COBRANCA_EXTRAORDINARIA' in group else None,
                }
                for i, (_, sub_df) in enumerate(group.iterrows(), start=1):
                    row[f'RECEITA_APROPRIACAO{i}[CONTA_CATEGORIA]'] = sub_df['CONTA_CATEGORIA']
                    row[f'RECEITA_APROPRIACAO{i}[COMPLEMENTO]'] = sub_df['COMPLEMENTO']
                    row[f'RECEITA_APROPRIACAO{i}[VALOR]'] = sub_df['VALOR']
                return pd.Series(row)

            combined_rows = [combine_rows(group) for _, group in grouped]
            final_df = pd.concat([final_df, pd.DataFrame(combined_rows)], ignore_index=True)
            final_df = final_df.where(pd.notnull(final_df), '')
           
            records = final_df.to_dict(orient='records')
            data_json = json.dumps(records, ensure_ascii=False)

            file.seek(0)
            file_content = file.read()
            hashed_data = hashlib.sha256(file_content).hexdigest()

            user = request.user

            Documento.objects.create(
                dados=json.loads(data_json),
                data_gerado=timezone.now(),
                usuario=user
            )
            
            return Response({'message': 'Dados do CSV salvos como JSON no ArquivoHash'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def segunda_via(self, request):
        arquivo_id = request.data.get('id_arquivo')
        
        try:
            documento = Documento.objects.get(id=arquivo_id)
        
            df = pd.DataFrame(documento.dados)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="dados_arquivo_{arquivo_id}.csv"'
            df.to_csv(path_or_buf=response, index=False, sep=',')
            
            return response
        
        except Documento.DoesNotExist:
            return Response({'error': 'Documento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)