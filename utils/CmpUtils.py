
from xml.sax.saxutils import escape
from suds.client import Client
from suds.sudsobject import asdict


class CmpUtils(object):

    @staticmethod
    def _get_url(url, host, port):
        return url.format(host=host, port=port)

    @staticmethod
    def _load_client_using_basic_authentication(username, password, url, timeout=None):
        if timeout:
            return Client(url, username=username, password=password, timeout=int(timeout))

        return Client(url, username=username, password=password)

    @staticmethod
    def _escape_xml_string(xml_string):
        data = xml_string
        data = escape(data)
        data = data.replace('&apos', '&amp;apos')
        data = data.replace('&quot', '&amp;quot')
        return data

    @staticmethod
    def _recursive_asdict(d):
        """Convert Suds object into serializable format."""
        out = {}
        for k, v in asdict(d).iteritems():
            if hasattr(v, '__keylist__'):
                out[k] = CmpUtils._recursive_asdict(v)
            elif isinstance(v, list):
                out[k] = []
                for item in v:
                    if hasattr(item, '__keylist__'):
                        out[k].append(CmpUtils._recursive_asdict(item))
                    else:
                        out[k].append(item)
            else:
                out[k] = v
        return out






