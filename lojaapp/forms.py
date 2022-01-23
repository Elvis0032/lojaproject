from tkinter import Widget
from django import forms
from.models import Pedido_order, Cliente
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
        
        
        

class ClienteRegistrarForm(forms.ModelForm):
    
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario','class':"form-control", 'style':'width:300px; display:flex;'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Senha','class':"form-control", 'style':'width:300px; display:flex;'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Ex: fulano3@gmail.com','class':"form-control", 'style':'width:300px; display:flex;'}))
         
    class Meta:
        model = Cliente
        fields = ["usuario","senha","email","nome_completo","endereco"]        
        widgets = {
            'nome_completo': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'Nome Completo'
            }),
            'endereco': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'Rua/Bairro/Cidade/Estado/CEP'
            }),
        }
        
        