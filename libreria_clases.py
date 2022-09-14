from ast import Pass


class Libreria:
    
    
    def __init__(self, Diccionario) -> None:
        self.repertorio_total = Diccionario    
    
    def agregar_libros(self, lista_libros) -> None:
        i=0
        while(i < len(lista_libros)):
            self.repertorio_total[lista_libros[i]] = lista_libros[i]
            i +=1

    
    
    def eliminar(self, libro : str) -> None:
        if(libro in self.repertorio_total):    
            del self.repertorio_total[libro]
        else:
            print("No existe este libro en la libreria")
    
    
    def Libros_disponibles(self) -> None:
        print(f"Los libros disponibles son: {self.repertorio_total.values()}")

    def rentar(self, libro : str) -> None:
        if(libro in self.repertorio_total):    
            del self.repertorio_total[libro]
        else:
            print("Este libro no esta actualmente no esta en libreria")

    
    def devolver(self, libro : str) -> None:
        self.repertorio_total[libro] = libro 

        

class Student:

    def __init__(self, name: str) -> None:
        self.name= name

    def rentar(self, objeto,  libro : str):
        objeto.rentar(libro)
        print (f"señor {self.name} rento { libro} ")
    
    def devolver(self, objeto,  libro : str):
        objeto.devolver(libro)
        print (f"señor {self.name} devolvio {libro} ")
  