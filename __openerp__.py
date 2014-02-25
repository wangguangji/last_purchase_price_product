# -*- encoding: utf-8 -*-
{
    "name" : "last_purchase_price_product",
    "description" : """
            1,添加针对商品添加最后一次采购价格
            2,要对不同的供应商指定最后一次采购价格
            3,选择的时候就使用产品最后采购价格为主
        """,
    "version" : "1.0",
    "author" : "http://www.freshfresh.com",
    "depends" : ["product","stock","purchase"],
    "category" : "Product",
    "sequence": 5,
    "data" : [
        'product/product_view.xml'
    ],
    "website": 'http://www.freshfresh.com',
    'installable': True,
    'active': False,
}
