from app.model.Base import Model


class Ciudad(Model):
    def insertCiudad(self,ciudadNombre):
        self._insert("INSERT INTO ciudad (nombre) VALUES ('" + ciudadNombre + "');" )

        data = self._query("SELECT nombre FROM ciudad where nombre = '" +  ciudadNombre + "';")

        return data

    def buscarCiudad(self,ciudadNombre):
        data = self._query("SELECT nombre FROM ciudad where nombre = '" +  ciudadNombre + "';")

        # for x in userInfo:
        #     returningData = x[0:4]

        return data


