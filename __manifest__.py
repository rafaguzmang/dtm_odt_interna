{
    "name":"dtm_odt_interna",
    "description":"Control de ordenes de trabajo interna",
    # 'depends': ['base', 'mail','dtm_servicios_externos'],
    "data":[
        #Security
        'security/ir.model.access.csv',
        #Views
        'views/dtm_odt_interna_view.xml',
        'views/dtm_odt_prediseno_view.xml',
        #Menú
        'views/menu_item.xml',

        ],
    'license': 'LGPL-3',
}
