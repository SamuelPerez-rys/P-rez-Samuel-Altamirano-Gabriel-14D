
import time
libro=[];

def menu():
  while True:
    print("_---Bienvenido a libros Duoc Uc---_");
    print("Menu de opciones:\n");

    print("1.-Agregar un libro");
    print("2.-Ver todos los libros");
    print("3.-Modificar un libro");
    print("4.-Eliminar Libro");
    print("5.-Guardar colección en un archivo");
    print("6.-Salir del programa");

    Menudecision=int(input("Ingrese una opcion: "))
    if Menudecision==1:
        print("Usted ingreso a la opcion 1");
    
    elif Menudecision==2:
        print("Usted ingreso la opcion 2");
    
    elif Menudecision==3:
        print("Usted ingreso la opcion 3");
    
    elif Menudecision==4:
        print("Usted ingreso la opcion 4");
    
    elif Menudecision==5:
        print("Usted ingreso la opcion 5");

    elif Menudecision==6:
        print("Usted ingreso la opcion 6.")
        print("Saliendo del programa. por favor espere...")
        time.sleep(2)
        break;

def agregar_libro(coleccion):
    while True:
        try:
            nuevolibro=input("Ingrese el nombre del libro que desea agregar");
        except ValueError:
            ("Ingrese un nombre o caracter valido");
        else:
            libro.append(nuevolibro);
        print("Se agrego el nuevo libro con exito.")
        return;


def ver_libro():
    while True:
        libro=
        break;

def modificar_libro():
    modificar=input("Escriba el nombre del libro que desea modificar (Nombre literal)")


def elimininar_libro():
    elimininar=input("Ingrese el nombre del libro que desea eliminar");
