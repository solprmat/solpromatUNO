from django import forms


class RegistrarEstudiante(forms.Form):

    CURSOS_SELECCION = (
        ('Seleccione...', 'Seleccione...'),
        ('801', '801'),
        ('802', '802'),
        ('803', '803'),
        ('804', '804'),
    )
    SEXO = (
        ('Seleccione...', 'Seleccione...'),
        ('F', 'F'),
        ('M', 'M'),
    )
    ESTRATO = (
        ('Seleccione...', 'Seleccione...'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    nombreCompleto = forms.CharField(max_length=40, required=True,
                                     label="Nombre Completo",
                                     widget=forms.TextInput(
                                         attrs={
                                             'placeholder': 'Por Favor Escriba su nombre completo',
                                         }
                                     ))
    sexo = forms.ChoiceField(choices=SEXO, label="Genero M (Masculino) F (Femenino)", required=True )
    curso = forms.ChoiceField(choices=CURSOS_SELECCION, label="Curso", required=True)
    estrato = forms.ChoiceField(choices=ESTRATO, label="Estrato", required=True)
    fecha_registro = forms.DateTimeField
