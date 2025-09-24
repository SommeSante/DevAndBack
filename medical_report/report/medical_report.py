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
        control = False
        emp = False
        cron = False
        for doc in docs:
            consult = self.env['x_bitacora_consultas'].search([('x_studio_many2one_field_8sTvT','=',doc.x_studio_many2one_field_r1IDF.id)])
            disability = self.env['x_bitacora_incapacidad'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print ("___________disability_____", disability, doc)
            st_7 = self.env['x_st_7'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print("___________st-7_____", st_7, doc)
            control = self.env['x_control_prenatal'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print("___________control____", control, doc)
            emp = self.env['x_emp'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print("___________emp____", emp, doc)
            cron = self.env['x_cronicos'].search(
                [('x_studio_nombre', '=', doc.x_studio_many2one_field_r1IDF.id)])
            print("___________cron____", cron, doc)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'x_emi',
            'data': data,
            'docs': docs,
            'consult': consult,
            'disability':disability,
            'control':control,
            'emp': emp,
            'st' : st_7,
            'cron':cron,
        }