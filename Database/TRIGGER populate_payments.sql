CREATE OR REPLACE FUNCTION populate_payments()
RETURNS TRIGGER
AS $$
DECLARE

BEGIN
--Insert new records into payments table when airwave_collection table is populated.
--payments table acts as summary table while airwave_collection table contains details.
--If airwave_collection table is updated for an existing record, 
--corresponding record in payments table will be updated.
--If an existing record is deleted from airwave_collection tables, then corresponding
--record will be deleted from payments table.
--Relationship between airwave_collection and payments tables are established by 
--customer_id, receipt_no and receipt_date.


	IF (TG_OP = 'INSERT' AND NEW.customer_id IS NOT NULL) THEN
		INSERT INTO payments (customer_id, payment_channel, receipt_number, payment_date,
			payment_amount,payment_type, remarks, bill_number, airwave_collection_id)
		SELECT customer_id, 'AIRWAVE',receipt_no, collection_date,total_amount,'BL', remarks,
			bill_number,id
		FROM NEW 
		WHERE NOT EXISTS (SELECT 1 FROM payments p
			WHERE NEW.customer_id = p.customer_id 
				AND NEW.receipt_no = p.receipt_number
				AND NEW.collection_date = p.payment_date);
		
	END IF;

	--DELETE is commented as deletion from payements table should be done in BEFORE trigger
	--because of foreign key constraint on airwave_collection_id in payments table.
/*
	IF TG_OP = 'DELETE' THEN
		DELETE FROM payments p
		WHERE OLD.customer_id = p.customer_id 
			AND OLD.receipt_no = p.receipt_number
			AND OLD.collection_date = p.payment_date;		
		
	END IF;*/

	IF TG_OP = 'UPDATE' THEN

		IF (NEW.customer_id IS NOT NULL AND OLD.customer_id IS NOT NULL) THEN
		-- Update existing record in payments if customer exists in old and new records
			UPDATE payments p
			SET customer_id = NEW.customer_id, 
				receipt_number = NEW.receipt_no, 
				payment_date = NEW.collection_date,
				payment_amount = NEW.total_amount, 
				remarks = NEW.remarks,
				bill_number = NEW.bill_number
			WHERE OLD.customer_id = p.customer_id 
				AND OLD.receipt_no = p.receipt_number
				AND OLD.collection_date = p.payment_date;
		END IF;

		IF (NEW.customer_id IS NOT NULL AND OLD.customer_id IS NULL) THEN
		-- Insert new record in payments if customer is added to airwave_collection record
			INSERT INTO payments (customer_id, payment_channel, receipt_number, payment_date,
				payment_amount,payment_type, remarks, bill_number, airwave_collection_id)
			SELECT customer_id, 'AIRWAVE',receipt_no, collection_date,total_amount,'BL', remarks,
				bill_number,id
			FROM NEW 
			WHERE NOT EXISTS (SELECT 1 FROM payments p
				WHERE NEW.customer_id = p.customer_id 
					AND NEW.receipt_no = p.receipt_number
					AND NEW.collection_date = p.payment_date);
		END IF;

		-- Below code is commented as deletion from payements table should be done in BEFORE trigger	
		--IF (NEW.customer_id IS NULL AND OLD.customer_id IS NOT NULL) THEN
		-- Delete record from payments if customer removed from airwave_collection record			
		--END IF;


	END IF;

	RETURN NULL;
END;$$
LANGUAGE PLPGSQL;

ALTER FUNCTION public.populate_payments()
    OWNER TO airwave_admin;

CREATE TRIGGER tr_airwave_collection_after_iu
    AFTER INSERT OR UPDATE
    ON public.airwave_collection
    FOR EACH ROW
    EXECUTE PROCEDURE public.populate_payments();