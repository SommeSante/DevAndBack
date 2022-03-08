# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportMedical(models.AbstractModel):
    _name = 'report.medical_report.report_medical'
    _description = 'Medical EMI report'



    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['x_emi'].browse(docids)
        print ("-------------dos",docs)
        consult = False
        disability =False
        st_7 = False
        for doc in docs:
            consult = self.env['x_bitacora_consultas'].search([('x_studio_many2one_field_8sTvT','=',doc.x_studio_many2one_field_r1IDF.id)])
            print ("---------------------------------------",consult ,  doc)
            disability = self.env['x_bitacora_incapacidad'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print("---------------------------------------", disability, doc)
            st_7 = self.env['x_st_7'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print("----------------------------stt-----------", st_7, doc)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'x_emi',
            'data': data,
            'docs': docs,
            'consult': consult,
            'disability':disability,
            'st' : st_7,

        }