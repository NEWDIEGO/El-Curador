from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def hello(request): 
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse('About')

def vista_medico(request):
    # abrir el contenido del archivo HTML medico.html
    plantilla_ext = open("myapp\Templates\Especialista.html")

    # cargar el contenido del archivo HTML
    template = Template(plantilla_ext.read())
    
    # cerrar el contenido del archivo HTML medico.html
    plantilla_ext.close()
    
    #crear contexto
    contexto = Context()

    #renderizar documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def Vista_EspecialistaPerfil(request):
    
    plantilla_ext = open("myapp\Templates\EspecialistaPerfil.html")

    
    template = Template(plantilla_ext.read())
    
   
    plantilla_ext.close()
    
   
    contexto = Context()

    
    documento = template.render(contexto)
    return HttpResponse(documento)

def Vista_EspecialistaLista(request):
    plantilla_ext = open("myapp\Templates\EspecialistaLista.html")

    
    template = Template(plantilla_ext.read())
    
    plantilla_ext.close()

    contexto = Context()

  
    documento = template.render(contexto)
    return HttpResponse(documento)