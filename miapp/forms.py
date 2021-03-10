from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Título",
        max_length = 100,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ingresa el título',
                'class' : 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'Solo puede ingresar letras y números','00x45er')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea
    )

    content.widget.attrs.update({
        'placeholder': 'Ingresa el contenido',
        'class' : 'contenido_form_article'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = '¿Publicado?',
        choices = public_options
    )