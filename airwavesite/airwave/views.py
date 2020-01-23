from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db import connection
#from django.urls import reverse
#from django.db import connection
from django.db.models import Q
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import EmployeeForm, TariffplanForm, AirwaveconfigForm, \
    AreaForm, OperatorForm, CustomerForm, CustomerplanForm, CustomerUseridForm, \
    PaymentsForm, AirwaveCollectionForm
from .models import Employee, Tariffplan, Airwaveconfig, Area, Operator, \
    Customer, Customerplan, CustomerUserid, Payments, AirwaveCollection

from tablib import Dataset
from .resources import LoadBills,LoadAirwirePayments,LoadBbnlPayments,LoadCashCollection
# Create your views here.

###############################Airwaveconfig######################################
@method_decorator(login_required, name='dispatch')
class AirwaveconfigCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Airwaveconfig
    form_class = AirwaveconfigForm
    success_url = reverse_lazy('airwave:airwaveconfig_list')
    success_message = "Configuration %(key_code)s addedd successfully"
    permission_required = ('airwave.add_airwaveconfig',)


@method_decorator(login_required, name='dispatch')
class AirwaveconfigUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Airwaveconfig
    form_class = AirwaveconfigForm
    template_name = 'airwave/airwaveconfig_form.html'
    success_url = reverse_lazy('airwave:airwaveconfig_list')
    success_message = "Configuration %(key_code)s changed successfully"
    permission_required = ('airwave.change_airwaveconfig',)


@method_decorator(login_required, name='dispatch')
class AirwaveconfigDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Airwaveconfig
    success_url = reverse_lazy('airwave:airwaveconfig_list')
    success_message = "Configuration %(key_code)s deleted successfully"
    permission_required = ('airwave.delete_airwaveconfig',)


@method_decorator(login_required, name='dispatch')
class AirwaveconfigListView(PermissionRequiredMixin,ListView):
    model = Airwaveconfig
    context_object_name = 'airwaveconfig'
    permission_required = ('airwave.view_airwaveconfig',)
###############################Airwaveconfig######################################


###############################Area######################################
@method_decorator(login_required, name='dispatch')
class AreaCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Area
    form_class = AreaForm
    success_url = reverse_lazy('airwave:area_list')
    success_message = "Area %(name)s addedd successfully"
    permission_required = ('airwave.add_area',)


@method_decorator(login_required, name='dispatch')
class AreaUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'airwave/area_form.html'
    success_url = reverse_lazy('airwave:area_list')
    success_message = "Area %(name)s changed successfully"
    permission_required = ('airwave.change_area',)


@method_decorator(login_required, name='dispatch')
class AreaDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Area
    success_url = reverse_lazy('airwave:area_list')
    success_message = "Area %(name)s deleted successfully"
    permission_required = ('airwave.delete_area',)


@method_decorator(login_required, name='dispatch')
class AreaListView(PermissionRequiredMixin,ListView):
    model = Area
    context_object_name = 'area'
    permission_required = ('airwave.view_area',)
###############################Area######################################


###############################Operator######################################
@method_decorator(login_required, name='dispatch')
class OperatorCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Operator
    form_class = OperatorForm
    success_url = reverse_lazy('airwave:operator_list')
    success_message = "Operator %(name)s addedd successfully"
    permission_required = ('airwave.add_operator',)


@method_decorator(login_required, name='dispatch')
class OperatorUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Operator
    form_class = OperatorForm
    template_name = 'airwave/operator_form.html'
    success_url = reverse_lazy('airwave:operator_list')
    success_message = "Operator %(name)s changed successfully"
    permission_required = ('airwave.change_operator',)


@method_decorator(login_required, name='dispatch')
class OperatorDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Operator
    success_url = reverse_lazy('airwave:operator_list')
    success_message = "Operator %(name)s deleted successfully"
    permission_required = ('airwave.delete_operator',)


@method_decorator(login_required, name='dispatch')
class OperatorListView(PermissionRequiredMixin,ListView):
    model = Operator
    context_object_name = 'operator'
    permission_required = ('airwave.view_operator',)
###############################Operator######################################


###############################Employee###########################################
@method_decorator(login_required, name='dispatch')
class EmployeeCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Employee
    form_class = EmployeeForm
    #fields = ('name', 'job_title', 'username')
    success_url = reverse_lazy('airwave:employee_list')
    success_message = "Employee %(name)s addedd successfully"
    permission_required = ('airwave.add_employee',)


@method_decorator(login_required, name='dispatch')
class EmployeeUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'airwave/employee_form.html'
    success_url = reverse_lazy('airwave:employee_list')
    success_message = "Employee %(name)s changed successfully"
    permission_required = ('airwave.change_employee',)


@method_decorator(login_required, name='dispatch')
class EmployeeDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Employee
    success_url = reverse_lazy('airwave:employee_list')
    success_message = "Employee %(name)s deleted successfully"
    permission_required = ('airwave.delete_employee',)


@method_decorator(login_required, name='dispatch')
class EmployeeListView(PermissionRequiredMixin,ListView):
    model = Employee
    context_object_name = 'employee'
    permission_required = ('airwave.view_employee',)
###############################Employee###########################################

###############################Tariffplan#########################################
@method_decorator(login_required, name='dispatch')
class TariffplanCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Tariffplan
    form_class = TariffplanForm
    #fields = ('plan_name', 'billing_type', 'billing_frequency',
    #        'subscription_amount','download_limit','download_rate')
    success_url = reverse_lazy('airwave:tariffplan_list')
    success_message = "Tariff Plan %(plan_name)s addedd successfully"
    permission_required = ('airwave.add_tariffplan',)


@method_decorator(login_required, name='dispatch')
class TariffplanUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Tariffplan
    form_class = TariffplanForm
    template_name = 'airwave/tariffplan_form.html'
    success_url = reverse_lazy('airwave:tariffplan_list')
    success_message = "Tariff Plan %(plan_name)s changed successfully"
    permission_required = ('airwave.change_tariffplan',)


@method_decorator(login_required, name='dispatch')
class TariffplanDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Tariffplan     
    success_url = reverse_lazy('airwave:tariffplan_list')
    success_message = "Tariff Plan %(plan_name)s deleted successfully"
    permission_required = ('airwave.delete_tariffplan',)


@method_decorator(login_required, name='dispatch')
class TariffplanListView(PermissionRequiredMixin,ListView):
    model = Tariffplan
    context_object_name = 'tariffplan'
    permission_required = ('airwave.view_tariffplan',)
###############################Tariffplan#########################################


###############################Customer######################################
@method_decorator(login_required, name='dispatch')
class CustomerCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('airwave:customer_list')
    success_message = "Customer %(name)s addedd successfully"
    permission_required = ('airwave.add_customer',)


@method_decorator(login_required, name='dispatch')
class CustomerUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'airwave/customer_form.html'
    success_url = reverse_lazy('airwave:customer_list')
    success_message = "Customer %(name)s changed successfully"
    permission_required = ('airwave.change_customer',)


@method_decorator(login_required, name='dispatch')
class CustomerDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Customer
    success_url = reverse_lazy('airwave:customer_list')
    success_message = "Customer %(name)s deleted successfully"
    permission_required = ('airwave.delete_customer',)


@method_decorator(login_required, name='dispatch')
class CustomerListView(PermissionRequiredMixin,ListView):
    model = Customer
    context_object_name = 'customer'
    permission_required = ('airwave.view_customer',)
###############################Customer######################################

###############################Customerplan######################################
@method_decorator(login_required, name='dispatch')
class CustomerplanCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Customerplan
    form_class = CustomerplanForm
    success_url = reverse_lazy('airwave:customerplan_list')
    success_message = "Customerplan for %(customer)s added successfully"
    permission_required = ('airwave.add_customerplan',)

    def get_initial(self):
        customer = get_object_or_404(Customer,id=self.kwargs.get('customer'))
        return {'customer':customer,}


@method_decorator(login_required, name='dispatch')
class CustomerplanUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Customerplan
    form_class = CustomerplanForm
    template_name = 'airwave/customerplan_form.html'
    success_url = reverse_lazy('airwave:customerplan_list')
    success_message = "Customerplan for %(customer)s changed successfully"
    permission_required = ('airwave.change_customerplan',)


@method_decorator(login_required, name='dispatch')
class CustomerplanDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Customerplan
    success_url = reverse_lazy('airwave:customerplan_list')
    success_message = "Customerplan for %(customer)s deleted successfully"
    permission_required = ('airwave.delete_customerplan',)


@method_decorator(login_required, name='dispatch')
class CustomerplanListView(PermissionRequiredMixin,ListView):
    model = Customerplan
    context_object_name = 'customerplan'
    permission_required = ('airwave.view_customerplan',)

    def get_context_data(self, **kwargs):
        context = super(CustomerplanListView, self).get_context_data(**kwargs)
        
        # list the customers matching the search criteria 
        submitbutton = self.request.GET.get('submit')
        if submitbutton:
            context['submitbutton'] = submitbutton
            cust_id = self.request.GET.get('custid')
            cust_name = self.request.GET.get('custname')
            if cust_id and cust_name:
                context['customers'] = Customer.objects.filter(Q(name__icontains = cust_name)|
                    Q(customer_id = cust_id))
            elif cust_id:
                context['customers'] = Customer.objects.filter(customer_id = cust_id)
            elif cust_name:
                context['customers'] = Customer.objects.filter(Q(name__icontains = cust_name))
            else:
                context['error_message'] = "Please enter customer name or customer id for search."
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            #list the plans for selected customer
            listplans = self.request.GET.get('listplans')
            if listplans:
                cust_id = self.request.GET.get('customer_id')
                if cust_id:
                    queryset = queryset.filter(customer=cust_id)
        return queryset

###############################Customerplan######################################

###############################CustomerUserid######################################
@method_decorator(login_required, name='dispatch')
class CustomerUseridCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = CustomerUserid
    form_class = CustomerUseridForm
    success_url = reverse_lazy('airwave:customeruserid_list')
    success_message = "Userid for %(customer)s added successfully"
    permission_required = ('airwave.add_customeruserid',)

    def get_initial(self):
        customer = get_object_or_404(Customer,id=self.kwargs.get('customer'))
        return {'customer':customer,}


@method_decorator(login_required, name='dispatch')
class CustomerUseridUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = CustomerUserid
    form_class = CustomerUseridForm
    template_name = 'airwave/customeruserid_form.html'
    success_url = reverse_lazy('airwave:customeruserid_list')
    success_message = "Userid for %(customer)s changed successfully"
    permission_required = ('airwave.change_customeruserid',)


@method_decorator(login_required, name='dispatch')
class CustomerUseridDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = CustomerUserid
    success_url = reverse_lazy('airwave:customeruserid_list')
    success_message = "Userid for %(customer)s deleted successfully"
    permission_required = ('airwave.delete_customeruserid',)


@method_decorator(login_required, name='dispatch')
class CustomerUseridListView(PermissionRequiredMixin,ListView):
    model = CustomerUserid
    context_object_name = 'customeruserid'
    permission_required = ('airwave.view_customeruserid',)

    def get_context_data(self, **kwargs):
        context = super(CustomerUseridListView, self).get_context_data(**kwargs)
        
        # list the customers matching the search criteria 
        submitbutton = self.request.GET.get('submit')
        if submitbutton:
            context['submitbutton'] = submitbutton
            cust_id = self.request.GET.get('custid')
            cust_name = self.request.GET.get('custname')
            if cust_id and cust_name:
                context['customers'] = Customer.objects.filter(Q(name__icontains = cust_name)|
                    Q(customer_id = cust_id))
            elif cust_id:
                context['customers'] = Customer.objects.filter(customer_id = cust_id)
            elif cust_name:
                context['customers'] = Customer.objects.filter(Q(name__icontains = cust_name))
            else:
                context['error_message'] = "Please enter customer name or customer id for search."
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            #list the userids for selected customer
            listuserids = self.request.GET.get('listuserids')
            if listuserids:
                cust_id = self.request.GET.get('customer_id')
                if cust_id:
                    queryset = queryset.filter(customer=cust_id)
        return queryset

###############################CustomerUserid######################################

###############################Payments######################################
@method_decorator(login_required, name='dispatch')
class PaymentsCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Payments
    form_class = PaymentsForm
    success_url = reverse_lazy('airwave:payments_list')
    success_message = "Payment for %(customer)s added successfully"
    permission_required = ('airwave.add_payments',)

    def get_initial(self):
        customer = get_object_or_404(Customer,id=self.kwargs.get('customer'))
        return {'customer':customer,}


@method_decorator(login_required, name='dispatch')
class PaymentsUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Payments
    form_class = PaymentsForm
    template_name = 'airwave/payments_form.html'
    success_url = reverse_lazy('airwave:payments_list')
    success_message = "Payment for %(customer)s changed successfully"
    permission_required = ('airwave.change_payments',)


@method_decorator(login_required, name='dispatch')
class PaymentsDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Payments
    success_url = reverse_lazy('airwave:payments_list')
    success_message = "Payment for %(customer)s deleted successfully"
    permission_required = ('airwave.delete_payments',)


@method_decorator(login_required, name='dispatch')
class PaymentsListView(PermissionRequiredMixin,ListView):
    model = Payments
    context_object_name = 'payments'
    permission_required = ('airwave.view_payments',)

    def get_context_data(self, **kwargs):
        context = super(PaymentsListView, self).get_context_data(**kwargs)
        
        # list the customers matching the search criteria 
        submitbutton = self.request.GET.get('submit')
        if submitbutton:
            context['submitbutton'] = submitbutton
            cust_id = self.request.GET.get('custid')
            cust_name = self.request.GET.get('custname')
            if cust_id and cust_name:
                context['customers'] = Customer.objects.filter(Q(name__icontains = cust_name)|
                    Q(customer_id = cust_id))
            elif cust_id:
                context['customers'] = Customer.objects.filter(customer_id = cust_id)
            elif cust_name:
                context['customers'] = Customer.objects.filter(Q(name__icontains = cust_name))
            else:
                context['error_message'] = "Please enter customer name or customer id for search."
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            #list the payments for selected customer
            listpayments = self.request.GET.get('listpayments')
            if listpayments:
                cust_id = self.request.GET.get('customer_id')
                if cust_id:
                    queryset = queryset.filter(customer=cust_id)
        return queryset

###############################Payments######################################

###############################AirwaveCollection###########################################
@method_decorator(login_required, name='dispatch')
class AirwaveCollectionCreateView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = AirwaveCollection
    form_class = AirwaveCollectionForm
    #fields = ('name', 'job_title', 'username')
    success_url = reverse_lazy('airwave:payments_list')
    success_message = "Payment addedd successfully"
    permission_required = ('airwave.add_airwavecollection',)

    def get_initial(self):
        cust = self.kwargs.get('customer')
        if cust :            
            customer = get_object_or_404(Customer,id=self.kwargs.get('customer'))
            return {'customer':customer,}


@method_decorator(login_required, name='dispatch')
class AirwaveCollectionUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    model = AirwaveCollection
    form_class = AirwaveCollectionForm
    template_name = 'airwave/airwavecollection_form.html'
    success_url = reverse_lazy('airwave:payments_list')
    success_message = "Payement changed successfully"
    permission_required = ('airwave.change_airwavecollection',)


@method_decorator(login_required, name='dispatch')
class AirwaveCollectionDeleteView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    model = AirwaveCollection
    success_url = reverse_lazy('airwave:payments_list')
    success_message = "Payment deleted successfully"
    permission_required = ('airwave.delete_airwavecollection',)


@method_decorator(login_required, name='dispatch')
class AirwaveCollectionListView(PermissionRequiredMixin,ListView):
    model = AirwaveCollection
    context_object_name = 'collections'
    permission_required = ('airwave.view_airwavecollection',)
###############################AirwaveCollection###########################################


###############################Upload######################################
class UploadView():    
    
    @login_required
    @permission_required('airwave.add_bbnlpaymentload')  
    def upload(request,filetype): 
        # in case of GET, display import page 
        if filetype =='BILLS':
            heading = "Billing Sheet"
        elif filetype == 'BBNL':
            heading = "BBNL Payments Sheet"
        elif filetype == 'AIRWIRE' :
            heading = "Airwire Payments Sheet"
        elif filetype == 'AIRWAVE' :
            heading = "Airwave Collection Sheet"

        if request.method == 'GET':
            return render(request, 'airwave/uploadfile.html',{'heading':heading})

        #in case of POST, import file
        if request.method == 'POST':
            if filetype =='BILLS':
                file_resource = LoadBills()
            elif filetype == 'BBNL':
                file_resource = LoadBbnlPayments()
            elif filetype == 'AIRWIRE':
                file_resource = LoadAirwirePayments()
            elif filetype == 'AIRWAVE':
                file_resource = LoadCashCollection()

            dataset = Dataset()
            #new_bills = request.FILES['myfile']
            new_file = request.FILES.get('myfile',False)
            #If no files chosen, ask user to choose a file
            if new_file == False :
                message = 'Please choose a file to upload'
                return render(request, 'airwave/uploadfile.html',{'heading':heading,'message':message})

            imported_data = dataset.load(new_file.read())
            #print(imported_data)
            result = file_resource.import_data(dataset, dry_run=True)  # Test the data import

            # return error information in case of validation failure
            if result.has_validation_errors():                
                validation_errors=[]
                for invalid_row in result.invalid_rows :
                    row_msg="Row "+str(invalid_row.number)+": "
                    for key in invalid_row.field_specific_errors.keys() :
                        row_msg=row_msg+key+": "                                                
                        for value in invalid_row.field_specific_errors[key]:
                            row_msg=row_msg+value+"; "   
                        row_msg=row_msg+", "
                    validation_errors.append(row_msg)
                return render(request, 'airwave/uploadfile.html',{'heading':heading,'errors':validation_errors})
                    
            
            if filetype =='BILLS':
                load_table = 'bill_load'
            elif filetype == 'BBNL':
                load_table = 'bbnl_payment_load'
            elif filetype == 'AIRWIRE':
                load_table = 'airwire_payment_load'
            elif filetype == 'AIRWAVE':
                load_table = 'cash_collection_load'

            #Clear load table
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM '+ load_table)

            if not result.has_errors():
                file_resource.import_data(dataset, dry_run=False)  # Actually import now
                
                if filetype =='BILLS':
                    load_proc = 'bill_load_process()'
                elif filetype in ('BBNL','AIRWIRE','AIRWAVE'):
                    load_proc = "payment_load_process( '"+filetype+"' )"
                
                #Call procedure to move data to other tables
                with connection.cursor() as cursor:
                    cursor.execute('CALL '+load_proc)
                    
                message = heading + " uploaded successfully"     
            else:
                print (result.row_errors())
                message = heading + " upload failed"
           
        return render(request, 'airwave/uploadfile.html',{'heading':heading,'message':message})


###############################Upload######################################



def index(request):
# No error message for inital display
    home_url = "http://www.airwaveco.in/"
#    print(message)
    return render(request, 'airwave/index.html', {'home_url': home_url})

@login_required
def start(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('airwave:login'))
   
    #parse all models appended with '_' from the permissions after splitting on '_'
    #eg. permission add_customer will give 'customer_'
    #createing set for uniq values.
    #model_perms : model level permissions are used to display the access links

    model_perms = set([i.split('_')[-1]+"_" for i in list(request.user.get_all_permissions())])
    return render(request, 'airwave/start.html',{'model_perms':model_perms})
    

