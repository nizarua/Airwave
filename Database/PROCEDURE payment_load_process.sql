CREATE OR REPLACE PROCEDURE payment_load_process( paytype VARCHAR)
LANGUAGE PLPGSQL
AS $$
DECLARE



BEGIN
	
	IF paytype = 'BBNL' THEN
		INSERT INTO payments (customer_id, payment_channel, receipt_number, payment_date,
			payment_amount,payment_type, remarks)
		SELECT 
		(SELECT id from customer where active_user_id = cid),
		paytype,bill_no,payment_date, paid_amount,'BL','Payment uploaded from BBNL'
		FROM bbnl_payment_load
		WHERE NOT EXISTS (SELECT 1 FROM payments
			WHERE receipt_number = bill_no) 
		AND EXISTS (SELECT id from customer where active_user_id = cid);
	ELSEIF paytype = 'AIRWIRE' THEN
		INSERT INTO payments (customer_id, payment_channel, receipt_number, payment_date,
			payment_amount,payment_type, remarks)
		SELECT 
		(SELECT id from customer where active_user_id = user_id),
		paytype,receipt_no,receipt_date, paid_amount, 'BL','Payment uploaded from AIRWIRE'
		FROM airwire_payment_load
		WHERE NOT EXISTS (SELECT 1 FROM payments
			WHERE receipt_number = receipt_no)
		AND EXISTS (SELECT id from customer where active_user_id = user_id);

	ELSEIF paytype = 'AIRWAVE' THEN

		INSERT INTO airwave_collection (receipt_no, employee_id, collection_date, customer_id, 
			particulars, cash_amount, cheque_amount, online_amount, wallet_amount, total_amount,
			cheque_no, bank_name, cheque_date, online_portal, wallet_name, reference_no, remarks)
		SELECT receipt_no,
			(SELECT id from employee where name = collection_person),
			collection_date,
			(SELECT id from customer where customer_id = customer_code),
			particulars, cash_amount, cheque_amount, online_amount,	wallet_amount, total_amount,
			cheque_no, bank_name, cheque_date, online_portal, wallet_name,reference_no,
			remarks || ' Payment uploaded from AIRWAVE'
		FROM cash_collection_load ccl
		WHERE NOT EXISTS (SELECT 1 FROM airwave_collection ac
				WHERE ccl.receipt_no = ac.receipt_no AND ccl.collection_date = ac.collection_date);


	END IF;
	
	-- commits changes to payments
	COMMIT;

END;
$$