from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import Chapter


@plugin_pool.register_plugin
class TTIPBarometerListPlugin(CMSPluginBase):
    """
    Plugin for rendering a list of chapters
    """

    module = _("TTIP Barometer")
    name = _("Chapter List")  # name of the plugin in the interface
    render_template = "correctiv_ttip_barometer/plugin/list.html"

    def render(self, context, instance, placeholder):
        context = super(TTIPBarometerListPlugin, self)\
            .render(context, instance, placeholder)
        context['object_list'] = Chapter.objects.all()
        return context


@plugin_pool.register_plugin
class TTIPBarometerSmallListPlugin(CMSPluginBase):
    """
    Plugin for rendering 5 chapters
    """

    module = _("TTIP Barometer")
    name = _("Chapter List (5 items)")  # name of the plugin in the interface
    render_template = "correctiv_ttip_barometer/plugin/list.html"

    def render(self, context, instance, placeholder):
        context = super(TTIPBarometerSmallListPlugin, self)\
            .render(context, instance, placeholder)
        context['object_list'] = Chapter.objects.all()[:5]
        return context
