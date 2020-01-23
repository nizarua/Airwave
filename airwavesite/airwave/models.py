from django.db import models

# Create your models here.

###############################################################################
class Airwaveconfig(models.Model):
    key_name = models.CharField(max_length=50)
    key_code = models.CharField(max_length=50)
    key_value = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'airwaveconfig'    

###############################################################################
class Isp(models.Model):
    isp_name = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = False
        db_table = 'isp'

    # __str__ implemented for displaying isp_name by default in referenced forms
    # using foreign key
    def __str__(self):
        return self.isp_name

###############################################################################
class Area(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = False
        db_table = 'area'
        ordering = ['name'] #area will be displayed in sorted order

    # __str__ implemented for displaying name by default in referenced forms
    # using foreign key
    def __str__(self):
        return self.name

###############################################################################
class Operator(models.Model):
    name = models.CharField(unique=True, max_length=50, )
    area = models.ForeignKey('Area', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operator'
        ordering = ['name'] #operator will be displayed in sorted order

    # __str__ implemented for displaying name by default in referenced forms
    # using foreign key
    def __str__(self):
        return self.name

###############################################################################
class Employee(models.Model):
    #id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=25)
    username = models.CharField(max_length=50, blank=False, null=False)
    mobile = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'employee'
        ordering = ['name'] #employee will be displayed in sorted order

    # __str__ implemented for displaying name by default in referenced forms
    # using foreign key
    def __str__(self):
        return self.name


###############################################################################
class Tariffplan(models.Model):
    plan_name = models.CharField(unique=True, max_length=50)
    billing_type = models.CharField(max_length=5, blank=True, null=True)
    billing_frequency = models.CharField(max_length=1, blank=True, null=True)
    subscription_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    data_limit = models.SmallIntegerField(blank=True, null=True)
    data_charge = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    plan_type = models.CharField(max_length=1, blank=True, null=True)
    bandwidth = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariffplan'
        ordering = ['plan_name'] #plan will be displayed in sorted order

    # __str__ implemented for displaying plan_name by default in referenced forms
    # using foreign key
    def __str__(self):
        return self.plan_name

#    def get_key_values():
#        return Airwaveconfig.objects.filter(key_name = '')
###############################################################################

class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    billing_address_line1 = models.CharField(max_length=50, blank=True, null=True)
    billing_address_line2 = models.CharField(max_length=50, blank=True, null=True)
    billing_address_line3 = models.CharField(max_length=50, blank=True, null=True)
    billing_address_city = models.CharField(max_length=50, blank=True, null=True)
    billing_address_pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    installation_address_line1 = models.CharField(max_length=50, blank=True, null=True)
    installation_address_line2 = models.CharField(max_length=50, blank=True, null=True)
    installation_address_line3 = models.CharField(max_length=50, blank=True, null=True)
    installation_address_city = models.CharField(max_length=50, blank=True, null=True)
    installation_address_pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True)
    mobile1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mobile2 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    landline = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    email_id = models.CharField(max_length=50, blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    connectivity_device = models.CharField(max_length=50, blank=True, null=True)
    active_user_id = models.CharField(max_length=50, blank=True, null=True)
    active_plan = models.ForeignKey('Tariffplan', models.DO_NOTHING, blank=True, null=True)
    activation_date = models.DateField(blank=True, null=True)
    allocated_ip = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    isp = models.ForeignKey('Isp', models.DO_NOTHING, blank=True, null=True)
    customer_type = models.CharField(max_length=25, blank=True, null=True)
    parent_customer_id = models.IntegerField(blank=True, null=True)
    connection_type = models.CharField(max_length=25, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    balance_due = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
        ordering = ['name']

    # __str__ implemented for displaying name by default in referenced forms
    # using foreign key
    def __str__(self):
        return self.name
###############################################################################

class Customerplan(models.Model):
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    tariffplan = models.ForeignKey('Tariffplan', models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_plan'
        ordering = ['customer','start_date']

    # __str__ implemented for displaying name by default in referenced forms
    # using foreign key
    def __str__(self):
        return f'{self.customer} {self.tariffplan}'
###############################################################################

class CustomerUserid(models.Model):
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    user_id = models.CharField(max_length=50)
    isp = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_userid'

    # __str__ implemented for displaying name by default in referenced forms
    # using foreign key
    def __str__(self):
        return f'{self.customer} {self.user_id}'

###############################################################################
class BillLoad(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    activation_date = models.DateField(blank=True, null=True)
    tariff_plan = models.CharField(max_length=50, blank=True, null=True)
    bill_no = models.CharField(max_length=30, blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    subs_from = models.DateField(blank=True, null=True)
    subs_to = models.DateField(blank=True, null=True)
    downl_from = models.DateField(blank=True, null=True)
    downl_to = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    line1 = models.CharField(max_length=50, blank=True, null=True)
    line_2 = models.CharField(max_length=50, blank=True, null=True)
    line_3 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    contact_no1 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contact_no2 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    installation = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    activation = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_a = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    deposit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    subscription_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    instlmnt = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_c = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_downloads_mb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    download_limit_mb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    extra_downloads_mb = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    download_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    download_charges = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    miscell_charges = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    currentcharges = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    service_tax = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_current_charges = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    previous_balance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_received = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    adjustments = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_balance_due = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    currentcharges_h = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_amount_due = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tot_aft_due_date = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=25, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    payment = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_usage = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    inventum = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    inventum_1 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    inventum_2 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    executive = models.CharField(max_length=50, blank=True, null=True)
    billing_type = models.CharField(max_length=50, blank=True, null=True)
    coll_exe_mob = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    old_code = models.CharField(max_length=50, blank=True, null=True)
    e_mail = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_load'
###############################################################################

class BbnlPaymentLoad(models.Model):
    cid = models.CharField(max_length=50, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbnl_payment_load'
###############################################################################

class AirwirePaymentLoad(models.Model):
    user_id = models.CharField(max_length=50, blank=True, null=True)
    receipt_date = models.DateField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    receipt_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airwire_payment_load'
###############################################################################

class Payments(models.Model):
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    payment_channel = models.CharField(max_length=10)
    receipt_number = models.CharField(max_length=20, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    payment_type = models.CharField(max_length=2)
    bill_number = models.CharField(max_length=30, blank=True, null=True)
    airwave_collection = models.ForeignKey('AirwaveCollection', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'
###############################################################################

class CashCollectionLoad(models.Model):
    receipt_no = models.CharField(max_length=20, blank=True, null=True)
    collection_person = models.CharField(max_length=20, blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    cash_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cheque_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    online_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    wallet_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cheque_no = models.CharField(max_length=25, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    online_portal = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    particulars = models.CharField(max_length=50, blank=True, null=True)
    wallet_name = models.CharField(max_length=10, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_collection_load'
###############################################################################

class AirwaveCollection(models.Model):
    receipt_no = models.CharField(max_length=20, blank=True, null=True)
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    particulars = models.CharField(max_length=50, blank=True, null=True)
    cash_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cheque_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    online_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    wallet_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cheque_no = models.CharField(max_length=25, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    cheque_date = models.DateField(blank=True, null=True)
    online_portal = models.CharField(max_length=50, blank=True, null=True)
    wallet_name = models.CharField(max_length=10, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    bill_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'airwave_collection'

###############################################################################

