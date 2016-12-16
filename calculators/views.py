from django.shortcuts import render, HttpResponseRedirect

from .models import Person

def calculators(request):
    """Widok umożliwiający wybór kalkulatora."""
    return render(
        request,
        "calculators/base.html",
    )


def calc_choose(request):
    """Funkcja przekierowująca użytkownika do
    kalkulatora bmi lub kalkulatora kalorii."""

    if "bmi" in request.POST:
        # usunięcie zawartości słownika request.session
        request.session.clear()

        # przekierowanie do adresu url calkulatora bmi
        return HttpResponseRedirect("/calculators/bmi_calculator/")

    elif "calories" in request.POST:
        # przekierowanie do adresu url calkulatora kalorii
        return HttpResponseRedirect("/calculators/calories_calculator/")


def view_main_calories(request):
    """Podstawowy widok kalkulatora kalorii."""
    return render(
        request,
        "calculators/calories.html",
    )


def get_default_contex():
    """Funkcja zwracająca podstawowy kontekst. """
    return {"sex": ("kobieta", "mężczyzna")}


def view_main_bmi(request):
    """Podstawowy widok kalkulatora bmi."""

    contex = get_default_contex()
    contex["error"] = request.session.get("error")

    return render(
        request,
        "calculators/bmi.html",
        contex
    )


def view_count_bmi(request):
    """Funkcja służąca do obliczeń wartości bmi
    na podstawie wartości podanych przez użytkownika.
    """

    # próba pobrania danych wprowadzonych przez użytkownika
    try:
        sex = request.POST["chosen_sex"]
        height = float(request.POST["height"].replace(",", "."))
        weight = float(request.POST["weight"].replace(",", "."))

    # przekierowanie do poprzedniego url w przypadku wystąpienia wyjątku
    except (KeyError, ValueError):
        request.session["error"] = "Wprowadzono nieprawidłowe dane."
        return HttpResponseRedirect("/calculators/bmi_calculator/")

    # usunięcie ze słownika request.session klucza "error"
    request.session.delete("error")

    # utworzenie obiektu clasy Person
    person = Person(sex=sex, weight=weight, height=height)

    # obliczenie indeksu bmi oraz kategorii wagowej
    bmi_result, weight_type = person.get_bmi()

    # dodanie obliczonych wartości bmi oraz
    # kategori wagowej do słownika request.session
    request.session.update({
        "bmi_result": bmi_result,
        "weight_type": weight_type,
        "height": height,
        "weight": weight
    })

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button !!
    return HttpResponseRedirect("/calculators/bmi_result/")


def view_bmi_result(request):
    """Widok zawierający obliczony wynik bmi dla użytkownika."""
    context = get_default_contex()
    context.update({
        "bmi_result": request.session["bmi_result"],
        "weight_type": request.session["weight_type"],
        "height": request.session["height"],
        "weight": request.session["weight"]
    })

    return render(
        request,
        "calculators/bmi_results.html",
        context
    )
