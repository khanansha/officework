from django import forms
from .models import Registrationform 

class SubmitEmbed(forms.Form):
    url = forms.URLField()

class RegForm(forms.ModelForm):  
    email=forms.EmailField(max_length=50)
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    mobile_no=forms.CharField(max_length=10)
    password=forms.CharField(max_length=30)
    con_password=forms.CharField(max_length=30)

    class Meta:  
        model = Registrationform 
        fields = "__all__"    


    def clean_first(self):
        user=self.cleaned_data['first_name']
        try:
            match=Registrationform.object.get(first_name=user)
        except:
            return self.changed_data['first_name']
        raise forms.ValidationError("username already exsit")   

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            mt=validate_email(email)
        except:
            return forms.ValidationError("email is not in correct format")
        return email 


    def clean_confirmpass(self):
        pas=self.cleaned_data['password']    
        cpas=self. cleaned_data['con_password'] 
        MIN_LENGTH=8
        if pas and cpas:
            if pas !=cpas:
                raise forms.ValidationError("password and confirm password are not matched")   
            else:
                if len(pas)<MIN_LENGTH:
                    raise forms.ValidationError("password is too short")     
                if pas.isdigit():
                    raise forms.ValidationError("password should not all numeric")  


