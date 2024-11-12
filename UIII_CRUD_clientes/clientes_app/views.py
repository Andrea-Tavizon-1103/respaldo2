from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.

def inicio_vistas(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes": losclientes})

def registrarCliente(request):
        ID_Cliente = request.POST["txtID_Cliente"]
        Nombre = request.POST["txtNombre"]
        Apellido = request.POST["txtApellido"]
        Email = request.POST["txtEmail"]
        Telefono = request.POST["numTelefono"]
        Direccion = request.POST["txtDireccion"]
        Fecha_Registro = request.POST["numFechaRegistro"]

        registrarCliente = Cliente.objects.create(ID_Cliente=ID_Cliente, Nombre=Nombre, Apellido=Apellido, Email=Email, Telefono=Telefono, Direccion=Direccion, Fecha_Registro=Fecha_Registro)

        return redirect("/")

def borrarCliente(request, ID_Cliente):
    Cliente = Cliente.objects.get(ID_Cliente=ID_Cliente)
    Cliente.delete()

    return redirect("/")

def seleccionarCliente(request, ID_Cliente):
    Cliente = Cliente.objects.get(ID_Cliente=ID_Cliente)

    return render(request, "editarCliente.html", {"misclientes":Cliente})

def editarCliente(request):
    ID_Cliente = request.POST["txtID_Cliente"]
    Nombre = request.POST["txtNombre"]
    Apellido = request.POST["txtApellido"]
    Email = request.POST["txtEmail"]
    Telefono = request.POST["numTelefono"]
    Direccion = request.POST["txtDireccion"]
    Fecha_Registro = request.POST["numFechaRegistro"]

    Cliente = Cliente.objects.get(ID_Cliente=ID_Cliente)

    Cliente.Nombre = Nombre
    Cliente.Apellido = Apellido
    Cliente.Email = Email
    Cliente.Telefono = Telefono
    Cliente.Direccion = Direccion
    Cliente.Fecha_Registro = Fecha_Registro
    Cliente.save()
    return redirect("/")