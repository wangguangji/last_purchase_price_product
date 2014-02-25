# -*- encoding: utf-8 -*-
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp

#----------------------------------------------------------
# Products
#----------------------------------------------------------
class product_template(osv.osv):
    _inherit = "product.template"

    _columns = {
        'is_last_purchase_price' :fields.boolean(u'是否取最后采购价格'),
        'is_last_price':fields.float('最后采购价格', digits_compute=dp.get_precision('Product Price'), groups="base.group_user"),
        'purchase_price_ids':fields.one2many('product.last.purchase.price', 'product_id', '最后采购价格', readonly=True, ),
    }

    _defaults = {
        'is_last_purchase_price':True,
    }


product_template()


class product_last_purchase_price(osv.osv):
    
    _name = "product.last.purchase.price"
    
    _columns = {
        'product_id': fields.many2one('product.template', u'产品', required=True, ondelete='cascade', select=True, readonly=True),        
        'price':fields.float(u'价格',digits_compute=dp.get_precision('Product Price'),required=True),
        'partner_id': fields.many2one('res.partner', u'供应商', required=True),
        'is_last':fields.boolean(u'最后的价格')
    }
    
    
    def update_or_create_using_purchse_price(self, cr, uid, partner_id,product_id,price, context=None):
        ids = self.search(cr,uid,[('product_id','=',product_id),('partner_id','=',partner_id)])
        if ids:
            return self.write(cr, uid, ids, {'price': price})
        else:
            return self.create(cr, uid, {'product_id':product_id,'price':price,'partner_id':partner_id}, context)
