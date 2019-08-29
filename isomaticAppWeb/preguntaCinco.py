from django import forms


class PreguntaCinco(forms.Form):
    RESPUESTA_PREGUNTA_CINCO = (
        ('a', 'a. 10.000'),
        ('b', 'b. 7.600'),
        ('c', 'c. 2.500'),
        ('d', 'd. 8.000'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_CINCO,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P05 = forms.DateTimeField