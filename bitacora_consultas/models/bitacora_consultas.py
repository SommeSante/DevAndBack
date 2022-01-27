# -*- coding: utf-8 -*-

from odoo import models, api
import datetime
import logging

_logger = logging.getLogger(__name__)


class BitacoraConsultas(models.Model):
    _inherit = "x_bitacora_consultas"
    
    def write(self, vals):
        _logger.info('Executing method -----------------dd--------------------- %s' % vals)
        return super(BitacoraConsultas, self).write(vals)
        
    
    
    @api.onchange('x_studio_fecha_y_hora_de_salida')
    def onchange_x_studio_fecha_y_hora_de_salida(self):
        _logger.info('Executing method -------------------------------------- %s' % self.x_studio_fecha_y_hora_de_salida)
        if self.x_studio_fecha_y_hora_de_salida:
            time_diff = self.x_studio_fecha_y_hora_de_salida - self.x_studio_fecha_y_hora_de_ingreso
            self.x_studio_tiempo_total_en_consulta = float(time_diff.days) * 24 + (float(time_diff.seconds) / 3600)


class BitacoraIncapacidad(models.Model):
    _inherit = "x_bitacora_incapacidad"
    
    @api.onchange('x_studio_das_otorgados')
    def onchange_x_studio_das_otorgados(self):
        if self.x_studio_inicia:
            self.x_studio_termina = self.x_studio_inicia + datetime.datetime.timedelta(days=self.x_studio_das_otorgados - 1)
            self.x_studio_se_reincorpora = self.x_studio_inicia + datetime.datetime.timedelta(days=self.x_studio_das_otorgados)
            