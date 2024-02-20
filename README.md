# DDL-Maker

## Purpose

These python files do long string concatenation for SQL and Snowflake queries needed for:
 - bulk copy process IO of missing cadence tables from on prem server (MSSQL)
 - file ingestion to snowflake.


## Instructions 
1. Put the all caps table names list from JIRA ticket into text file in input folder named:
	tablenamesCAPS.txt

2. Run sql_get_ddl.py

3. Find produced text files in output folder:
	sql_get_ddl.txt
	sql_get_pks.txt
	sql_get_tableinfo.txt

4. Run GET DDL queries in sql server.

5. Paste output from sql into text files in input folder named:
	tablenames.txt
	create_history_table_empty_pk.txt
	create_table_empty_pk.txt
	PKlist.txt

6. Run snf_ddl.py

7. Find produced text file in output folder:
	snowflake_ddl.txt

8. Run DDL queries in snowflake DEV.

9. Create RFC to run DDL queries in snowflake PROD.

10. Run cadence_bcpio_config_maker.py.

11. Find produced text files in output folder:
	dev_bcpio_configs.txt
	dev_t_file_load_configs.txt
	prod_bcpio_configs.txt
	prod_t_file_load_configs.txt

12. Run queries to insert configuration entries for source export and file ingestion in Snowflake DEV and PROD, respectively.
