from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# Register your models here.
#@admin.register(Area,Tariffplan,Customer,Customerplan,CustomerUserid,Operator,BillLoad,
#	BbnlPaymentLoad,AirwirePaymentLoad,CashCollectionLoad)
class ViewAdmin(ImportExportModelAdmin):
	pass