from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CarrinhoAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
    )
    # HiddenInput -> para não mostrar para o cliente
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
    )