from django import forms


class PreguntaSiete(forms.Form):
    RESPUESTA_PREGUNTA_SIETE = (
        ('a', 'a. 24 veces'),
        ('b', 'b. 12 veces'),
        ('c', 'c. 36 veces'),
        ('d', 'd. 48 veces'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_SIETE,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P07 = forms.DateTimeField