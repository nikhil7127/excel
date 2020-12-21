import pandas as p 
import numpy as n
import time as t
import os

# required Lists
sbi_accounts = []
and_accounts =[]
other_accounts = []

try:
    data = p.concat([p.read_excel('./main.xlsx',sheet_name=sheet) for sheet in p.ExcelFile("main.xlsx").sheet_names])
except:
    data = p.concat([p.read_excel("./main.xls",sheet_name=sheet) for sheet in p.ExcelFile("main.xlsx").sheet_names])

if "E_P" in data.columns:
    data = data.drop(columns=["E_P"])
if "Y_N" in data.columns:
    data = data.drop(columns=["Y_N"])
if "EMP_ADD" in data.columns:
    data = data.drop(columns=["EMP_ADD"])
for index,df in data.iterrows():
    if "SBIN" in df["BNK_IFSC"]:
        sbi_accounts.append(df)
    elif "ANDB" in df["BNK_IFSC"]:
        and_accounts.append(df)
    else:
        other_accounts.append(df)



sbi_name = [sbi.EMP_NAME for sbi in sbi_accounts]
sbi_ifsc = [sbi.BNK_IFSC for sbi in sbi_accounts]
sbi_ac = [str(sbi.EMP_AC) for sbi in sbi_accounts]
sbi_amount = [int(sbi.CR_AMOUNT) for sbi in sbi_accounts]

ab_name = [ab.EMP_NAME for ab in and_accounts]
ab_ifsc = [ab.BNK_IFSC for ab in and_accounts]
ab_ac = [str(ab.EMP_AC) for ab in and_accounts]
ab_amount = [int(ab.CR_AMOUNT) for ab in and_accounts]

oth_name = [other.EMP_NAME for other in other_accounts]
oth_ifsc = [other.BNK_IFSC for other in other_accounts]
oth_ac = [str(other.EMP_AC) for other in other_accounts]
oth_amount = [int(other.CR_AMOUNT) for other in other_accounts] 

sbi_data = p.DataFrame({"IFSC Code": sbi_ifsc,"Account Numbers":sbi_ac,"Amount":sbi_amount,"Name":sbi_name})
other_data = p.DataFrame({"IFSC Code": oth_ifsc,"Account Numbers":oth_ac,"Amount":oth_amount,"Name":oth_name})
andhra_data = p.DataFrame({"IFSC Code": ab_ifsc,"Account Numbers":ab_ac,"Amount":ab_amount,"Name":ab_name})

#csv Files
sbi_data.to_excel("Sbi_Accounts.xlsx",index=False)
other_data = other_data.sort_values(by="IFSC Code")
other_data.to_excel("Other_Accounts.xlsx",index=False)
andhra_data.to_excel("Andhra_Accounts.xlsx",index=False)

oth_max = len(str(max(int(other.EMP_AC) for other in other_accounts)))

with open("andhra_Accounts.txt","w") as r:
    r.write("APEPDCL - Sri V S RAMACHANDRA MURTHY\nEE O BHIMAVARAM\nTRANSACTIONS ANDHRA BANK - 04/07/2020 - EMPLOYEES\n")
    r.write(f"{'-'*100}\nSl.{' '*6}IFSC CODE{' '*8}Account{' '*11}Amount{' '*13}Name \n{'-'*100}\n")
    for index,a in enumerate(andhra_data.values):
        r.write(f"{str(index+1).rjust(3,' ')}    {a[0]}      {str(a[1]).rjust(15,'0')}       {str(a[2]).rjust(len(str(max(ab_amount))),' ')}.00         {a[3]}\n")
    r.write(f"{'-'*100}\n")
    r.write(f"{' '*25} TOTAL{' '*10}{sum(ab_amount)}.00 {' '*30}\n")
    r.write(f"{'-'*100}\n")

with open("sbi_Accounts.txt","w") as r:
    r.write("APEPDCL - Sri V S RAMACHANDRA MURTHY\nEE O BHIMAVARAM\nTRANSACTIONS SBI BANK - 04/07/2020 - EMPLOYEES\n")
    r.write(f"{'-'*100}\nSl.{' '*6}IFSC CODE{' '*8}Account{' '*11}Amount{' '*13}Name \n{'-'*100}\n")
    for index,a in enumerate(sbi_data.values):
        r.write(f"{str(index+1).rjust(3,' ')}    {a[0]}      {str(a[1])}       {str(a[2]).rjust(len(str(max(sbi_amount))),' ')}.00         {a[3]}\n")
    r.write(f"{'-'*100}\n")
    r.write(f"{' '*25} TOTAL{' '*10}{sum(sbi_amount)}.00 {' '*30}\n")
    r.write(f"{'-'*100}\n")

with open("other_Accounts.txt","w") as r:
    r.write("APEPDCL - Sri V S RAMACHANDRA MURTHY\nEE O BHIMAVARAM\nTRANSACTIONS OTHER BANK - 04/07/2020 - EMPLOYEES\n")
    r.write(f"{'-'*100}\nSl.{' '*6}IFSC CODE{' '*8}Account{' '*11}Amount{' '*13}Name \n{'-'*100}\n")
    for index,a in enumerate(other_data.sort_values(by="IFSC Code").values):
        r.write(f"{str(index+1).rjust(3,' ')}    {str(a[0])}      {str(a[1]).ljust(oth_max,' ')}       {str(a[2]).rjust(len(str(max(oth_amount))),' ')}.00         {a[3]}\n")
    r.write(f"{'-'*100}\n")
    r.write(f"{' '*25} TOTAL{' '*10}{sum(oth_amount)}.00 {' '*30}\n")
    r.write(f"{'-'*100}\n")

with open("total.txt","w") as r:
    r.write("APEPDCL - Sri V S RAMACHANDRA MURTHY\nEE O BHIMAVARAM\nTRANSACTIONS OTHER BANK - 04/07/2020 - EMPLOYEES\n")
    r.write(f"{'-'*70}\n BANK        NUMBER        AMOUNT          FILE GENERATED\n{'-'*70}\n")
    r.write(f"   SBI         {str(len(sbi_accounts)).rjust(3,' ')}        {sum(sbi_amount)}.00        sbi_Accounts.txt\n")
    r.write("\n")
    r.write(f"ANDHRA         {str(len(and_accounts)).rjust(3,' ')}        {sum(ab_amount)}.00        andhra_Accounts.txt\n")
    r.write("\n")
    r.write(f" OTHER         {str(len(other_accounts)).rjust(3,' ')}        {sum(oth_amount)}.00        Other_Accounts.txt\n")
    r.write(f"{'-'*70}\n")
    r.write(f"TOTAL        {len(sbi_accounts)+len(other_accounts)}        {sum(sbi_amount)+sum(oth_amount)}.00\n")
    r.write(f"{'-'*70}\n")


    
