from odoo import models


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):
        # mo_auto = []
        # mo_auto_target = self.env['mrp.bom'].search(self.product_id.id)

        for record in self:
            for k in record.order_line:
                auto_bom = k.product_id.bom_ids.id
                if auto_bom:
                    k.env['mrp.production'].create(
                        {'product_id': k.product_id.id,
                         "product_uom_id": k.product_uom.id,
                         "bom_id": k.product_id.bom_ids.id,
                         "product_qty": k.product_uom_qty})
                else:
                    pass
