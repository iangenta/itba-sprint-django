from cProfile import label
from socket import fromshare
from django import forms
from apps.clientes.models import Cliente

class clienteForms(forms.ModelForm):
    class Meta:
        model=Cliente
        
        fields= [ 'cliente_id','nombre_cliente','apellido_cliente','dni_cliente','tipo_cliente','numero_tarjeta',
        ]
        labels={'cliente_id': 'ID', 
                'nombre_cliente': 'Nombre',
                'apellido_cliente':'Apellido',
                'dni_cliente':'DNI',
                'tipo_cliente':'Tipo',
                'numero_tarjeta':'Numero de Tarjeta',
        }

        widgets ={
            'cliente_id': forms.IntegerField(attrs={'class':'form-control'}),
            'nombre_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'dni_cliente': forms.IntegerField(attrs={'class':'form-control'}),
            'tipo_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'numero_tarjeta':forms.TextInput(attrs={'class':'form-control'}),
        }

