from django import forms


class PreguntaDos(forms.Form):
    RESPUESTA_PREGUNTA_DOS = (
        ('a', 'a.'),
        ('b', 'b.'),
        ('c', 'c.'),
    )

    respuesta = forms.TypedChoiceField(
        # label='preubas',
        choices=RESPUESTA_PREGUNTA_DOS,
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-indicator',

        })
    )
    fecha_registro_P02 = forms.DateTimeField