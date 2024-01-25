## config maker
## jessica hoffman
##1/17/24

from config import tablenamesLoc, s1Loc, s2Loc,s3Loc,s4Loc,s5Loc,s6Loc,s7Loc,s8Loc ,s9Loc,s10Loc,s11Loc,s12Loc
from config import out1Loc,out2Loc,out3Loc,out4Loc

#READ IN CAMELCASE TABLE NAMES FROM ON PREM SQL SERVER
tn = open(tablenamesLoc,'r')
tables = [line.rstrip() for line in tn]
tn.close()

#DEV BCPIO CONFIG ENTRIES
def dev_bcp_io_config_maker():
    with open(s1Loc,'r') as string:
        s1 = string.read()
    with open(s2Loc,'r') as string:
        s2 = string.read()
    with open(s3Loc,'r') as string:
        s3 = string.read()

    with open(out1Loc,'w') as f:
        for t in tables:
            print(''.join([s1,t,s2,t,s3]), file=f)

#DEV T FILE LOAD CONFIG ENTRIES
def dev_t_file_load_config_maker():
    with open(s4Loc,'r') as string:
        s4 = string.read()
    with open(s5Loc,'r') as string:
        s5 = string.read()
    with open(s6Loc,'r') as string:
        s6 = string.read()

    with open(out2Loc,'w') as f:
        for t in tables:
            print(''.join([s4,t,s5,"T_",t.upper(),s6]), file=f)

#PROD BCPIO CONFIG ENTRIES
def prod_bcp_io_config_maker():
    with open(s7Loc,'r') as string:
        s7 = string.read()
    with open(s8Loc,'r') as string:
        s8 = string.read()
    with open(s9Loc,'r') as string:
        s9 = string.read()

    with open(out3Loc,'w') as f:
        for t in tables:
            print(''.join([s7,t,s8,t,s9]), file=f)

#PROD T FILE LOAD CONFIG ENTRIES
def prod_t_file_load_config_maker():
    with open(s10Loc,'r') as string:
        s10 = string.read()
    with open(s11Loc,'r') as string:
        s11 = string.read()
    with open(s12Loc,'r') as string:
        s12 = string.read()

    with open(out4Loc,'w') as f:
        for t in tables:
            print(''.join([s10,t,s11,"T_",t.upper(),s12]), file=f)

dev_bcp_io_config_maker()
dev_t_file_load_config_maker()
prod_bcp_io_config_maker()
prod_t_file_load_config_maker()