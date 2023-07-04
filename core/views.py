from django.shortcuts import redirect, render
from .models import Usuario, Producto
from .forms import RegistrationForm
from django.views import View
from django.contrib.auth.views import RegisterView


# Create your views here.


def home(request):
    return render(request, "core/home.html")

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireccionar a la página de inicio de sesión
        return render(request, 'register.html', {'form': form})

def Validar_registro(request):
    data = {"mesg": "", "form": RegistrationForm, "usuario": ""}

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            try:
                cuenta = request.POST.get('cuenta')
                rut = request.POST.get('rut')
                objeto = Usuario.objects.get(cuenta=cuenta, rut=rut)
                data["mesg"] = "¡La cuenta y el rut son correctos!"
                data["usuario"] = Usuario.objects.get(cuenta=cuenta)
                return render(request, "core/VerDatosPersona.html", data)
            except:
                data["mesg"] = "¡La cuenta o el rut no son correctos!"
    return render(request, "core/ValidarPersona.html", data)

def usuario(request, action, id):
    data = {"mesg": "", "form": RegistrationForm, "action": action, "id": id}


    if action == 'ins':
        if request.method == "POST":
            form = RegistrationForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El Usuario fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos usuarios con el mismo Rut!"
    elif action == 'upd':
        objeto = Usuario.objects.get(rut=id)
        if request.method == "POST":
            form = RegistrationForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El usuario fue actualizado correctamente!"
        data["form"] = RegistrationForm(instance=objeto)


    elif action == 'del':
        try:
            Usuario.objects.get(rut=id).delete()
            data["mesg"] = "¡El usuario fue eliminado correctamente!"
            return redirect(usuario, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El usuario ya estaba eliminado!"


    data["list"] = Usuario.objects.all().order_by('rut')
    return render(request, "core/vehiculo.html", data)


def poblar_bd(request):
    Usuario.objects.all().delete()
    Usuario.objects.create(rut="4704704-8", nombres='Valentina', apellido="Corral",email="",direccion="", imagen="images/saleen.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="25521511-6", nombres='Samuel', apellido="Fariña",email="",direccion="",imagen="images/saleen.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="5856145-2", nombres='Carmen', apellido="Llanos",email="",direccion="", imagen="images/cobra.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="17146729-2", nombres='Maria', apellido="Galiano",email="",direccion="", imagen="images/pagoda.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="14962484-8", nombres='Evangelina', apellido="Rosello",email="",direccion="", imagen="images/wolf.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="20139651-4", nombres='Mar', apellido="Sastre",email="",direccion="", imagen="images/flathead.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="25401013-8", nombres='Teodoro', apellido="Valdes",email="",direccion="", imagen="images/phantom.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="20383637-6", nombres='Juan', apellido="Leon",email="",direccion="", imagen="images/mustang.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="34860225-k", nombres='Martina', apellido="Roldan",email="",direccion="", imagen="images/motoiron.jpg", usuario=Usuario.objects.get(rut=3))
    Usuario.objects.create(rut="31031276-2", nombres='Alejo', apellido="Portillo",email="",direccion="", imagen="images/silver.jpg", usuario=Usuario.objects.get(rut=3))
    return redirect(usuario, action='ins', id = '-1')


""""
def home(request):
    return render(request, "core/home.html")

def vehiculo_tienda(request):
    data = {"list": Usuario.objects.all().order_by('rut')}
    return render(request, "core/vehiculo_tienda.html", data)

def vehiculo_ficha(request, id):
    vehiculo = Usuario.objects.get(rut=id)
    data = {"vehiculo":  vehiculo}
    return render(request, "core/vehiculo_ficha.html", data)

def vehiculo(request, action, id):
    data = {"mesg": "", "form": VehiculoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = VehiculoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El vehículo fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos vehículos con la misma rut!"

    elif action == 'upd':
        objeto = Usuario.objects.get(rut=id)
        if request.method == "POST":
            form = VehiculoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El vehículo fue actualizado correctamente!"
        data["form"] = VehiculoForm(instance=objeto)

    elif action == 'del':
        try:
            Usuario.objects.get(rut=id).delete()
            data["mesg"] = "¡El vehículo fue eliminado correctamente!"
            return redirect(vehiculo, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El vehículo ya estaba eliminado!"

    data["list"] = Usuario.objects.all().order_by('rut')
    return render(request, "core/vehiculo.html", data)


def poblar_bd(request):
    Usuario.objects.all().delete()
    Usuario.objects.create(rut="ALAN67", nombres='Volvo', apellido="Volvo Station Wagon", imagen="images/volvosw.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="BILL88", nombres='Saleen', apellido="S7", imagen="images/saleen.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="ELVI54", nombres='Shelby', apellido="Cobra de 1967", imagen="images/cobra.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="FEDE84", nombres='Mercedes-Benz', apellido="Pagoda de 1972", imagen="images/pagoda.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="JEFF46", nombres='Ford', apellido="Wolf WR1 Ford Race Car", imagen="images/wolf.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="JOHN80", nombres='Ford', apellido="Flathead Roadster de 1932", imagen="images/flathead.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="PAUL62", nombres='Rolls-Royce', apellido="Phantom", imagen="images/phantom.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="SCAR47", nombres='Mustang', apellido="Mustang de 1970", imagen="images/mustang.jpg", usuario=Usuario.objects.get(rut=2))
    Usuario.objects.create(rut="TIRO98", nombres='Mercedes-Benz', apellido="Iron Bike de 1998", imagen="images/motoiron.jpg", usuario=Usuario.objects.get(rut=3))
    Usuario.objects.create(rut="UVAM20", nombres='Silver Plus', apellido="Silver de 2000", imagen="images/silver.jpg", usuario=Usuario.objects.get(rut=3))
    return redirect(vehiculo, action='ins', id = '-1')
"""