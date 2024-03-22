# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.7 (default, Apr 15 2020, 05:09:04) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: D:\workcode\BioTime8.5\BioTime8.5.5_release\mysite\config.py
# Compiled at: 2023-03-30 16:24:57
# Size of source mod 2**32: 1133 bytes
from django.conf import settings
EMPLOYEE_LIST_FILTER = ('employee__emp_code', 'employee__first_name', 'employee__last_name')
WDMS_LIST_DISPLAY = ('company_code', 'company') if settings.ENABLE_WDMS else ()
WDMS_FILTER_APP_STATUS = () if settings.ENABLE_WDMS else ('app_status', )
WDMS_FILTER_ACC_LIST = () if settings.ENABLE_WDMS else ('lock_func', 'is_access')
# WDMS_HIDDEN = ('company_code', ) if settings.ENABLE_WDMS else ()
WDMS_LIST_FILTER_EMPLOYEE_ONE = ('employee__company', ) if settings.ENABLE_WDMS else ()
WDMS_LIST_FILTER_EMPLOYEE = ('employee__company__company_code', 'employee__company__company_name') if settings.ENABLE_WDMS else ()
WDMS_LIST_FILTER_AREA = ('area__company__company_code', 'area__company__company_name') if settings.ENABLE_WDMS else ()
WDMS_LIST_FILTER_TERMINAL = ('terminal__area__company__company_code', 'terminal__area__company__company_name') if settings.ENABLE_WDMS else ()
WDMS_LIST_FILTER = ('company__company_code', 'company__company_name') if settings.ENABLE_WDMS else ()