{
    'name' : 'Product Movement Report',
    'version' : '16.0.0.0',
    'author': 'Atsevah Anthony',
    'maintainer': 'Atsevah Anthony',
    'description': 'Shows product movement report by location'
    'summary': 'Product movement report',
    'category': 'Warehouse',
    'depends' : ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/moves_wizard.xml',
        'report/moves_report.xml',
        'report/moves_view.xml',
        ],
    'images': ['static/description/banner_image.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}