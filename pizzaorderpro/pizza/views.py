from django.shortcuts import render
from .forms import PizzaForm
from .forms import MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza


def home(request):
    return render(request, "home.html")


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            pizza_pk = created_pizza.id
            note = f"Thanks for Ordering. Your {filled_form.cleaned_data['size']} sized {filled_form.cleaned_data['toppings1']}  and {filled_form.cleaned_data['toppings2']} Pizza is on the way"
            filled_form = PizzaForm()
        else:
            note="Enter Correct Details"
            pizza_pk= None

        return render(
                request,
                "order2.html",
                {
                    "pizzaform":filled_form,
                    "note": note,
                    "multiple_form": multiple_form,
                    "pizza_pk": pizza_pk,
                },
            )
        
    else:
        pizzaform = PizzaForm()
        return render(
            request,
            "order2.html",
            {"pizzaform": pizzaform, "multiple_form": multiple_form},
        )

#/pizzas&2
def pizzas(request):
    num_of_pizzas = 2
    filled_multiple_pizzaform = MultiplePizzaForm(request.GET)
    if filled_multiple_pizzaform.is_valid():
        num_of_pizzas = filled_multiple_pizzaform.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm,extra=num_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['toppings1'])
            note = 'Pizzas have been Ordered'
        else:
            note = 'Please Try Again'

        return render(request, "pizza.html",{"note":note,"formset":formset})
    else:
        return render(request, "pizza.html",{"formset":formset})


def edit_order(request,pk):
    pizza = Pizza.objects.get(pk = pk)
    form = PizzaForm(instance=pizza)
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            note = "Edit Saved"
            filled_form.save()
            form = filled_form
        return render(request, "edit_order.html",{"note":note,"form":form,"pizza":pizza})
    return render(request, "edit_order.html",{"form":form,"pizza":pizza})





