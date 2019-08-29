from django import forms


class PreguntaCuatro(forms.Form):
    RESPUESTA_PREGUNTA_CUATRO = (
        ('a', 'a. 418'),
        ('b', 'b. 450'),
        ('c', 'c. 403'),
        ('d', 'd. 420'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_CUATRO,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P04 = forms.DateTimeField