from import_export import resources
from .models import BillLoad,AirwirePaymentLoad,BbnlPaymentLoad,CashCollectionLoad

class LoadBills(resources.ModelResource):
	class Meta:
		model = BillLoad
		
class LoadAirwirePayments(resources.ModelResource):
	class Meta:
		model = AirwirePaymentLoad

class LoadBbnlPayments(resources.ModelResource):
	class Meta:
		model = BbnlPaymentLoad

class LoadCashCollection(resources.ModelResource):
	class Meta:
		model = CashCollectionLoad
				