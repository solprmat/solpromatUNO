from django import forms


class PreguntaUno(forms.Form):
    RESPUESTA_PREGUNTA_UNO = (
        ('a', 'a. 40 km/h'),
        ('b', 'b. 20 km/h'),
        ('c', 'c. 80 km/h'),
        ('d', 'd. 100 km/h'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_UNO,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P01 = forms.DateTimeField
