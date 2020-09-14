from django.shortcuts import render

from django.http import HttpResponse

from usuario.models import Usuario
# Create your views here.

def login(request):
    return render(request,'base.html')

def listar(request):
    lista = Usuario.objects.all()
    lista2 = [1,2,4,5,6,7,8]
    context = {'usuarios': lista, 'saludo': 'holis', 'numeros': lista2}

    return render(request, 'listar.html', context)

def perfil(request, identificador):
    usuario = Usuario.objects.get(usuario_id=identificador)
    context = {'dato': usuario}
    return render(request, 'detalle.html', context)

def nuevo(request):
	if request.POST:
		post = request.POST
		nuevo_usuario = Usuario(post['id'], post['nombre'], post['telefono'], post['email'], post['contrasena'], post['domicilio'])
		nuevo_usuario.save()

	return render(request, 'nuevo.html')

    def alta(request):

        return render()