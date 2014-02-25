# -*- encoding: utf-8 -*-
from openerp.osv import osv

class partial_picking(osv.osv_memory):

    _inherit = 'stock.partial.picking'

    def do_partial(self, cr, uid, ids, context=None):
        if context is None:
            context = {} 
        res = super(partial_picking, self).do_partial(cr, uid, ids, context=context)
        pick_obj = self.pool.get('stock.picking')
        purchase_obj = self.pool.get('purchase.order')
        currency_obj = self.pool.get('res.currency')
        plpp_obj = self.pool.get('product.last.purchase.price')
        picking_ids = context.get('active_ids', False)
        partial = self.browse(cr, uid, ids[0], context=context)
        pick_list = pick_obj.browse(cr, uid, picking_ids, context=context)
        for pick in pick_list:
            if pick.type == 'in' and pick.origin:
                order_id = pick.purchase_id and pick.purchase_id.id or False
                if order_id:
                    order = purchase_obj.browse(cr, uid, order_id)
                    for move in partial.move_ids:
                        if move.product_id.is_last_purchase_price:
                            product_cost = 0.0
                            for line in order.order_line:
                                if line.product_id.id == move.product_id.id:
                                    product_cost = currency_obj.compute(cr, uid, order.currency_id.id, order.company_id.currency_id.id, line.price_unit)
                                    plpp_obj.update_or_create_using_purchse_price(cr,uid,pick.purchase_id.partner_id.id,move.product_id.id,product_cost)
                            self.pool.get('product.product').write(cr, uid, [move.product_id.id], {'is_last_price': product_cost})
        return res

partial_picking()
