from django import forms
from django.core import validators
class UserRegistrationForm(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName= forms.CharField(widget=forms.Textarea,required=False,validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    lastName=forms.CharField(widget=forms.FileInput)
    email= forms.CharField(required=False)
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)
    ssn=forms.IntegerField()


"""    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName)>20: 
            raise forms.ValidationError('The max length of firstName is 20 characters')
        inputEmail = user_cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('The email should contain @ symbol')
        
    def clean_firstName(self):
        inputFirstname = self.cleaned_data['firstName']
        if len(inputFirstname)>20:
            raise forms.ValidationError('The max length of firstName is 20 characters')
        return inputFirstname
    def clean_email(self):
        inputEmail= self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('The email should contain @ symbol')
        return inputEmail"""