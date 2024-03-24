

APP_NAME = 'accounts'


def get_menu(url_func):
    from django.conf import settings
    menu = {'menu_groups': [{
        'verbose_name': 'accounts',
        'icon': 'fa-user',
        'permissions': [],
        'menus': [
            {
                'model_name': 'user',
                'verbose_name': 'user',
                'visible': settings.ENABLE_WDMS,
                'url': url_func('%s_%s_init' % (APP_NAME, 'user'))
            },
            {
                'model_name': 'doctorprofile',
                'verbose_name': 'doctorprofile',
                'visible': settings.ENABLE_WDMS,
                'url': url_func('%s_%s_init' % (APP_NAME, 'doctorprofile'))
            },
            {
                'model_name': 'patient',
                'verbose_name': 'patient',
                'visible': settings.ENABLE_WDMS,
                'url': url_func('%s_%s_init' % (APP_NAME, 'patient'))
            },
        ],
    },

    ]}
