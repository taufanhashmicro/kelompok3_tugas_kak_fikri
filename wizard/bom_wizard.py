from odoo import api, fields, models


class BomWizard(models.TransientModel):
    _name = 'bom.wizard'
    _description = 'Wizard Information BoM'

    # sale_order_compute = fields.Many2one("sale.order", string="Sale Order",
    #     compute='_compute_field' )

    # @api.depends('depends')
    # def _compute_field(self):
    #     return self.env['sale.order'].search([],limit=1, order='id desc')


    # # bom_ids = fields.Many2one(comodel_name="mrp.bom",string='MRP BoM')
    # produk_so = sale_order_compute.order_line

    # for record in produk_so:
    #         if record.product_id.bom_ids:
    #             continue
    #         else :
    #             print('Mohon Maaf Produk Ini Tidak Mempunyai BoM')