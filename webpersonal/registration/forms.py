from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'nombres', 'apellidos', 'domicilio', 'telefono', 'obra_social', 'dni']
        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control-file mt-3','placeholder':'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control-file mt-3','placeholder':'Apellidos'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control-file mt-3','placeholder':'Domicilio'}),
            'telefono': forms.TextInput(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Teléfono'}),
            'obra_social': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Obra Social'}),
            'dni': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'DNI'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email