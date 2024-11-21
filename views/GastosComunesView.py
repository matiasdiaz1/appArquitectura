from flask import Blueprint, request, jsonify
from controllers.GastosComunesController import GastosComunesController

gastos_comunes_blueprint = Blueprint('gastos_comunes_blueprint', __name__)

# Definir la clase GastosComunesView
class GastosComunesView:

    @staticmethod
    @gastos_comunes_blueprint.route('/gastos-comunes/crear', methods=['POST'])
    def asignar_gc():
        # Obtener los datos del cuerpo de la solicitud y asignar un gasto común
        data = request.get_json()
        tipo_gc = data.get('tipoGc')
        total_gc = data.get('totalGc')
        residente_id = data.get('residenteId')
        fecha_pago = data.get('fechaPago')
        
        mensaje = GastosComunesController.asignar_gc(tipo_gc, total_gc, residente_id, fecha_pago)
        if mensaje == "Gasto común asignado exitosamente":
            return jsonify({"mensaje": mensaje}), 201
        return jsonify({"mensaje": mensaje}), 400

    @staticmethod
    @gastos_comunes_blueprint.route('/gastos-comunes/calcular/<int:gasto_id>', methods=['PATCH'])
    def calcular_gc(gasto_id):
        # Llama al controlador para calcular el gasto común
        mensaje = GastosComunesController.calcular_gc(gasto_id)
        
        if "actualizado" in mensaje:
            return jsonify({"mensaje": mensaje}), 200
        return jsonify({"mensaje": mensaje}), 400
    
    @staticmethod
    @gastos_comunes_blueprint.route('/gastos-comunes', methods=['GET'])
    def lista_gc():
        # Llama al controlador para obtener la lista de los gastos comunes
        lista = GastosComunesController.lista_gc()
        if lista:
            return jsonify({"gastos_comunes": lista}), 200
        return jsonify({"mensaje": "No hay gastos comunes asignados"}), 404
    
    @staticmethod
    @gastos_comunes_blueprint.route('/gastos-comunes/pagar/<int:residente_id>', methods=['PATCH'])
    def pagar_gc(residente_id):
        # Llama al controlador para pagar los gastos comunes
        mensaje = GastosComunesController.pagar_gc(residente_id)
        
        if "marcados como pagados" in mensaje:
            return jsonify({"mensaje": mensaje}), 200
        return jsonify({"mensaje": mensaje}), 400
