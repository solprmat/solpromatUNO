from django import forms


class PreguntaTres(forms.Form):
    RESPUESTA_PREGUNTA_TRES = (
        ('a', 'a. 50.000'),
        ('b', 'b. 20.000'),
        ('c', 'c. 30.000'),
        ('d', 'd. 40.000'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_TRES,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P03 = forms.DateTimeField