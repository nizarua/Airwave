CREATE OR REPLACE FUNCTION update_balance_due()
RETURNS TRIGGER
AS $$
DECLARE

BEGIN
	IF TG_OP = 'INSERT' THEN
		UPDATE customer SET balance_due = balance_due - NEW.payment_amount
		WHERE id = NEW.customer_id;
		
	END IF;

	IF TG_OP = 'DELETE' THEN
		UPDATE customer SET balance_due = balance_due + OLD.payment_amount
		WHERE id = OLD.customer_id;
		
	END IF;

	IF TG_OP = 'UPDATE' THEN
		IF OLD.customer_id <> NEW.customer_id  THEN
			--if customer is changed, update balance for both customers
			UPDATE customer SET balance_due = balance_due + OLD.payment_amount
			WHERE id = OLD.customer_id;

			UPDATE customer SET balance_due = balance_due - NEW.payment_amount
			WHERE id = NEW.customer_id;
		ELSEIF OLD.customer_id = NEW.customer_id THEN
			-- if customer has not changed, update balance 
			UPDATE customer 
			SET balance_due = balance_due - (NEW.payment_amount - OLD.payment_amount) 
			WHERE id = NEW.customer_id;
		END IF;
		
	END IF;

	RETURN NULL;
END;$$
LANGUAGE PLPGSQL;

ALTER FUNCTION public.update_balance_due()
    OWNER TO airwave_admin;

CREATE TRIGGER tr_payments_after_iud
    AFTER INSERT OR DELETE OR UPDATE OF customer_id, payment_amount
    ON public.payments
    FOR EACH ROW
    EXECUTE PROCEDURE public.update_balance_due();