from app.model.Base import Model


class Empleado(Model):
    def insertarEmpleado(self,codigo,tipoDocumento,numeroDocumento,nombres,apellidos,telefono,fechaInicioContrato,salario,estado,puntoAgil_nombreUsuario,multiplex_nombre):
        self._insert("INSERT INTO Empleado (codigo,tipoDocumento,numeroDocumento,nombres,apellidos,telefono,fechaInicioContrato,salario,estado,puntoAgil_nombreUsuario,multiplex_nombre) VALUES ('" + codigo + "','" + tipoDocumento + "','" + numeroDocumento + "','" + nombres + "','" + apellidos + "','" + telefono + "','" + fechaInicioContrato + "','" + salario + "','" + estado + "','" + puntoAgil_nombreUsuario + "','" + multiplex_nombre + "');" )
        data = self.buscarEmpleado(codigo)
        return data

    def buscarEmpleado(self,codigo):
        data = self._query("SELECT * FROM Empleado where codigo = '" +  codigo + "';")

        # for x in userInfo:
        #     returningData = x[0:4]
        return data

    def borrarEmpleado(self,codigo):
        self._insert("DELETE FROM empleado Where codigo = '" + codigo + "';")

    def actualizarEmpleado(self, codigo, tipoDocumento, numeroDocumento, nombres, apellidos,
        telefono,fechaInicioContrato,salario,estado,puntoAgil_nombreUsuario,multiplex_nombre):
        
        self._insert("UPDATE empleado SET codigo='" + codigo + "', tipoDocumento='" + tipoDocumento + "', numeroDocumento='" + numeroDocumento + "', nombres='" + nombres + "', apellidos='" + apellidos + "', telefono='" + telefono + "', fechaInicioContrato='" + fechaInicioContrato + "', salario='" + salario + "', estado='" + estado + "', puntoAgil_nombreUsuario='" + puntoAgil_nombreUsuario + "', multiplex_nombre='" + multiplex_nombre + "'  WHERE codigo='"+ codigo +"';")
        return self.buscarEmpleado(codigo)