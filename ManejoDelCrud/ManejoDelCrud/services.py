import os
import sys
import django
from datetime import date

# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ManejoDelCrud.settings')
django.setup()

from web.models import Roles

def crear_roles():
    rol = Roles(rol="arrendatario")
    rol.save()
    print(f"El rol {rol.rol} ha sido creado con éxito")
    
    rol = Roles(rol="arrendador")
    rol.save()
    print(f"El rol {rol.rol} ha sido creado con éxito")
    
    rol = Roles(rol="vendedor")
    rol.save()
    print(f"El rol {rol.rol} ha sido creado con éxito")

#crear_roles()

def enlistar_roles():
    roles = Roles.objects.all()
    print("Los roles existentes son:")
    for rol in roles:
        print(rol.rol)
        
#enlistar_roles()

def cambiar_rol():
    rol = Roles.objects.get(rol="vendedor")
    rol.rol = "comprador"
    rol.save()
    print(f"El rol {rol.rol} ha sido modificado con éxito")
    
#cambiar_rol()

def eliminar_rol():
    rol = Roles.objects.get(rol="comprador")
    rol.delete()
    print(f"El rol {rol.rol} ha sido eliminado con éxito")
    
#eliminar_rol