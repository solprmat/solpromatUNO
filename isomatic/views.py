from django.shortcuts import render


# ruta a la primera pagina
def tips(request):
    return render(request, "tips.html",{})


def inicio(request):
    return render(request, "index.html", {})
#
# def pregunta2(request):
#     return render(request, "pregunta2.html", {})
#
# def pregunta3(request):
#     return render(request, "pregunta3.html", {})
#
# def pregunta4(request):
#     return render(request, "pregunta4.html", {})
#
# def pregunta5(request):
#     print('Ingreso a la pagina 5')
#     return render(request, "pregunta5.html", {})
#
# def pregunta6(request):
#     print('Ingreso a la pagina 6')
#     return render(request, "pregunta6.html", {})
# def pregunta7(request):
#     print('Ingreso a la pagina 7')
#     return render(request, "pregunta7.html", {})
# def pregunta8(request):
#     print('Ingreso a la pagina 8')
#     return render(request, "pregunta8.html", {})
# def pregunta9(request):
#     print('Ingreso a la pagina 9')
#     return render(request, "pregunta9.html", {})
# def pregunta10(request):
#     print('Ingreso a la pagina 10')
#     return render(request, "pregunta10.html", {})


