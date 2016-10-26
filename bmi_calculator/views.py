from django.shortcuts import render, HttpResponseRedirect


def get_defoult_contex():
    """Funkcja zwracająca podstawowy kontekst. """
    return {"sex": ("kobieta", "męszczyzna")}


def view_main_bmi(request):
    """Podstawowy widok aplikacji bmi."""
    return render(
        request,
        "bmi_calculator/bmi.html",
        get_defoult_contex()
    )


def view_count_bmi(request):
    """Funkcja służąca do obliczeń wartości bmi na podstawie wartości podanych przez użytkownika."""

    # próba pobrania danych wprowadzonych przez użytkownika
    try:
        sex = request.POST["chosen_sex"]
        height = float(request.POST["height"])
        weight = float(request.POST["weight"])

    # przekierowanie do poprzedniego url w przypadku wystąpienia wyjątku
    except (KeyError, ValueError):
        return HttpResponseRedirect("/bmi_calculator/")

    # właściwe obliczanie bmi
    bmi_result = round(weight / height ** 2, 2)

    # sprawdzenie kategori wagowej
    weight_type = None

    if sex == "kobieta":
        if bmi_result <= 17.5:
            weight_type = "niedowaga"
        elif 17.5 < bmi_result <= 22.5:
            weight_type = "normalna waga"
        elif 22.5 < bmi_result <= 27.5:
            weight_type = "nadwaga"
        else:
            weight_type = "otyłość"
    else:
        if bmi_result <= 20:
            weight_type = "niedowaga"
        elif 20 < bmi_result <= 25:
            weight_type = "normalna waga"
        elif 25 < bmi_result <= 30:
            weight_type = "nadwaga"
        else:
            weight_type = "otyłość"

    # dodanie obliczonych wartości bmi oraz kategori wagowej do słownika request.session
    request.session["bmi_result"] = bmi_result
    request.session["weight_type"] = weight_type

    return HttpResponseRedirect("/bmi_calculator/result/")


def view_bmi_result(request):
    """Widok zawierający obliczony wynik bmi dla użytkownika."""
    context = get_defoult_contex()
    context.update({
        "bmi_result": request.session["bmi_result"],
        "weight_type": request.session["weight_type"]
    })

    return render(
        request,
        "bmi_calculator/bmi_results.html",
        context
    )