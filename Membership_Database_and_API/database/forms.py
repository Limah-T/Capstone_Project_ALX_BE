from django import forms
from django.core.exceptions import ValidationError
from .models import IndividualMember, CorporateMember

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'required': 'Email field cannot be empty!', 'invalid': 'The email you entered is invalid!'})
    password = forms.CharField(widget=forms.PasswordInput(), error_messages={'required': 'Please enter your password'})

    def clean(self):
        cleaned_data = super().clean()
        # Ensure that cleaned data is not an empty or none value
        if not cleaned_data.get('email'):
            raise ValidationError('Email cannot be empty!')
        if not cleaned_data.get('password'):
            raise ValidationError('Password cannot be empty!')
        return cleaned_data
    
class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualMember
        fields = "__all__"
        exclude = ['is_active', 'past']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply Bootstrap form-control class to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):  # For dropdowns
                field.widget.attrs.update({'class': 'form-select'})
            else:  # For text, email, file, etc.
                field.widget.attrs.update({'class': 'form-control'})

class CooperateForm(forms.ModelForm):
    date_of_establishment = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = CorporateMember
        fields = "__all__"
        exclude = ['is_active', 'past']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply Bootstrap form-control class to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):  # For dropdowns
                field.widget.attrs.update({'class': 'form-select'})
            else:  # For text, email, file, etc.
                field.widget.attrs.update({'class': 'form-control'})