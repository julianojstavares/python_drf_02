from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'O CPF digitado é inválido'})

        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'O Nome deve ser apenas texto'})

        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve conter 9 dígitos'})
        
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular':'O Celular deve seguir este padrão 00 00000-0000'})

        return data




