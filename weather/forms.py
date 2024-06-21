from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'City Name'
            })
        }