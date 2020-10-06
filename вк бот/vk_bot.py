from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('c2a0e326bbada5bf04d2e515be62ca3c', config_dict)

def temo_po_name(place):

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    weather = observation.weather

    temp = weather.temperature('celsius')['temp']
    status = weather.detailed_status
    mark='ну это '
    ob={'st':status, 'temp':temp, 'mar':mark}
    return ob
