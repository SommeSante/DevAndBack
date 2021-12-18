# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta

class EmpleadosPlanta(models.Model):
    _name = 'empleados.planta'
    _description = 'Empleados Planta'

    cliente_id = fields.Many2one(comodel_name='res.partner', string='Cliente')
    nombre = fields.Char(string='Nombre')
    telefono = fields.Char(string='Telefono')
    nomina = fields.Char(string='nomina')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    edad = fields.Integer(string='Edad', compute='compute_edad')
    area_trabajo = fields.Char(string='Area Trabajo')
    jefe_inmediato = fields.Char(string='Jefe Inmediato')


    def compute_edad(self):
        for rec in self:
            age = (date.today() - rec.fecha_nacimiento) // timedelta(days=365.2425)
            rec.edad = age
