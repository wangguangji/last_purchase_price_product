# -*- encoding: utf-8 -*-
from openerp.osv import  osv


class purchase_order_line(osv.osv):
    
    _inherit = 'purchase.order.line'
    
    def onchange_product_id(self, cr, uid, ids, pricelist_id, product_id, qty, uom_id,
        partner_id, date_order=False, fiscal_position_id=False, date_planned=False,
        name=False, price_unit=False, context=None):
        res = super(purchase_order_line, self).onchange_product_id(cr, uid, ids, pricelist_id, product_id, qty, uom_id,
                                                                    partner_id, date_order=False, fiscal_position_id=False, date_planned=False,
                                                                    name=False, price_unit=False, context=None)
        product_product = self.pool.get('product.product')
        context_partner = context.copy()
        if product_id:
            product = product_product.browse(cr, uid, product_id, context=context_partner)
            if product.is_last_purchase_price:
                res['value'].update({'price_unit': product.is_last_price})
        return   res  