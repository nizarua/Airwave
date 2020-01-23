CREATE OR REPLACE FUNCTION delete_payments()
RETURNS TRIGGER
AS $$
DECLARE

BEGIN
--If an existing record is deleted from airwave_collection tables, then corresponding
--record will be deleted from payments table.
--Relationship between airwave_collection and payments tables are established by 
--customer_id, receipt_no and receipt_date.


--Deletion from payements table should be done in BEFORE trigger
--because of foreign key constraint on airwave_collection_id in payments table.

	IF TG_OP = 'DELETE' THEN
		DELETE FROM payments p
		WHERE OLD.customer_id = p.customer_id 
			AND OLD.receipt_no = p.receipt_number
			AND OLD.collection_date = p.payment_date;		
		
		RETURN OLD;
	END IF;	

	
	IF TG_OP = 'UPDATE' THEN
		-- Delete record from payments if customer removed from airwave_collection record
		IF OLD.customer_id IS NOT NULL AND (
			(NEW.customer_id IS NULL) OR (NEW.customer_id <> OLD.customer_id))THEN
			DELETE FROM payments p
			WHERE OLD.customer_id = p.customer_id 
				AND OLD.receipt_no = p.receipt_number
				AND OLD.collection_date = p.payment_date;			
		END IF;

		RETURN NEW;
					
	END IF;	

	RETURN NULL;
	
END;$$
LANGUAGE PLPGSQL;

ALTER FUNCTION public.delete_payments()
    OWNER TO airwave_admin;

CREATE TRIGGER tr_airwave_collection_before_ud
    BEFORE DELETE OR UPDATE
    ON public.airwave_collection
    FOR EACH ROW
    EXECUTE PROCEDURE public.delete_payments();