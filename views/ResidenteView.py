from flask import Blueprint, request, jsonify
from controllers.ResidenteController import ResidenteController

residente_blueprint = Blueprint('residente_blueprint', __name__)

class ResidentesView:

    @staticmethod
    @residente_blueprint.route('/residentes/create', methods=['POST'])
    def crear_residente():
        # Recibe la solicitud para crear un residente y delega al servicio
        data = request.get_json()
        nombre = data.get('nombre')
        apellido_paterno = data.get('apellido_paterno')
        apellido_materno = data.get('apellido_materno')
        num_telefono = data.get('num_telefono')
        correo = data.get('correo')
        
        new_residente = ResidenteController.create_residente_controller(
            nombre, apellido_paterno, apellido_materno, num_telefono, correo
        )
        
        return jsonify({
            "mensaje": "Residente creado", 
            "residente": {
                "id_residente": new_residente.id_residente, 
                "nombre": new_residente.nombre,
                "apellido_paterno": new_residente.apellido_paterno,
                "apellido_materno": new_residente.apellido_materno,
                "num_telefono": new_residente.num_telefono,
                "correo": new_residente.correo
            }
        }), 201

    @staticmethod
    @residente_blueprint.route('/residentes', methods=['GET'])
    def lista_residentes():
        # Llama al controlador para obtener todos los residentes
        residentes = ResidenteController.get_residentes_controller()
        residentes_list = [{
            "id_residente": residente.id_residente,
            "nombre": residente.nombre,
            "apellido_paterno": residente.apellido_paterno,
            "apellido_materno": residente.apellido_materno,
            "num_telefono": residente.num_telefono,
            "correo": residente.correo
        } for residente in residentes]
        
        return jsonify({"residentes": residentes_list}), 200

    @staticmethod
    @residente_blueprint.route('/residentes/<int:id_residente>', methods=['GET'])
    def get_residente_by_id(id_residente):
        # Llama al controlador para obtener un residente por su ID
        residente = ResidenteController.get_residente_by_id_controller(id_residente)
        if residente is None:
            return jsonify({"mensaje
