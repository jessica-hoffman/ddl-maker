## get ddl and pk sql code maker
## jessica hoffman
##1/18/24

from config import tablenamesCAPSLoc, sql1Loc,sql2Loc,sql3Loc,sql4Loc,sql5Loc,sql6Loc,out0Loc,out00Loc,out000Loc

#READ IN TABLE NAMES
tn = open(tablenamesCAPSLoc,'r')
tables = ["".join(line.rstrip()) for line in tn]
tables_string = ''
i=0
n=len(tables)

for t in tables:
    tables_string = ''.join([tables_string,"'",t,"'"])
    if i <= n-2:
        tables_string = ''.join([tables_string,','])
    i+=1
tn.close()


#MS SQL GET DDL MAKER
def sql_get_ddl_maker():
    with open(sql1Loc,'r') as string:
        sql1 = string.read()
    with open(sql2Loc,'r') as string:
        sql2 = string.read()
    with open(sql3Loc,'r') as string:
        sql3 = string.read()
    
    # base tables
    with open(out0Loc,'w') as f:
        print(''.join([sql1,tables_string,sql2]), file=f)

    # history tables    
    with open(out0Loc,'a') as f:
        print(''.join([sql3,tables_string,sql2]), file=f)
        
#MS SQL GET PK MAKER
def sql_get_pk_maker():
    with open(sql4Loc,'r') as string:
        sql4 = string.read()

    with open(out00Loc,'w') as f:
        print(''.join([sql4,tables_string,")order by 1"]), file=f)

#MS SQL TABLE INFO MAKER
def sql_get_table_info_maker():
    with open(sql5Loc,'r') as string:
        sql5 = string.read()
    with open(sql6Loc,'r') as string:
        sql6 = string.read()
      
    with open(out000Loc,'w') as f:
        print(''.join([sql5,tables_string,sql6]), file=f)

sql_get_ddl_maker()
sql_get_pk_maker()
sql_get_table_info_maker()