from django import forms
from .models import Producto

""" 
    FORMULARIO DE PRODUCTOS 
"""
class FormProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('titulo','imagen','descripcion','precio','categoria')
        """ widgets = {
            'titulo': forms.TextInput(),
            'descripcion' : forms.Textarea(),
            'precio' : forms.NumberInput(),
            'imagen' : forms.FileField()
        } """
        """ widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre del producto...' , 'required': True}),
            'descripcion' : forms.Textarea(attrs={'class' : 'form-control', 'row' : 3, 'required': True}),
            'precio' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder':'XXXX.XX', 'required': True}),
            'imagen' : forms.FileField(attrs={'class':'form-control-file', 'id':'imagen', 'placeholder': 'Ingrese la imagen...', 'required': True})
        } """
