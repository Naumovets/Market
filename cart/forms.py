from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.TextInput(attrs={
        'class': 'form-control text-center',
        'value': 1,
        'max': 20,
        'min': 1,
        'aria-describedby': 'button-addon1',
        'type': 'number'
    }))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)