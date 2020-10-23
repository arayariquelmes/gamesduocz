from django.shortcuts import render

# Create your views here.
def home(request):
    productos = []
    for i in range(1,10):
        prod = {"nombre": "producto " + str(i), "precio": i * 1000}
        productos.append(prod)
    return render(request, "index.html", {'titulo': 'Nuestros productos son lo mejor ya tu sabes', 'productos':productos})

def contacto(request):
    return render(request,"contacto.html")