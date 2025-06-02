from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .model import Client
from .serializer import ClientSerializer


class RegistroView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "Cadastro realizado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        cpf = request.data.get('cpf')
        senha = request.data.get('password')

        try:
            cliente = Client.objects.get(cpf=cpf)
            if cliente.password == senha:
                return Response({"mensagem": "Login realizado com sucesso!"})
            else:
                return Response({"erro": "Senha incorreta."}, status=status.HTTP_401_UNAUTHORIZED)
        except Client.DoesNotExist:
            return Response({"erro": "CPF não encontrado."}, status=status.HTTP_404_NOT_FOUND)


class ValoresReceberView(APIView):
    def post(self, request):
        dados = request.data
        # Aqui vai a integração com a API do Alyson, tipo:
        # resposta = requests.post("https://api.alyson.com.br", json=dados)
        # return Response(resposta.json())

        return Response({"mensagem": "Simulação de envio dos dados para API externa", "dados": dados})
