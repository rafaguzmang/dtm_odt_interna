from odoo import fields,models,api
from datetime import datetime


class OrdenInterna(models.Model):
    _name = "dtm.odt.interna"
    _description = "Modulo para generar ordenes de trabajo internas"
    _rec_name = "ot_number"

        #---------------------Basicos----------------------
    def action_autoNum(self): # Genera número consecutivo de NPI
        # get_terminado = self.env['dtm.facturado.npi'].search([],order='ot_number desc',limit=1)
        get_npi = self.env['dtm.odt'].search([("tipe_order","=","ODT-I")],order='ot_number desc', limit=1)
        get_self = self.env['dtm.odt.interna'].search([],order='ot_number desc', limit=1)
        return get_npi.ot_number + 1 if get_npi.ot_number > get_self.id else get_self.id + 1

    ot_number = fields.Integer(string="NO.",default=action_autoNum,readonly=True)
    tipe_order = fields.Char(string="TIPO",readonly=True, default='ODT-I')
    name_client = fields.Char(string="CLIENTE",default="DTM",readonly=True)
    product_name = fields.Char(string="NOMBRE DEL PRODUCTO")
    date_in = fields.Date(string="CREACIÒN", default= datetime.today(),readonly=True)

    date_rel = fields.Date(string="FECHA DE ENTREGA", default= datetime.today())
    cuantity = fields.Integer(string="CANTIDAD")
    disenador = fields.Selection(string="DISEÑADOR", selection=[("andres","Andrés Orozco"),("luis","Luís García")])
    anexos_id = fields.Many2many("ir.attachment",string="Archivos")

    #---------------------Resumen de descripción------------
    descripcion = fields.Text(string="DESCRIPCIÓN")

    #------------------------Notas---------------------------
    notas = fields.Text(string="notas")

    def action_pasive(self):
        pass

    def action_generar(self):
        vals = {
            "ot_number":self.ot_number,
            "tipe_order":self.tipe_order,
            "name_client":self.name_client,
            "product_name":self.product_name,
            "date_in":self.date_in,
            "date_rel":self.date_rel,
            "cuantity":self.cuantity,
            "disenador":self.disenador,
            "description":self.descripcion,
            "orden_compra_pdf":self.anexos_id
        }
        get_ot = self.env['dtm.odt'].search([("ot_number","=",self.ot_number),("tipe_order","=","ODT-I")])
        get_ot.write(vals) if get_ot else get_ot.create(vals)
        # get_ot = self.env['dtm.odt'].search([("ot_number","=",self.ot_number),("tipe_order","=","ODT-I")])
        # print(self.anexos_id.mapped('id'))
        # get_ot.write({'anexos_id': [(5, 0, {})]})
        # get_ot.write({'anexos_id': [(6, 0, self.anexos_id.mapped('id'))]})

