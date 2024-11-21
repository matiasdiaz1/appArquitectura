from datetime import datetime
from app import db

class GastosComunes(db.Model):
    GastosComID = db.Column(db.Integer, primary_key=True)
    tipoGc = db.Column(db.String(100), nullable=False)  # Tipo de gasto común (e.g., mantenimiento, servicios)
    totalGc = db.Column(db.Float, nullable=False, default=0.0)  # Total del gasto común
    fecha_pago = db.Column(db.Date, nullable=False)  # Fecha límite de pago
    estado_pago = db.Column(db.String(20), default='Pendiente')  # Estado del pago (Pendiente, Pagado, Moroso)
    residente_id = db.Column(db.Integer, db.ForeignKey('residente.id'), nullable=False)  # Relación con el residente
    residente = db.relationship('Residente', backref='gastos_comunes')  # Relación inversa

    def asignar_gc(self, tipo_gc, total_gc, residente_id, fecha_pago):
        """
        Asigna el tipo y el total del gasto común al residente.
        """
        self.tipoGc = tipo_gc
        self.totalGc = total_gc
        self.fecha_pago = fecha_pago
        self.residente_id = residente_id
        db.session.add(self)
        db.session.commit()

    def calcular_gc(self):
        """
        Lógica para calcular el gasto común, si se necesita realizar algún cálculo.
        """
        # Implementar lógica de cálculo aquí (si es necesario)
        # Ejemplo de lógica de cálculo (personalizar según necesidad)
        self.totalGc += 100  # Supongamos que se suma un monto adicional
        db.session.commit()

    def lista_gc(self):
        """
        Muestra la lista de residentes y el estado del pago de sus gastos comunes.
        """
        gastos = db.session.query(GastosComunes).all()
        lista_residentes = []
        for gasto in gastos:
            estado = 'Moroso' if gasto.fecha_pago < datetime.today().date() and gasto.estado_pago != 'Pagado' else gasto.estado_pago
            lista_residentes.append({
                'residente': gasto.residente.nombre,
                'tipo_gc': gasto.tipoGc,
                'total_gc': gasto.totalGc,
                'fecha_pago': gasto.fecha_pago,
                'estado_pago': estado
            })
        return lista_residentes

    def pagar_gc(self, residente_id):
        """
        Marca el gasto común como pagado si el residente paga.
        """
        gasto = db.session.query(GastosComunes).filter_by(residente_id=residente_id).first()
        if gasto:
            gasto.estado_pago = 'Pagado'
            db.session.commit()
            return f'Gasto común de {gasto.residente.nombre} pagado exitosamente.'
        return 'No se encontró el gasto común para este residente.'

    def serialize(self):
        return {
            'GastosComID': self.GastosComID,
            'tipoGc': self.tipoGc,
            'totalGc': self.totalGc,
            'fecha_pago': self.fecha_pago,
            'estado_pago': self.estado_pago,
            'residente_id': self.residente_id
        }

class Residente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    gastos_comunes = db.relationship('GastosComunes', backref='residente', lazy=True)

