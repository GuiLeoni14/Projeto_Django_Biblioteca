from django.forms import ModelForm
from app.models import livro, emprestimo

# Create the form class.
class livroForm(ModelForm):
    class Meta:
        model = livro
        fields = ["nome", "autor", "data", "quantidade", "editora", "tipo", "localizacao"]


class emprestimoForm(ModelForm):
    class Meta:
        model = emprestimo
        fields = ["nome", "dataem", "pessoa", "quantidadeem"]
