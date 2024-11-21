from services.GastosComunesService import GastosComunesService

class GastosComunesController:
    @staticmethod
    def asignar_gc_controller(tipo_gc, total_gc, residente_id, fecha_pago):
        """
        Asigna un gasto común a un residente.
        """
        return GastosComunesService.asignar_gc(tipo_gc, total_gc, residente_id, fecha_pago)

    @staticmethod
    def calcular_gc_controller(gasto_id):
        """
        Calcula el gasto común de un residente específico.
        """
        return GastosComunesService.calcular_gc(gasto_id)
    
    @staticmethod
    def lista_gc_controller():
        """
        Obtiene la lista de residentes con sus gastos comunes y el estado de pago.
        """
        return GastosComunesService.lista_gc()

    @staticmethod
    def pagar_gc_controller(residente_id):
        """
        Marca un gasto común como pagado para un residente.
        """
        return GastosComunesService.pagar_gc(residente_id)
