CREATE USER kattakke;

CREATE DATABASE kattakke;

GRANT ALL PRIVILEGES ON DATABASE kattakke TO kattakke;

\c kattakke

CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$ BEGIN NEW.updated_at = NOW(); RETURN NEW; END; $$ LANGUAGE plpgsql;
