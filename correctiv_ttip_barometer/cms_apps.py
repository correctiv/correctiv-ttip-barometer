from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class TTIPBarometerApp(CMSApp):
    name = _('TTIP Barometer')
    app_name = 'ttip_barometer'
    urls = ['correctiv_ttip_barometer.urls']


apphook_pool.register(TTIPBarometerApp)
