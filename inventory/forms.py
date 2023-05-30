from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['brand'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['description'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = Stock
        fields = ['name', 'brand' , 'quantity', 'price', 'description']
