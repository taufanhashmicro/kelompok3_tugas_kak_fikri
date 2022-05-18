from odoo import api, fields, models


class BomWizard(models.TransientModel):
    _name = 'bom.wizard'
    _description = 'Wizard Information BoM'

    bom_ids = fields.Char(string='MRP BoM')
