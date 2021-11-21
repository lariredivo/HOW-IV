from django.forms import ModelForm
from blog.models import Assist

class AssistForm(ModelForm):
    class Meta:
        model=Assist
        fields=["name", "CPF", "telephone", "email", "address"]