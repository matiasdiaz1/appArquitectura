from models.GastosComunesModel import db, GastosComunes
from models.ResidenteModel import Residente
from datetime import datetime

class GastosComunesService:
    @staticmethod
    def asignar_gc(tipo_gc, total_gc, residente_id, fecha_pago):
        """
        Asigna un gasto común a un residente.
        """
        # Verificar si el residente existe
        residente = Residente.query.get(residente_id)
        if not residente:
            return "Residente no encontrado"
        
        # Crear una nueva instancia de GastosComunes
        nuevo_gasto = GastosComunes(tipoGc=tipo_gc, totalGc=total_gc, residente_id=residente_id, fecha_pago=fecha_pago)
        db.session.add(nuevo_gasto)
        db.session.commit()
        return "Gasto común asignado exitosamente"
    
    @staticmethod
    def calcular_gc(gasto_id):
        """
        Calcula el gasto común (puede agregar lógica adicional según sea necesario).
        """
        gasto = GastosComunes.query.get(gasto_id)
        if not gasto:
            return "Gasto común no encontrado"

        # Lógica para actualizar el total del gasto (si es necesario)
        gasto.totalGc += 100  # Ejemplo de incremento
        db.session.commit()
        return "Gasto común calculado y actualizado"
    
    @staticmethod
    def lista_gc():
        """
        Obtiene la lista de todos los residentes con sus gastos comunes y estado de pago.
        """
        gastos = GastosComunes.query.all()
        lista_residentes_gastos = []

        for gasto in gastos:
            residente = Residente.query.get(gasto.residente_id)
            if residente:
                estado_pago = "Pagado" if gasto.pago else "Moroso" if gasto.fecha_pago < datetime.today().date() else "Pendiente"
                lista_residentes_gastos.append({
                    'residente': f"{residente.nombre} {residente.apellido_paterno}",
                    'tipoGc': gasto.tipoGc,
                    'totalGc': gasto.totalGc,
                    'estadoPago': estado_pago,
                    'fechaPago': gasto.fecha_pago
                })
        return lista_residentes_gastos
    
    @staticmethod
    def pagar_gc(residente_id):
        """
        Marca el gasto común de un residente como pagado.
        """
        gastos = GastosComunes.query.filter_by(residente_id=residente_id).all()
        if not gastos:
            return "No se encontraron gastos comunes para este residente"

        for gasto in gastos:
            gasto.pago = True  # Marca el pago como realizado
            db.session.commit()
        
        return "Gastos comunes marcados como pagados"
