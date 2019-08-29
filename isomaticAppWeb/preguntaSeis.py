from django import forms


class PreguntaSeis(forms.Form):
    RESPUESTA_PREGUNTA_SEIS = (
        ('a', 'a. 7 rectángulos'),
        ('b', 'b. 5 rectángulos'),
        ('c', 'c. 10 rectángulos'),
        ('d', 'd. Es imposible de realizar.'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_SEIS,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P06 = forms.DateTimeField