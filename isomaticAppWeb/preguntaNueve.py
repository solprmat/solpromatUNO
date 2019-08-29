from django import forms


class PreguntaNueve(forms.Form):
    RESPUESTA_PREGUNTA_NUEVE = (
        ('a', 'a. 2km'),
        ('b', 'b. 3km'),
        ('c', 'c. 4km'),
        ('d', 'd. 6km'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_NUEVE,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P09 = forms.DateTimeField