from django import forms


class PreguntaOcho(forms.Form):
    RESPUESTA_PREGUNTA_OCHO = (
        ('a', 'a. 300'),
        ('b', 'b. 265'),
        ('c', 'c. 530'),
        ('d', 'd. 305'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_OCHO,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P08 = forms.DateTimeField