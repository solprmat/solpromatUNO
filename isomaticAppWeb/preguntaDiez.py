from django import forms


class PreguntanDiez(forms.Form):
    RESPUESTA_PREGUNTA_DIEZ = (
        ('a', 'a. Ana'),
        ('b', 'b. Jana'),

    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_DIEZ,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P010 = forms.DateTimeField