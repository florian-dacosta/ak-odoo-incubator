# coding: utf-8
# © 2017 David BEAL @ Akretion <david.beal@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Stock Inventory Simple Valuation",
    'summary': "... ",
    'description': """
        Display cost information from different sources in inventory line""",
    'author': "Akretion",
    'website': "http://www.akretion.com",
    'category': 'Stock',
    'version': '8.0.1.0.1',
    'depends': [
        'stock',
        'report_xlsx',
    ],
    'data': [
        'views/inventory_view.xml',
        'report/report_view.xml',
    ],
}
