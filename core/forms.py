from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput, NumberInput, CheckboxInput, FileInput
from . models import *

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
        widgets = {
                'name': TextInput(attrs={
                    'class':'norm-input',
                    'name':'name',
                    'data-custom': 'some-value',
                    'placeholder': 'Name'
                }),
                'description': Textarea(attrs={
                    'class':'text-input',
                    'name':'description',
                    'rows': 4,
                    'data-custom': 'some-value',
                    'placeholder': 'Description'
                })
            }
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['collection', 'likes', 'views', 'sold_status']
        widgets = {
            'name': TextInput(attrs={
                'class':'norm-input',
                'name':'name',
                'data-custom': 'some-value',
                'placeholder': 'Name'
            }),
            'description': Textarea(attrs={
                'class':'text-input',
                'name':'description',
                'rows': 4,
                'data-custom': 'some-value',
                'placeholder': 'Description'
            }),
            'price': NumberInput(attrs={
                'class':'norm-input',
                'name':'price',
                'data-custom': 'some-value',
                'placeholder': 'Price'
            }),
            'photo': FileInput(attrs={
                'class':'file-input',
                'name':'photo',
                'data-custom': 'some-value',
                
            }),
            'sold_status': CheckboxInput(attrs={
                'class':'check-input',
                'name':'sold',
                'data-custom': 'some-value',
                
            })
        }
class PhoneInfoForm(ModelForm):
    class Meta:
        model = PhoneInfo
        fields = '__all__'
        exclude = ['product']
        widget = {
            'screen_type':TextInput(attrs={
                'class':'norm-input',
                'name':'name',
                'data-custom': 'some-value',
                'placeholder': 'Screen Type'
            }),
            'screen_resolution':TextInput(attrs={
                'class':'norm-input',
                'name':'name',
                'data-custom': 'some-value',
                'placeholder': 'Screen Resolution'
            }),
            'ram': NumberInput(attrs={
                'class':'norm-input',
                'name':'price',
                'data-custom': 'some-value',
                'placeholder': 'RAM'
            }),
            'storage': NumberInput(attrs={
                'class':'norm-input',
                'name':'price',
                'data-custom': 'some-value',
                'placeholder': 'Storage'
            }),
            'camera': NumberInput(attrs={
                'class':'norm-input',
                'name':'price',
                'data-custom': 'some-value',
                'placeholder': 'Camera'
            }),
            'battery': NumberInput(attrs={
                'class':'norm-input',
                'name':'price',
                'data-custom': 'some-value',
                'placeholder': 'Battery'
            }),
        }