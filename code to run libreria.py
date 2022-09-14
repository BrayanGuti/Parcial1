from libreria_clases import Libreria, Student

repertorio = {"La Biblia" : "La Biblia", "100 años de soledad" : "100 años de soledad"}
nueva_libreria = ["carne roja", "Big foot", "las flipantes aventuras del amongus"]
libro_eliminar = "Big foot"


libreria1 = Libreria(Diccionario= repertorio)
""""Creo una libreria que tendra como repertorio las claves del diccionario repertorio"""


libreria1.Libros_disponibles()
""""Muestro el repertorio inicial que tiene el bibliotecario"""


libreria1.agregar_libros(lista_libros= nueva_libreria)
""""Adiciono una lista de libros que se encuentran en la variable nueva_libreria"""


libreria1.Libros_disponibles()
""""Muestro el nuevo repertorio despues de adicionar la lista de libros nueva almacenada en la variable nueva_libreria"""


libreria1.eliminar(libro= libro_eliminar)


libreria1.Libros_disponibles()
""""Muestro el nuevo repertorio despues de eliminar el libro de la variable (libro_eliminar)"""


estudiante = Student(name= "Miguel")
""""Creo un objeto estudiante llamado Miguel que va a tener acceso a los metodos rentrar y devolver"""


estudiante.rentar(objeto= libreria1, libro="las flipantes aventuras del amongus")
""""El obejeto miguel de clase estudiante usa el metodo "rentar" para rentar el libro "las flipantes aventuras del amongus" """
""""Ademas atraves de un print notifico que el señor (nombre del objeto estudiante) a rentado (nombre del libro rentado) """


libreria1.Libros_disponibles()
""""Muestro como quedaria el repertorio de la libreria despues que el estudiante miguel rente el libro"""


estudiante.devolver(objeto= libreria1, libro= "las flipantes aventuras del amongus")
""""Atraves del metodo devolver el objeto miguel de la clase estudiante reingresa el libro rentado"""
""""Ademas atraves de un print notifico que el señor (nombre del objeto estudiante) a devolvido (nombre del libro devolvido) """


libreria1.Libros_disponibles()
""""Muestro como quedaria el repertorio devolviendo el libro prestado"""