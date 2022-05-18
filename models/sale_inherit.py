from odoo import models


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):
        for record in self.order_line:
            for k in record.product_id.bom_ids:
                auto_bom = record.env['mrp.bom'].search(
                    [('id', '=', k.id)]).read()
                if auto_bom == True:
                    record.env['mrp.production'].create(
                        {'product_id': record.product_id.id,
                         "product_uom_id": record.product_uom.id,
                         "bom_id": k.id,
                         "product_qty": record.product_uom_qty})   
                
            return {
                    'type': 'ir.actions.act_window',
                    'name': 'Wizard BoM',
                    'res_model': 'bom.wizard',
                    'view_mode': 'form',
                    'view_type': 'form',
                    'target': 'new',
                   }
               

