# Generated by Django 2.2.6 on 2019-12-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airwave', '0006_auto_20191122_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField(blank=True, null=True)),
                ('activation_date', models.DateField(blank=True, null=True)),
                ('tariff_plan', models.CharField(blank=True, max_length=50, null=True)),
                ('bill_no', models.CharField(blank=True, max_length=30, null=True)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('subs_from', models.DateField(blank=True, null=True)),
                ('subs_to', models.DateField(blank=True, null=True)),
                ('downl_from', models.DateField(blank=True, null=True)),
                ('downl_to', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('line1', models.CharField(blank=True, max_length=50, null=True)),
                ('line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('line_3', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('contact_no1', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('contact_no2', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('operator', models.CharField(blank=True, max_length=50, null=True)),
                ('installation', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('activation', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_a', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('subscription_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('instlmnt', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_c', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_downloads_mb', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('download_limit_mb', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('extra_downloads_mb', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('download_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('download_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('miscell_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('currentcharges', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('service_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_current_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('previous_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('payment_received', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('adjustments', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_balance_due', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('currentcharges_h', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_amount_due', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('tot_aft_due_date', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(blank=True, max_length=25, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('payment', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_usage', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('inventum', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('inventum_1', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('inventum_2', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('executive', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_type', models.CharField(blank=True, max_length=50, null=True)),
                ('coll_exe_mob', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('old_code', models.CharField(blank=True, max_length=50, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bill_load',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerUserid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('isp', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'customer_userid',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='customerplan',
            options={'managed': False, 'ordering': ['customer', 'start_date']},
        ),
        migrations.AlterModelTable(
            name='airwaveconfig',
            table='airwaveconfig',
        ),
        migrations.AlterModelTable(
            name='area',
            table='area',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='customerplan',
            table='customer_plan',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='employee',
        ),
        migrations.AlterModelTable(
            name='isp',
            table='isp',
        ),
        migrations.AlterModelTable(
            name='operator',
            table='operator',
        ),
        migrations.AlterModelTable(
            name='tariffplan',
            table='tariffplan',
        ),
    ]
