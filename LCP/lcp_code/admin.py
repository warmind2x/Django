from django.contrib import admin

from lcp_code.models import Lcp_code, Buyer, LcpType, StakeHolder

# Register your models here.
admin.site.register(Lcp_code)
admin.site.register(Buyer)
admin.site.register(LcpType)
admin.site.register(StakeHolder)
