from app.model.Base import Model


class PuntoAgil(Model):
    def insertarPuntoagil(self,nombreUsuario,ubicacion,ciudad_nombre):
        query = "INSERT INTO Puntoagil (nombreUsuario,ubicacion,ciudad_nombre) VALUES ('"
        query += nombreUsuario + "','" + ubicacion + "','" + ciudad_nombre + "');"
        self._insert(query)

        data = self._query("SELECT * FROM Puntoagil where nombreUsuario = '" + nombreUsuario + "';")

        return data

    def buscarPuntoagil(self,PuntoagilnombreUsuario):
        data = self._query("SELECT * FROM Puntoagil where nombreUsuario = '" +  PuntoagilnombreUsuario + "';")

        # for x in userInfo:
        #     returningData = x[0:4]

        return data

    def borrarPuntoagil(self,PuntoagilnombreUsuario):
        self._insert("DELETE FROM Puntoagil Where nombreUsuario = '" + PuntoagilnombreUsuario + "';")

    def actualizarPuntoagil(self,idPunto, nueva_ubicacion, nueva_ciudad):
        self._insert("UPDATE Puntoagil SET ubicacion='" + nueva_ubicacion +  "', ciudad_nombre='" + nueva_ciudad + "' WHERE nombreUsuario='"+ idPunto +"';")
        return self.buscarPuntoagil(idPunto)