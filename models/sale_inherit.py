from odoo import models


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):
        mo_auto = []
        mo_auto_target = self.env['sale.order'].browse(self.id)
        # print("a")
        for m in mo_auto_target:
            mo_auto.append([{
                'product_id': m.order_line.product_id.id,
                'product_uom_id': m.order_line.product_id.bom_ids.product_uom_id.id,
                'bom_id': m.order_line.product_id.bom_ids.id,
                'harga_bom': m.order_line.product_id.bom_ids.harga_bom,
                'product_qty': m.order_line.product_uom_qty,
            }])

        auto_product_id = mo_auto[0][0]["product_id"]
        auto_product_uom_id = mo_auto[0][0]["product_uom_id"]
        auto_bom_id = mo_auto[0][0]["bom_id"]
        auto_harga_bom = mo_auto[0][0]["harga_bom"]
        auto_product_qty = mo_auto[0][0]["product_qty"]

        if auto_harga_bom:
            self.env['mrp.production'].create(
                {'product_id': auto_product_id, "product_uom_id": auto_product_uom_id, "bom_id": auto_bom_id, "product_qty": auto_product_qty})
        else:
            pass
