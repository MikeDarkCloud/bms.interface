
from model.Config import *

def get_url(EndPoint):
    host = Config().url()
    endpoint = EndPoint
    url = ''.join([host, endpoint])
    return url

