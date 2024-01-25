## Snowflake DDL maker
## jessica hoffman
##1/19/24
##  This code inserts pks into ddl statements created in sql

from config import cLoc,chLoc,pkLoc,ddlLoc

with open(cLoc,'r') as create_base:
    c = create_base.read()

with open(chLoc,'r') as create_history:
    ch = create_history.read()

with open(pkLoc,'r') as pkfile:
    pks = [line.rstrip() for line in pkfile]

def findall(text, sub):
    return[
        index 
        for index in range(len(text) - len(sub) + 1)
        if text[index:].startswith(sub)]        

def get_indices(text,sub):
    indices = (findall(text,sub))
    return indices

def ddl_maker():
    # base tables
    cnew = ''
    i=-13
    indices = get_indices(c,'PRIMARY KEY ()')

    for idx in indices:
        start = i+13
        end = int(idx)+13
        try:
            cnew = cnew + c[start:end] + pks[indices.index(idx)]
        except Exception as error:
            print(f"an exception occurred at idx #= {indices.index(idx)} for {error}")
            break
        i=int(idx)
 
    with open(ddlLoc,'w') as f:
        print(''.join([cnew,c[i+13:],'\n\n\n']), file=f)

    # history tables
    chnew = ''
    i=-14
    indices = get_indices(ch,'PRIMARY KEY ( ,EDP_BEG_EFF_DT)')
    # print(f"length of pks is {len(pks)} and length of indices is {len(indices)}")
    for idx in indices:
        start = i+14
        end = int(idx)+13
        try:
            chnew = chnew + ch[start:end] + pks[indices.index(idx)]
        except Exception as error:
            print(f"an exception occurred at idx = {indices.index(idx)} and pk = {pks[indices.index(idx)]} for {error}")
            break
        i=int(idx)

    with open(ddlLoc,'a') as f:
        print(''.join([chnew,ch[i+14:]]), file=f)

ddl_maker()

