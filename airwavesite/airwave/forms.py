# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:27:37 2019

@author: Ullampuzha.Nizar
"""

from django import forms
from .models import Employee, Tariffplan, Airwaveconfig, Isp, Area, Operator, Customer, \
    Customerplan, CustomerUserid, Payments, AirwaveCollection
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def keyvalues(keyname):
    #Gets tuples of (key_code,key_value) from configuration table
    return Airwaveconfig.objects.filter(key_name = keyname).values_list('key_code','key_value')   

def get_area():
    #Gets tuples of (id, name) oreder by name from Area table
    return Area.objects.values_list().order_by('name')

class AirwaveconfigForm(forms.ModelForm):
    class Meta:
        model = Airwaveconfig
        fields = ('key_name', 'key_code', 'key_value')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = ('name','area')        
        labels={'area':'Select Area',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        #self.fields['area'].empty_label=None

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'job_title', 'username','mobile')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


class TariffplanForm(forms.ModelForm):    
    class Meta:
        model = Tariffplan
        fields = ('plan_name', 'billing_type', 'billing_frequency',
            'subscription_amount','data_limit','data_charge','plan_type','bandwidth')
        widgets = {'billing_type': forms.Select(choices= keyvalues('billing_type')),
        'billing_frequency': forms.Select(choices=keyvalues('billing_frequency')),
        'plan_type': forms.Select(choices=keyvalues('plan_type')),}
        labels={'data_limit':'Data Limit (GB)','subscription_amount':'Subscription Amount (Rs.)',
        'data_charge': 'Data Charge (Rs./MB)', 'plan_type': 'Plan Type',
        'bandwidth': 'Bandwidth (Mbps)'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['billing_type'].initial='Post-paid'
        self.fields['billing_frequency'].initial='Monthly'
        self.fields['plan_type'].initial='Unlimited'        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {'connectivity_device': forms.Select(choices= keyvalues('connectivity_device')),
        'status': forms.Select(choices= keyvalues('customer_status')),
        'customer_type': forms.Select(choices= keyvalues('customer_type')),
        'connection_type': forms.Select(choices= keyvalues('connection_type')),
        'remarks': forms.Textarea({'rows':5}),
        'activation_date': forms.SelectDateWidget (years = range(1990,2020),
            empty_label=('Year','Month','Day'),attrs=({'style': 'width: 33%; \
                display: inline-block;'})),
        'email_id': forms.EmailInput()}  
        labels={'customer_id':'Customer ID',
            'name':'Customer Name',
            'billing_address_line1':'Address Line1',
            'billing_address_line2':'Address Line2',
            'billing_address_line3':'Address Line3',
            'billing_address_city':'City',
            'billing_address_pincode':'Pincode',
            'installation_address_line1':'Address Line1',
            'installation_address_line2':'Address Line2',
            'installation_address_line3':'Address Line3',
            'installation_address_city':'City',
            'installation_address_pincode':'Pincode',
            'contact_name':'Contact Name',
            'mobile1':'Mobile',
            'mobile2':'Alternate Mobile',
            'landline':'Landline',
            'email_id':'Email',
            'profession':'Profession',
            'connectivity_device':'Connectivity Device',
            'active_user_id':'User ID',
            'active_plan':'Plan Name',
            'activation_date':'Activation Date',
            'allocated_ip':'Allocated IP ',
            'status':'Status',
            'isp':'ISP Name',
            'customer_type':'Customer Type',
            'parent_customer_id':'Root Customer ID',
            'connection_type':'Connnection Type',
            'area':'Area',
            'balance_due': 'Due Amount (Rs)'
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['isp'].empty_label=None

class CustomerplanForm(forms.ModelForm):
    class Meta:
        model = Customerplan
        fields = '__all__'
        widgets = {'status': forms.Select(choices= keyvalues('customerplan_status')),}
#        labels={'area':'Select Area',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        #self.fields['area'].empty_label=None


class CustomerUseridForm(forms.ModelForm):
    class Meta:
        model = CustomerUserid
        fields = '__all__'
        widgets = {'status': forms.Select(choices= keyvalues('customeruserid_status')),}
#        labels={'area':'Select Area',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'
        widgets = {'payment_type': forms.Select(choices= keyvalues('payment_type')),
        'payment_channel': forms.Select(choices= keyvalues('payment_channel')),
        'remarks': forms.Textarea({'rows':5}),}
        labels={'payment_type':'Type',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class AirwaveCollectionForm(forms.ModelForm):
    class Meta:
        model = AirwaveCollection
        fields = '__all__'
        widgets = {'wallet_name': forms.Select(choices= keyvalues('wallet_name')),
        'remarks': forms.Textarea({'rows':3}),}
#        labels={'area':'Select Area',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['wallet_name'].initial=''
        
