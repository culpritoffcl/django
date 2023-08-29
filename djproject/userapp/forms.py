from django.forms import ModelForm


from .models import userDetails


class UserForm(ModelForm):
    class Meta:
        model=userDetails