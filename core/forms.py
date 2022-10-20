from random import choices
from django import forms
from .models import register
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils.translation import gettext_lazy as _


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'
    #     'job_title',
    #     'company_name',
    #     'location',
    #     'job_about' ,
    #     'work_schedule',
    #     'currency',
    #     'salary',
    #     'company_website',
    #     'return_number',
    #     'return_email',
    #     'category',
    #     'tags',
    #     ]
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': _('Username')}),
        #     'email': forms.EmailInput(attrs={'class': _('example@email.com')}),
        #     'password1': forms.PasswordInput(attrs={'class': _('password')}),
        #     'password2': forms.PasswordInput(attrs={'class': _('password2')}),
        # }
    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': ("first name")})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': ("last name")})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': ("example@email.com")})
        self.fields['phone_number'].widget = forms.TextInput(attrs={'placeholder': ("+234123456778")})
        self.fields['country'].widget = forms.TextInput(attrs={'placeholder': ("return phone number")})
       
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': ("form-control"),'placeholder': ("first name")})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': ("form-control"),'placeholder': ("last name")})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': ("form-control"),'placeholder': ("example@email.com")})
        self.fields['phone_number'].widget = forms.TextInput(attrs={'class': ("form-control"),'placeholder': ("+234123456778")})
        self.fields['country'].widget = forms.TextInput(attrs={'class': ("form-control")})

        # self.fields['Wassce_Waec'].widget = forms.FileInput(attrs={'class': ("form-control"),'placeholder': ("Mass communication")})
    

