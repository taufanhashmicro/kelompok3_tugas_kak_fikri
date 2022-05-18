from odoo import models


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):
        for record in self.order_line:
            if record.product_id.bom_ids:
                for bom_id in record.product_id.bom_ids:
                    bom_data = record.env['mrp.bom'].search([('id', '=', bom_id.id)]).read()
                    if bom_data:
                        record.env['mrp.production'].create({
                            'product_id': record.product_id.id, 
                            'product_uom_id': record.product_id.bom_ids.product_uom_id.id, 
                            'bom_id': bom_id.id, 
                            'product_qty': record.product_uom_qty})
            else:
                return {
                        'type': 'ir.actions.act_window',
                        'name': 'Wizard BoM',
                        'res_model': 'bom.wizard',
                        'view_mode': 'form',
                        'view_type': 'form',
                        'target': 'new',
                        }
               

