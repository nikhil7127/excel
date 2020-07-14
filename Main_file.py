import pandas as p 
import time as t
import os
i=0
j=0
z=0
tot_sbi =0
tot_other =0
tot_sbi1 =0
tot_other1 =0

files = input("Enter file name(only excel files) : ")
try:
    os.remove("SBI_ACCOUNTS.txt")
    os.remove("OTHER_ACCOUNTS.txt")
    os.remove("TOTAL.txt")
except:
    pass
print(t.clock())
k = p.read_excel(f"{files}.xlsx")
#k = p.read_excel(f"another.xlsx")
lens = len(k)
for a in range(0,lens):
    let = k['BNK_IFSC'][a].split("0")
    let = let[0]
    if(let == "SBIN"):
        if(i==0):
            with open("SBI_ACCOUNTS.txt","a") as n:
                n.write("""
APEPDCL - Sri V S RAMACHANDRA MURTHY
EE O BHIMAVARAM
TRANSACTIONS ANDHRA BANK - 04/07/2020 - EMPLOYEES
--------------------------------------------------------------------------------
Sl.    IFSC CODE         Account           Amount          Name 
--------------------------------------------------------------------------------\n""")
        i = i+1
        ask = k['CR_AMOUNT'][a]
        tot_sbi = tot_sbi+1
        tot_sbi1 = tot_sbi1+ask
        with open("SBI_ACCOUNTS.txt","a") as n:
    
            ask = str(ask)[::-1]
            final = ""
            for aa in range(0,8):
                if (aa >= len(ask)):
                    final = final + " "
                else:
                    final = final+ask[aa]
            final = final[::-1]
            try:
                n.write(f"{k['E_P'][a]}     {k['BNK_IFSC'][a]}       {k['EMP_AC'][a]}\t{final}.00")
                n.write(f"\t {k['EMP_NAME'][a]}\n")
            except:
                n.write(f"E     {k['BNK_IFSC'][a]}       {k['EMP_AC'][a]}\t{final}.00")
                n.write(f"\t {k['EMP_NAME'][a]}\n")
            n.close()
       
    else:
        if(j==0):
            with open("OTHER_ACCOUNTS.txt","a") as o:
                o.write("""
APEPDCL - Sri V S RAMACHANDRA MURTHY
EE O BHIMAVARAM
TRANSACTIONS ANDHRA BANK - 04/07/2020 - EMPLOYEES
--------------------------------------------------------------------------------
Sl.    IFSC CODE         Account           Amount          Name 
--------------------------------------------------------------------------------\n""")
        j = i+1
        ask1 = k['CR_AMOUNT'][a]
        tot_other = tot_other+1
        tot_other1 = tot_other1+ask1
        with open("OTHER_ACCOUNTS.txt","a") as o:
            ask1 = str(ask1)[::-1]
            final1 = ""
            for aa1 in range(0,8):
                if (aa1 >= len(ask1)):
                    final1 = final1 + " "
                else:
                    final1 = final1+ask1[aa1]
            final1 = final1[::-1]
            try:
                o.write(f"{k['E_P'][a]}     {k['BNK_IFSC'][a]}       {k['EMP_AC'][a]}\t{final1}.00")
                o.write(f"\t {k['EMP_NAME'][a]}\n")
            except:
                o.write(f"E     {k['BNK_IFSC'][a]}       {k['EMP_AC'][a]}\t{final1}.00")
                o.write(f"\t {k['EMP_NAME'][a]}\n")
            o.close()

with open("SBI_ACCOUNTS.txt","a") as n:
    n.write("--------------------------------------------------------------------------------\n")
    n.write(f"                            Total         {tot_sbi1}.00                            \n")
    n.write("--------------------------------------------------------------------------------\n")
    n.close()
with open("OTHER_ACCOUNTS.txt","a") as o:
    o.write(f"--------------------------------------------------------------------------------\n")
    o.write(f"                            Total         {tot_other1}.00                           \n")
    o.write("--------------------------------------------------------------------------------\n")
    o.close()
if(z==0):
    with open("TOTAL.txt","a") as t:
        t.write("""
APEPDCL - Sri V S RAMACHANDRA MURTHY
EE O BHIMAVARAM
    SUMMARY OF TRANSACTIONS - 04/07/2020 - EMPLOYEES
--------------------------------------------------------------------------------
 BANK      NUMBER        AMOUNT         FILES GENERATED
--------------------------------------------------------------------------------\n""")
        
        t.write(f" SBI         {tot_sbi}          {tot_sbi1}.00")
        t.write("\tSBI_ACCOUNTS.txt")
        t.write("\n")
        t.write("\n")
        t.write(f" OTHER       {tot_other}          {tot_other1}.00")
        t.write("\t        OTHER_ACCOUNTS.txt")
        t.write("\n")
        t.write(f"""--------------------------------------------------------------------------------
 TOTAL       {tot_sbi+tot_other} \t {tot_sbi1+tot_other1}.00
--------------------------------------------------------------------------------""")
print(tot_sbi1,tot_other1)
