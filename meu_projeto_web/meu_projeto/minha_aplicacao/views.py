from django.shortcuts import render

# Create your views here.
def index(request):
    nome= ""
    if request.method == "POST":
        nome = request.POST.get("nome", "")
    return render(request, "minha_aplicacao/index.html", {"nome": nome})