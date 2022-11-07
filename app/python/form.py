from django.forms import ModelForm, TextInput, NumberInput

from app.models import Veiculo


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'ano', 'valor']
        error_messages = {
            'ano': {
                'min_value': 'Necessário informar um valor superior a 2000 para o campo ANO.'
            }
        }
        widgets = {
            'modelo': TextInput(attrs={
                'class': 'form-control', 'autocomplete': 'off'}),
            'marca': TextInput(attrs={
                'class': 'form-control', 'autocomplete': 'off'}),
            'ano': NumberInput(attrs={
                'class': 'form-control'
            }),
            'valor': NumberInput(attrs={
                'class': 'form-control'
            })
        }
