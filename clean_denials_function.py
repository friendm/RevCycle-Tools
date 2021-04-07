subset_list=[]
denial_delimeter='_'

def clean_denials(x):
    code_list = x.split(denial_delimeter)
    contains_denial = True
    new_list = []
    for x in code_list:
        if True:
        #if x in subset_list:
            contains_denial = True
            new_list.append(x)
    output = ""
    if contains_denial:
        s = set(new_list)
        finalized_list = []
        for x in s:
            finalized_list.append(x)
        master_list = sorted(finalized_list, reverse=True)
        for y in master_list:
            output = y + "_" + output
        return output