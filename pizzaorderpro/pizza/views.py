from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, "home.html")


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = f"Thanks for Ordering. Your {filled_form.cleaned_data['size']} sized {filled_form.cleaned_data['toppings1']}  and {filled_form.cleaned_data['toppings2']} Pizza is on the way"
            pizzaformnew = PizzaForm()
            return render(
                request, "order2.html", {"pizzaform": pizzaformnew, "note": note}
            )

    else:
        pizzaform = PizzaForm()
        return render(request, "order2.html", {"pizzaform": pizzaform})
