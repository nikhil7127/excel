import pandas as p 
import os
i=0
j=0
z=0
tot_sbi =0
tot_other =0
tot_sbi1 =0
tot_other1 =0

files = input("Enter file name(only excel files) : ")
date  = input("Enter date(dd-mm-year)")
try:
    os.remove(f"SBI_ACCOUNTS_{date}.txt")
    os.remove(f"OTHER_ACCOUNTS_{date}.txt")
    os.remove(f"TOTAL_{date}.txt")
except:
    pass
k = p.read_excel(f"{files}.xlsx")
lens = len(k)
for a in range(0,lens):
    let = k['BNK_IFSC'][a].split("0")
    let = let[0]
    if(let == "SBIN"):
        if(i==0):
            with open(f"SBI_ACCOUNTS_{date}.txt","a") as n:
                n.write("""APEPDCL - Sri V S RAMACHANDRA MURTHY
EE O BHIMAVARAM
TRANSACTIONS ANDHRA BANK - 04/07/2020 - EMPLOYEES
--------------------------------------------------------------------------------
Sl.    IFSC CODE         Account           Amount          Name 
--------------------------------------------------------------------------------\n""")
        i = i+1
        ask = k['CR_AMOUNT'][a]
        tot_sbi = tot_sbi+1
        tot_sbi1 = tot_sbi1+ask
        with open(f"SBI_ACCOUNTS_{date}.txt","a") as n:
    
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
            with open(f"OTHER_ACCOUNTS_{date}.txt","a") as o:
                o.write("""APEPDCL - Sri V S RAMACHANDRA MURTHY
EE O BHIMAVARAM
TRANSACTIONS ANDHRA BANK - 04/07/2020 - EMPLOYEES
--------------------------------------------------------------------------------
Sl.    IFSC CODE         Account           Amount          Name 
--------------------------------------------------------------------------------\n""")
        j = i+1
        ask1 = k['CR_AMOUNT'][a]
        tot_other = tot_other+1
        tot_other1 = tot_other1+ask1
        with open(f"OTHER_ACCOUNTS_{date}.txt","a") as o:
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

with open(f"SBI_ACCOUNTS_{date}.txt","a") as n:
    n.write("--------------------------------------------------------------------------------\n")
    n.write(f"                            Total         {tot_sbi1}.00                            \n")
    n.write("--------------------------------------------------------------------------------\n")
    n.close()
with open(f"OTHER_ACCOUNTS_{date}.txt","a") as o:
    o.write(f"--------------------------------------------------------------------------------\n")
    o.write(f"                            Total         {tot_other1}.00                           \n")
    o.write("--------------------------------------------------------------------------------\n")
    o.close()
if(z==0):
    with open(f"TOTAL_{date}.txt","a") as t:
        t.write("""APEPDCL - Sri V S RAMACHANDRA MURTHY
EE O BHIMAVARAM
SUMMARY OF TRANSACTIONS - 04/07/2020 - EMPLOYEES
--------------------------------------------------------------------------------
 BANK\t\tNUMBER\t\tAMOUNT\t\tFILES GENERATED
--------------------------------------------------------------------------------\n""")
        tot_c = str(tot_sbi1)[::-1]
        tot_c1 = str(tot_other1)[::-1]
        tot_count =""
        tot_count1 =""
        for asa in range(0,10):
            if(asa>= len(tot_c)):
                tot_count = tot_count+" "
            else:
                tot_count = tot_count+tot_c[asa]
        for asa1 in range(0,10):
            if(asa1>= len(tot_c1)):
                tot_count1 = tot_count1+" "
            else:
                tot_count1 = tot_count1+tot_c1[asa1]
        tot_count = tot_count[::-1]
        tot_count1 = tot_count1[::-1]
        t.write(f" SBI\t\t{tot_sbi}\t{tot_count}.00")
        t.write("\t\tSBI_ACCOUNTS.txt")
        t.write("\n")
        t.write("\n")
        t.write(f" OTHER\t\t{tot_other}\t{tot_count1}.00")
        t.write("\t\tOTHER_ACCOUNTS.txt")
        t.write("\n")
        t.write(f"""--------------------------------------------------------------------------------
 TOTAL\t\t{tot_sbi+tot_other}\t   {tot_sbi1+tot_other1}.00
--------------------------------------------------------------------------------""")

