from django import forms


class PizzaForm(forms.Form):
    toppings1 = forms.CharField(label="Toppings1", max_length=100)
    toppings2 = forms.CharField(label="Toppings2", max_length=100)
    size = forms.ChoiceField(
        label="Size",
        choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")],
    )

