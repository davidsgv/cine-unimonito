from app.model.Ciudad import Ciudad
from app.model.Base import Model


class Multiplex(Model):
    def insertMultiplex(self,nombre,direccion,localidad,ciudad_nombre):
        query = "INSERT INTO multiplex (nombre,direccion,localidad,ciudad_nombre) VALUES ('"
        query += nombre + "','" + direccion + "','" + localidad + "','" + ciudad_nombre + "');"
        self._insert(query)

        data = self._query("SELECT * FROM multiplex where nombre = '" + nombre + "';")
        return data


    def buscarMultiplex(self,multiplexNombre):
        data = self._query("SELECT * FROM multiplex where nombre = '" +  multiplexNombre + "';")
        return data


    def borrarMultiplex(self,multiplexNombre):
        self._insert("DELETE FROM multiplex Where nombre = '" + multiplexNombre + "';")


    def actualizarMultiplex(self,multiplex_nombre, nuevo_multiplex = None, nueva_direccion = None, nueva_localidad = None, nueva_ciudad = None):
        oldMultiplex = self.buscarMultiplex(multiplex_nombre)

        if(nuevo_multiplex == None):
            nuevo_multiplex = oldMultiplex["nombre"]
        if(nueva_direccion == None):
            nueva_direccion = oldMultiplex["direccion"]
        if(nueva_localidad == None):
            nueva_localidad = oldMultiplex["localidad"]
        if(nueva_ciudad == None):
            nueva_ciudad = oldMultiplex["ciudad_nombre"]

        query = "UPDATE multiplex SET nombre='{}', direccion='{}', localidad='{}', ciudad_nombre='{}'  WHERE nombre='{}';".format(nuevo_multiplex,nueva_direccion,nueva_localidad,nueva_ciudad,multiplex_nombre)

        self._insert(query)
        return self.buscarMultiplex(nuevo_multiplex)