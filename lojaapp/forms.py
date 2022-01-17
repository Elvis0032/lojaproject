from tkinter import Widget
from django import forms
from.models import Pedido_order
from django.db.models import fields
from django.forms import ModelForm, TextInput, EmailInput




class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordenando_por","endereco_envio","telefone","email" ]        
        widgets = {
            'ordenando_por': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'Pedido por'
            }),
            'endereco_envio': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'Rua/Bairro/Cidade/Estado/CEP'
            }),
            'telefone': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'Ex: 82 999555333'
            }),
            'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'Ex: fulano3@gmail.com'
            }),
        }
        
        