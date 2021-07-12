from django import forms
from.models import Products
from django.forms import ModelForm



 
class ProductForm(ModelForm):
  
    class Meta:
        model=Products
        fields=['name','weight','price']
        