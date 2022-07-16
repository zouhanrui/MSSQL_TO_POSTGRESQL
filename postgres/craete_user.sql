-- create etl user
create user hanrui_etl with password 'etlpassowrd';
-- grant connect
grant connect on database "testdb" to hanrui_etl;
-- grant table permissions
grant select, insert, update, delete on all tables in schema public to hanrui_etl;