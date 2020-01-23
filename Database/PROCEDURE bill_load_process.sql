CREATE OR REPLACE PROCEDURE bill_load_process()
LANGUAGE PLPGSQL
AS $$
DECLARE
	rec_plan RECORD;
	rec_bill RECORD;
	datalimit tariffplan.data_limit%TYPE;
	bandwidth tariffplan.bandwidth%TYPE;
	plantype tariffplan.plan_type%TYPE;
	frequency tariffplan.billing_frequency%TYPE;
	subscription tariffplan.subscription_amount%TYPE;
	datacharge tariffplan.data_charge%TYPE;
	msg varchar(1000);
	particular bill_details.particulars%TYPE;

	cur_plans CURSOR FOR 
	SELECT UPPER(tariff_plan) plan, 
		split_part(UPPER(tariff_plan),'_',2) bandwidth, 
		split_part(UPPER(tariff_plan),'_',3) datalimit,
		split_part(UPPER(tariff_plan),'_',4) frequency,
		max(subscription_amount) subscrption
		FROM bill_load  
		WHERE UPPER(tariff_plan) NOT IN (
			SELECT DISTINCT UPPER(plan_name) 
			FROM tariffplan )
		GROUP BY UPPER(tariff_plan) ;

	cur_bill CURSOR FOR
	SELECT UPPER(bill_no) bill_no,
		(SELECT id from customer where customer_id = cust_id) customer_id,
		installation, activation, deposit,subscription_amount,download_charges,miscell_charges, service_tax, previous_balance, adjustments
	FROM bill_load  
		WHERE EXISTS 
			(SELECT  1 FROM bill_summary 
			WHERE UPPER(bill_number ) = UPPER(bill_no))
		AND NOT EXISTS 
			(SELECT  1 FROM bill_details 
			WHERE UPPER(bill_number ) = UPPER(bill_no));

BEGIN
	OPEN cur_plans;	

	LOOP
		bandwidth = NULL;
		datalimit = NULL;
		plantype = NULL;
		frequency = NULL;
		subscription = NULL;
		datacharge = NULL;
		msg = NULL;

		FETCH cur_plans INTO rec_plan;


		EXIT WHEN NOT FOUND;

		-- extract bandwidth 
		IF position('MBPS' in rec_plan.bandwidth) > 0 THEN
			bandwidth = CAST(LEFT(rec_plan.bandwidth,position('MBPS' in rec_plan.bandwidth)-1) AS INTEGER);
			
		END IF;
		
		-- extract datalimit 
		IF position('GB' in rec_plan.datalimit) > 0 THEN
			datalimit = CAST(LEFT(rec_plan.datalimit,position('GB' in rec_plan.datalimit)-1) AS INTEGER);
			plantype = 'L';
			
		ELSEIF rec_plan.datalimit = 'UL' THEN
			plantype = 'U';
			
		END IF;

		-- extract billing frequency
		CASE rec_plan.frequency
			WHEN 'YLY' THEN
				frequency = 'Y';
			WHEN 'HLY' THEN
				frequency = 'H';
			WHEN 'QLY' THEN
				frequency = 'Q';
			ELSE
				frequency = 'M';
		END CASE;
		-- msg = "INSERT INTO tariffplan (plan_name,billing_type,billing_frequency,subscription_amount,";
		-- msg = msg || "data_limit,data_charge,plan_type,bandwidth) VALUES ('%','PO_PD','%',%,%,%,'%',%)";

		-- RAISE NOTICE 'plan_name %,billing_frequency %, subscription_amount %', rec_plan.plan,frequency,rec.subscrption;
		-- RAISE NOTICE 'data_limit %,data_charge %,plan_type %,bandwidth %', datalimit, datacharge,  plantype, bandwidth;

		INSERT INTO tariffplan (plan_name,billing_type,billing_frequency,subscription_amount, data_limit,data_charge,plan_type,bandwidth) VALUES (rec_plan.plan,'PO-PD',frequency, rec_plan.subscrption, datalimit, datacharge, plantype, bandwidth);		


	END LOOP;

	CLOSE cur_plans;

	--commmits changes to tariffplan
	COMMIT;

	--extract area info
	INSERT INTO area(name)
	SELECT TRIM(area)
		FROM bill_load  
		WHERE UPPER(TRIM(area)) NOT IN (
			SELECT DISTINCT UPPER(TRIM(name)) 
			FROM area )
		GROUP BY area
		ORDER BY area ;

	-- commits changes to area
	COMMIT;

	--extract executive employee info
	INSERT INTO employee(name,mobile,job_title)
	SELECT TRIM(executive), MAX(coll_exe_mob), 'Executive'
		FROM bill_load  
		WHERE UPPER(TRIM(executive)) NOT IN (
			SELECT DISTINCT UPPER(TRIM(name)) 
			FROM employee )
		GROUP BY TRIM(executive)
		ORDER BY 1 ;

	-- commits changes to employee
	COMMIT;

	--extract operator info 
	INSERT INTO operator(name)
	SELECT UPPER(TRIM(operator))
		FROM bill_load  
		WHERE UPPER(TRIM(operator)) NOT IN (
			SELECT DISTINCT UPPER(TRIM(name)) 
			FROM operator )
		GROUP BY UPPER(TRIM(operator))
		ORDER BY 1 ;

	-- commits changes to operator
	COMMIT;

	--extract customer info 
	--if cust_id not in customer
	INSERT INTO customer(customer_id,name,billing_address_line1,billing_address_line2,billing_address_line3,billing_address_city,billing_address_pincode,mobile1,mobile2,email_id,active_user_id,active_plan_id,activation_date,allocated_ip,status,connection_type,area_id,remarks,balance_due)
	SELECT cust_id, name, line1, line_2, line_3, city, postal_code, contact_no1, contact_no2, e_mail, user_id,
	(SELECT id FROM tariffplan WHERE UPPER(plan_name) = UPPER(tariff_plan)), activation_date, ip,
	(SELECT key_code FROM airwaveconfig WHERE UPPER(key_value)= UPPER(status) and key_name = 'customer_status'),
	CASE 
		WHEN upper(tariff_plan) like '%CORP%' THEN 'C'
		ELSE 'R'
	END,
	(SELECT id FROM area WHERE UPPER(name) = UPPER(TRIM(area))),
	remarks,
	total_amount_due
		FROM bill_load  
		WHERE cust_id NOT IN (
			SELECT customer_id 
			FROM customer );

	-- commits changes to customer
	COMMIT;

	--Insert into customer_plan
	--if cust_id with Active tariffplan does not exist in customer_plan
	--and cust_id exists in customer and tariff_plan exists in tariffplan
	INSERT INTO customer_plan (customer_id,tariffplan_id, start_date, status)
	SELECT 
	(SELECT id from customer where customer_id = cust_id),
	(SELECT id FROM tariffplan WHERE UPPER(plan_name) = UPPER(tariff_plan)),
	activation_date, 'A'
	FROM bill_load  
		WHERE NOT EXISTS ( SELECT customer_id 
			FROM customer_plan
			WHERE customer_id = (SELECT id from customer where customer_id = cust_id)
			AND tariffplan_id = (SELECT id FROM tariffplan WHERE UPPER(plan_name) = UPPER(tariff_plan))
			AND status = 'A')
			AND EXISTS (SELECT id from customer where customer_id = cust_id)
			AND EXISTS (SELECT id FROM tariffplan WHERE UPPER(plan_name) = UPPER(tariff_plan));

	-- commits changes to customer_plan
	COMMIT;

	--Insert into customer_userid
	--if cust_id does not exist in customer_userid and cust_id exists in customer 
	INSERT INTO customer_userid (customer_id,user_id, start_date, status)
	SELECT 
	(SELECT id from customer where customer_id = cust_id),
	user_id, activation_date, 'A'
	FROM bill_load  
		WHERE NOT EXISTS ( SELECT customer_id 
			FROM customer_userid
				WHERE customer_id = (SELECT id from customer where customer_id = cust_id))			
			AND EXISTS (SELECT id from customer where customer_id = cust_id)	;		

	-- commits changes to customer_user_id
	COMMIT;



	--extract bill summary info 
	--if bill_no not in bill_summary and cust_id is present in customer and tariff_plan is 
	--present in customer_plan. 
	INSERT INTO bill_summary(customer_id,bill_number,plan_id,bill_date,due_date,subs_from,subs_to)
	SELECT 
	(SELECT id from customer where customer_id = cust_id), 
	UPPER(bill_no),
	(SELECT cp.id FROM customer_plan cp,customer c,tariffplan tp 
		WHERE UPPER(tp.plan_name) = UPPER(tariff_plan)
		AND tp.id = cp.tariffplan_id
		AND cp.customer_id = c.id 
		AND c.customer_id = cust_id),
	bill_date,due_date,subs_from,subs_to
	FROM bill_load  
		WHERE UPPER(bill_no) NOT IN (
			SELECT UPPER(bill_number )
				FROM bill_summary )
			AND bill_no IS NOT NULL
			AND cust_id IN (SELECT customer_id FROM customer)
			AND UPPER(tariff_plan) IN (SELECT UPPER(tp.plan_name) 
				FROM customer_plan cp,customer c,tariffplan tp 
					WHERE UPPER(tp.plan_name) = UPPER(tariff_plan)
					AND tp.id = cp.tariffplan_id
					AND cp.customer_id = c.id 
					AND c.customer_id = cust_id);

	-- commits changes to bill_summary
	COMMIT;

	--extract bill details info
	OPEN cur_bill;

	LOOP
		FETCH cur_bill INTO rec_bill;
		EXIT WHEN NOT FOUND;

		--Installation Charge
		IF rec_bill.installation IS NOT NULL and rec_bill.installation <> 0 THEN			
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'IC',rec_bill.installation);
		END IF;

		--Activation Charge
		IF rec_bill.activation IS NOT NULL and rec_bill.activation <> 0 THEN			
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'AC',rec_bill.activation);
		END IF;

		--Deposit Amount
		IF rec_bill.deposit IS NOT NULL and rec_bill.deposit <> 0 THEN			
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'DA',rec_bill.deposit);
		END IF;

		--Subscription Fee
		IF rec_bill.subscription_amount IS NOT NULL and rec_bill.subscription_amount <> 0 THEN			
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'SF',rec_bill.subscription_amount);
		END IF;

		--Download charges
		IF rec_bill.download_charges IS NOT NULL and rec_bill.download_charges <> 0 THEN		
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'DC',rec_bill.download_charges);
		END IF;

		--Miscellenious charges
		IF rec_bill.miscell_charges IS NOT NULL and rec_bill.miscell_charges <> 0 THEN		
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'MC',rec_bill.miscell_charges);
		END IF;

		--Service Tax
		IF rec_bill.service_tax IS NOT NULL and rec_bill.service_tax <> 0 THEN		
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'MC',rec_bill.service_tax);
		END IF;		

		--Previous Balance
		IF rec_bill.previous_balance IS NOT NULL and rec_bill.previous_balance <> 0 THEN		
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'PB',rec_bill.previous_balance);
		END IF;	

		--Adjustments Amount
		IF rec_bill.adjustments IS NOT NULL and rec_bill.adjustments <> 0 THEN		
			INSERT INTO bill_details(customer_id, bill_number,particulars,amount)
			VALUES (rec_bill.customer_id, rec_bill.bill_no,'AA',rec_bill.adjustments);
		END IF;			

	END LOOP;
	CLOSE cur_bill;

	-- commits changes to bill_details
	COMMIT;

END;
$$