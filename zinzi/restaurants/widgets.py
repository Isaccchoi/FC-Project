from django.conf import settings
from django.forms import widgets


class GoogleMapsAddressWidget(widgets.TextInput):
    """a widget that will place a google map right after the #id_address field"""
    template_name = "django_google_maps/widgets/map_widget.html"

    class Media:
        css = {
            'all': (
                'https://s3.ap-northeast-2.amazonaws.com/zinzi/static/django_google_maps/css/google-maps-admin.css',
            )
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js',
            'https://maps.google.com/maps/api/js?key={}'.format(
                settings.GOOGLE_MAPS_API_KEY),
            'https://s3.ap-northeast-2.amazonaws.com/zinzi/static/django_google_maps/js/google-maps-admin.js',)
