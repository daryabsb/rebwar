import re

try:
    from ipware import get_client_ip
    # from ipware.utils import is_public_ip
except ImportError:
    public_addr_pattern = re.compile('\n        ^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\n        (?<!127)(?<!^10)(?<!^0)\n            #1) `127.*` is loop address\n            #2) `10.*` is private address\n            #3) `0.*` is illegal\n        \\.# first digit\n        ([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!192\\.168)(?<!172\\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))\n        \\.# second digit # in python `re` negative lookbehind need to be fixed-width\n        ([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\n        \\.# third digit\n        ([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\n        (?<!\\.255$)$ # filter broadcast IPs\n        # last digit\n        ', re.M | re.VERBOSE)

    def is_public_ip(ip):
        if public_addr_pattern.search(ip) is not None:
            return True
        return False
    
    def _get_client_ip(request):
        """
        [simple but not robust]
        Get the incoming request's originating IP, looks first for X_FORWARDED_FOR header, which is provided by some
        PaaS platforms, since the Django REMOTE_ADDR is affected by internal routing.  Fallback to the REMOTE_ADDR if
        the header is not present
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if not x_forwarded_for:
            ip = request.META.get('REMOTE_ADDR')
        else:
            ip = x_forwarded_for.split(',')[0].strip()
        return (
         ip, is_public_ip(ip))


    get_client_ip = _get_client_ip

BUILD_IN_PERMISSION = {
    'GeneralActionNew':'add',
    'GeneralActionDelete':'delete'
    }


def get_error_message(e, **kwargs):
    correlated_field = kwargs.get('field', None)
    original_msg = str(e) or '{}: {}'.format(type(e), e.args)
    if correlated_field is not None:
        return correlated_field + str(original_msg)
    return original_msg