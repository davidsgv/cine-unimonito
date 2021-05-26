from app.model.Base import Model


class Ciudad(Model):
    #buscar todas las ciudades
    def listaCiudades(self):
        data = self._query("SELECT * FROM ciudad;")
        return data

    #insertar ciudad
    def insertCiudad(self,ciudadNombre):
        self._insert("INSERT INTO ciudad (nombre) VALUES ('" + ciudadNombre + "');" )
        data = self._query("SELECT nombre FROM ciudad where nombre = '" +  ciudadNombre + "';")
        return data

    #Buscar ciudad
    def buscarCiudad(self,ciudadNombre):
        data = self._query("SELECT nombre FROM ciudad where nombre = '" +  ciudadNombre + "';")
        return data
    
    #Borrar ciudad
    def borrarCiudad(self,ciudadNombre):
        self._insert("DELETE FROM ciudad WHERE nombre = '" + ciudadNombre + "';" )

    #Actualizar ciuadad
    def actualizarCiudad(self, ciudadNombre, nuevoNombre):
        self._insert("UPDATE ciudad SET nombre='" + nuevoNombre + "' WHERE nombre = '" + ciudadNombre + "';" )
        return self.buscarCiudad(nuevoNombre)



