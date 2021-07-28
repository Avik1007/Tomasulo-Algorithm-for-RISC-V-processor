from bitstring import BitArray
def load(val_rs1,imm):
    val_rs1=RAT[val_rs1]
    value=mem[val_rs1+(imm*4)]
    return value

def div(val_rs1,val_rs2):
    value=val_rs1/val_rs2
    return value
def mul(val_rs1,val_rs2):
    value=val_rs1*val_rs2
    return value
def add(val_rs1,val_rs2):
    value=val_rs1+val_rs2
    return value
def sub(val_rs1,val_rs2):
    value=val_rs1-val_rs2
    return value    
def calc_issue_cycle(cycle,instruction_type,add_sub_rs,mul_div_rs,load_store_rs,instrs_table):
    if(instruction_type == "ADD" or instruction_type == "SUB"):
        if(len(add_sub_rs)<=3):
            issue_cycle=cycle
        else:
            dest_tag1=add_sub_rs[0][2]
            dest_tag2=add_sub_rs[1][2]
            dest_tag3=add_sub_rs[2][2]
            dest_tag1=int(dest_tag1[3]) -1
            dest_tag2=int(dest_tag2[3]) -1
            dest_tag3=int(dest_tag3[3]) -1
            iss_cyc1=instrs_table[dest_tag1][1]
            iss_cyc2=instrs_table[dest_tag2][1]
            iss_cyc3=instrs_table[dest_tag3][1]
            l=[iss_cyc1,iss_cyc2,iss_cyc3]
            issue_cycle=min(l) +1 
            pos=l.index(min(l))
            del add_sub_rs[pos]
            ##### FOR TOMADULO EXAMPLE QUESTION
            # dest_tag1=add_sub_rs[0][2]
            # dest_tag1=int(dest_tag1[3]) -1
            # iss_cyc1=instrs_table[dest_tag1][1]
            # issue_cycle=iss_cyc1 +1 
            # del add_sub_rs[0]
    elif(instruction_type == "MUL" or instruction_type == "DIV"):
        if(len(mul_div_rs)<=2):
            issue_cycle=cycle
        else:
            dest_tag1=mul_div_rs[0][2]
            dest_tag2=mul_div_rs[1][2]
            dest_tag1=int(dest_tag1[3]) -1
            dest_tag2=int(dest_tag2[3]) -1
            iss_cyc1=instrs_table[dest_tag1][1]
            iss_cyc2=instrs_table[dest_tag2][1]
            l=[iss_cyc1,iss_cyc2]
            issue_cycle=min(l) +1 
            pos=l.index(min(l))
            del mul_div_rs[pos]        
    elif(instruction_type == "LOAD"):
        if(len(load_store_rs)<=3):
            issue_cycle=cycle
        else:
            dest_tag1=load_store_rs[0][2]
            dest_tag2=load_store_rs[1][2]
            dest_tag3=load_store_rs[2][2]
            dest_tag1=int(dest_tag1[3]) -1
            dest_tag2=int(dest_tag2[3]) -1
            dest_tag3=int(dest_tag3[3]) -1
            iss_cyc1=instrs_table[dest_tag1][1]
            iss_cyc2=instrs_table[dest_tag2][1]
            iss_cyc3=instrs_table[dest_tag3][1]
            l=[iss_cyc1,iss_cyc2,iss_cyc3]
            issue_cycle=min(l) +1 
            pos=l.index(min(l))
            del load_store_rs[pos]
    return issue_cycle

def cycle_calc(instruction_type,cycle,issue_cycle,instrs_table_entry,exec_cycle): 
    # Calculating all the cycle values. Issue to RS, Execute start/Address calculation for LD,Execute/Memory access complete,Write to CDB,Commit
    if(instruction_type=="LOAD"):
        issue_to_RS=issue_cycle
        Execute_start_AddresscalculationforLD= exec_cycle
        Execute_Memoryaccess_complete=exec_cycle+5-1
        Write_to_CDB=Execute_Memoryaccess_complete+1
        if(cycle==1):
            commit=Write_to_CDB+1
        elif ((Write_to_CDB+1)<instrs_table[cycle-2][4]):
            commit=instrs_table[cycle-2][4]+1  
        elif((Write_to_CDB+1)>instrs_table[cycle-2][4]):
            commit=Write_to_CDB+1          
        cycle=cycle+1
        instrs_table.append([issue_to_RS,Execute_start_AddresscalculationforLD,Execute_Memoryaccess_complete,Write_to_CDB,commit])
        print("Instruction Table: ",instrs_table)
        instrs_table_entry=instrs_table_entry+1
    elif(instruction_type=="DIV"):
        issue_to_RS=issue_cycle
        Execute_start_AddresscalculationforLD= exec_cycle
        Execute_Memoryaccess_complete=exec_cycle+40-1
        Write_to_CDB=Execute_Memoryaccess_complete+1
        if(cycle==1):
            commit=Write_to_CDB+1
        elif ((Write_to_CDB+1)<instrs_table[cycle-2][4]):
            commit=instrs_table[cycle-2][4]+1  
        elif((Write_to_CDB+1)>instrs_table[cycle-2][4]):
            commit=Write_to_CDB+1 
        cycle=cycle+1
        instrs_table.append([issue_to_RS,Execute_start_AddresscalculationforLD,Execute_Memoryaccess_complete,Write_to_CDB,commit])
        print("Instruction Table: ",instrs_table)
        instrs_table_entry=instrs_table_entry+1  
    elif(instruction_type=="MUL"):
        issue_to_RS=issue_cycle
        Execute_start_AddresscalculationforLD= exec_cycle
        Execute_Memoryaccess_complete=exec_cycle+10-1
        Write_to_CDB=Execute_Memoryaccess_complete+1
        if(cycle==1):
            commit=Write_to_CDB+1
        elif ((Write_to_CDB+1)<instrs_table[cycle-2][4]):
            commit=instrs_table[cycle-2][4]+1  
        elif((Write_to_CDB+1)>instrs_table[cycle-2][4]):
            commit=Write_to_CDB+1 
        cycle=cycle+1
        instrs_table.append([issue_to_RS,Execute_start_AddresscalculationforLD,Execute_Memoryaccess_complete,Write_to_CDB,commit])
        print("Instruction Table: ",instrs_table)
        instrs_table_entry=instrs_table_entry+1  
    elif(instruction_type=="ADD" or instruction_type=="SUB"):
        issue_to_RS=issue_cycle
        Execute_start_AddresscalculationforLD= exec_cycle
        Execute_Memoryaccess_complete=exec_cycle+1-1
        Write_to_CDB=Execute_Memoryaccess_complete+1
        if(cycle==1):
            commit=Write_to_CDB+1
        elif ((Write_to_CDB+1)<instrs_table[cycle-2][4]):
            commit=instrs_table[cycle-2][4]+1  
        elif((Write_to_CDB+1)>instrs_table[cycle-2][4]):
            commit=Write_to_CDB+1 
        cycle=cycle+1
        instrs_table.append([issue_to_RS,Execute_start_AddresscalculationforLD,Execute_Memoryaccess_complete,Write_to_CDB,commit])
        print("Instruction Table: ",instrs_table)
        instrs_table_entry=instrs_table_entry+1

    return cycle    


def ROB(instruction,cycle,rob_entry,robtable,instrs_table,instrs_table_entry,add_sub_rs,add_sub_rs_entry,mul_div_rs,mul_div_rs_entry,load_store_rs,load_store_rs_entry):
    if(instruction[25:32]=='0000011'): #Decoding 
        instruction_type="LOAD"
        rs1 = BitArray(bin=instruction[12:17]).uint
        rd= BitArray(bin=instruction[20:25]).uint
        imm= BitArray(bin=instruction[0:12]).uint
        robnum="ROB"+str(rob_entry)
        if(load_store_rs_entry<=3): # load store reservation station of size 3
            busy=1
            load_store_rs.append([instruction,busy,robnum,imm,rs1]) #load store RS entry
            load_store_rs_entry=load_store_rs_entry+1
            print("load_store_rs: ",load_store_rs)
            issue_cycle=calc_issue_cycle(cycle,instruction_type,add_sub_rs,mul_div_rs,load_store_rs,instrs_table) #issue cycle calculation
            if(isinstance(RAT[rs1-1], str) ): #Checking if RAT entry has ROB entry as data-> calculating execute cycle and source register values accordingly 
                its_robentry=RAT[rs1-1]
                robnumber=int(its_robentry[3])
                val_rs1=robtable[robnumber-1][3]
                exec_cycle=instrs_table[robnumber-1][3] + 1     
                           
            else:
                val_rs1=rs1-1   
                exec_cycle=cycle+1          
                
        RAT[rd-1]=robnum #updating/renaming RAT with ROB number entry
        print("RAT: ",RAT)
        cycle=cycle_calc(instruction_type,cycle,issue_cycle,instrs_table_entry,exec_cycle) #instruction table cycle calculations
        value=load(val_rs1,imm) #value of the operation calculation
        load_store_rs_entry=load_store_rs_entry-1 
        robtable.append([robnum,instruction_type,rd,value]) # ROB table entry
        print("ROB table: ",robtable)
        print(" \n")
        rob_entry=rob_entry+1
    elif(instruction[25:32]=='0110011'): 
        if(instruction[17:20]=='100' and instruction[0:7]=='0000001'): #Decoding 
            instruction_type="DIV"
            rs2= BitArray(bin=instruction[7:12]).uint
            rs1 = BitArray(bin=instruction[12:17]).uint
            rd= BitArray(bin=instruction[20:25]).uint
            robnum="ROB"+str(rob_entry)
            if(mul_div_rs_entry<=2):
                busy=1
                mul_div_rs.append([instruction,busy,robnum,rs1,rs2,RAT[rs1-1],RAT[rs2-1]])
                mul_div_rs_entry=mul_div_rs_entry+1
                print("mul_div_rs: ",mul_div_rs)
                issue_cycle=calc_issue_cycle(cycle,instruction_type,add_sub_rs,mul_div_rs,load_store_rs,instrs_table) #issue cycle calculation
                if(isinstance(RAT[rs1-1], str) or isinstance(RAT[rs2-1], str) ): #if destination is a rob entry then get the value from robtable...... also setting the execute start cycle value
                    if(isinstance(RAT[rs1-1], str)):
                        if(isinstance(RAT[rs2-1], str)):
                            its_robentry1=RAT[rs1-1]
                            robnumber1=int(its_robentry1[3])
                            val_rs1=robtable[robnumber1-1][3]
                            exec_cycle1=instrs_table[robnumber1-1][3]
                            its_robentry2=RAT[rs2-1]
                            robnumber2=int(its_robentry2[3])
                            val_rs2=robtable[robnumber2-1][3]
                            exec_cycle2=instrs_table[robnumber2-1][3]
                            exec_cycle=max(exec_cycle1,exec_cycle2) + 1
                        else:
                            its_robentry=RAT[rs1-1]
                            robnumber=int(its_robentry[3])
                            val_rs1=robtable[robnumber-1][3]
                            val_rs2=RAT[rs2-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1
                    elif(isinstance(RAT[rs2-1], str)):  
                            its_robentry=RAT[rs2-1]
                            robnumber=int(its_robentry[3])
                            val_rs2=robtable[robnumber-1][3]
                            val_rs1=RAT[rs1-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1 
                else:
                    val_rs1=RAT[rs1-1]
                    val_rs2=RAT[rs2-1]  
                    exec_cycle=cycle+1          
                
            RAT[rd-1]=robnum #updating/renaming RAT with ROB number entry
            print("RAT: ",RAT)
            cycle=cycle_calc(instruction_type,cycle,issue_cycle,instrs_table_entry,exec_cycle) #instruction table cycle calculations
            value=div(val_rs1,val_rs2) #value of the operation calculation
            mul_div_rs_entry=mul_div_rs_entry-1
            robtable.append([robnum,instruction_type,rd,value]) # ROB table entry
            print("ROB table: ",robtable)
            print(" \n")
            rob_entry=rob_entry+1 
        elif(instruction[17:20]=='000' and instruction[0:7]=='0000001'):
            instruction_type="MUL"
            rs2= BitArray(bin=instruction[7:12]).uint
            rs1 = BitArray(bin=instruction[12:17]).uint
            rd= BitArray(bin=instruction[20:25]).uint
            robnum="ROB"+str(rob_entry)
            if(mul_div_rs_entry<=2):
                busy=1
                mul_div_rs.append([instruction,busy,robnum,rs1,rs2,RAT[rs1-1],RAT[rs2-1]])
                mul_div_rs_entry=mul_div_rs_entry+1
                print("mul_div_rs: ",mul_div_rs)
                issue_cycle=calc_issue_cycle(cycle,instruction_type,add_sub_rs,mul_div_rs,load_store_rs,instrs_table)
                if(isinstance(RAT[rs1-1], str) or isinstance(RAT[rs2-1], str) ):
                    if(isinstance(RAT[rs1-1], str)):
                        if(isinstance(RAT[rs2-1], str)):
                            its_robentry1=RAT[rs1-1]
                            robnumber1=int(its_robentry1[3])
                            val_rs1=robtable[robnumber1-1][3]
                            exec_cycle1=instrs_table[robnumber1-1][3]
                            its_robentry2=RAT[rs2-1]
                            robnumber2=int(its_robentry2[3])
                            val_rs2=robtable[robnumber2-1][3]
                            exec_cycle2=instrs_table[robnumber2-1][3]
                            exec_cycle=max(exec_cycle1,exec_cycle2) + 1
                            
                        else:
                            its_robentry=RAT[rs1-1]
                            robnumber=int(its_robentry[3])
                            val_rs1=robtable[robnumber-1][3]
                            val_rs2=RAT[rs2-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1
                    elif(isinstance(RAT[rs2-1], str)):  
                            its_robentry=RAT[rs2-1]
                            robnumber=int(its_robentry[3])
                            val_rs2=robtable[robnumber-1][3]
                            val_rs1=RAT[rs1-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1 
                else:
                    val_rs1=RAT[rs1-1]
                    val_rs2=RAT[rs2-1]  
                    exec_cycle=cycle+1          
                
            RAT[rd-1]=robnum #updating/renaming RAT with ROB number entry
            print("RAT: ",RAT)
            cycle=cycle_calc(instruction_type,cycle,issue_cycle,instrs_table_entry,exec_cycle) #instruction table cycle calculations
            value=mul(val_rs1,val_rs2) #value of the operation calculation
            mul_div_rs_entry=mul_div_rs_entry-1
            robtable.append([robnum,instruction_type,rd,value]) # ROB table entry
            print("ROB table: ",robtable)
            print(" \n")
            rob_entry=rob_entry+1 
        elif(instruction[17:20]=='000' and instruction[0:7]=='0000000'):
            instruction_type="ADD"
            rs2= BitArray(bin=instruction[7:12]).uint
            rs1 = BitArray(bin=instruction[12:17]).uint
            rd= BitArray(bin=instruction[20:25]).uint
            robnum="ROB"+str(rob_entry)
            if(add_sub_rs_entry<=2):
                busy=1
                add_sub_rs.append([instruction,busy,robnum,rs1,rs2,RAT[rs1-1],RAT[rs2-1]])
                add_sub_rs_entry=add_sub_rs_entry+1
                print("add_sub_rs: ",add_sub_rs)
                issue_cycle=calc_issue_cycle(cycle,instruction_type,add_sub_rs,mul_div_rs,load_store_rs,instrs_table)
                if(isinstance(RAT[rs1-1], str) or isinstance(RAT[rs2-1], str) ):
                    if(isinstance(RAT[rs1-1], str)):
                        if(isinstance(RAT[rs2-1], str)):
                            its_robentry1=RAT[rs1-1]
                            robnumber1=int(its_robentry1[3])
                            val_rs1=robtable[robnumber1-1][3]
                            exec_cycle1=instrs_table[robnumber1-1][3]
                            its_robentry2=RAT[rs2-1]
                            robnumber2=int(its_robentry2[3])
                            val_rs2=robtable[robnumber2-1][3]
                            exec_cycle2=instrs_table[robnumber2-1][3]
                            exec_cycle=max(exec_cycle1,exec_cycle2) + 1
                        else:
                            its_robentry=RAT[rs1-1]
                            robnumber=int(its_robentry[3])
                            val_rs1=robtable[robnumber-1][3]
                            val_rs2=RAT[rs2-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1
                    elif(isinstance(RAT[rs2-1], str)):  
                            its_robentry=RAT[rs2-1]
                            robnumber=int(its_robentry[3])
                            val_rs2=robtable[robnumber-1][3]
                            val_rs1=RAT[rs1-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1  
                else:
                    val_rs1=RAT[rs1-1]
                    val_rs2=RAT[rs2-1]  
                    exec_cycle=cycle+1          
                
            RAT[rd-1]=robnum #updating/renaming RAT with ROB number entry
            print("RAT: ",RAT)
            cycle=cycle_calc(instruction_type,cycle,issue_cycle,instrs_table_entry,exec_cycle) #instruction table cycle calculations
            value=add(val_rs1,val_rs2) #value of the operation calculation
            add_sub_rs_entry=add_sub_rs_entry-1
            robtable.append([robnum,instruction_type,rd,value]) # ROB table entry
            print("ROB table: ",robtable)
            print(" \n")
            rob_entry=rob_entry+1 
        elif(instruction[17:20]=='000' and instruction[0:7]=='0100000'):
            instruction_type="SUB"
            rs2= BitArray(bin=instruction[7:12]).uint
            rs1 = BitArray(bin=instruction[12:17]).uint
            rd= BitArray(bin=instruction[20:25]).uint
            robnum="ROB"+str(rob_entry)
            if(add_sub_rs_entry<=2):
                busy=1
                add_sub_rs.append([instruction,busy,robnum,rs1,rs2,RAT[rs1-1],RAT[rs2-1]])
                add_sub_rs_entry=add_sub_rs_entry+1
                print("add_sub_rs: ",add_sub_rs)
                issue_cycle=calc_issue_cycle(cycle,instruction_type,add_sub_rs,mul_div_rs,load_store_rs,instrs_table)
                if(isinstance(RAT[rs1-1], str) or isinstance(RAT[rs2-1], str) ):
                    if(isinstance(RAT[rs1-1], str)):
                        if(isinstance(RAT[rs2-1], str)):
                            its_robentry1=RAT[rs1-1]
                            robnumber1=int(its_robentry1[3])
                            val_rs1=robtable[robnumber1-1][3]
                            exec_cycle1=instrs_table[robnumber1-1][3]
                            its_robentry2=RAT[rs2-1]
                            robnumber2=int(its_robentry2[3])
                            val_rs2=robtable[robnumber2-1][3]
                            exec_cycle2=instrs_table[robnumber2-1][3]
                            exec_cycle=max(exec_cycle1,exec_cycle2) + 1
                        else:
                            its_robentry=RAT[rs1-1]
                            robnumber=int(its_robentry[3])
                            val_rs1=robtable[robnumber-1][3]
                            val_rs2=RAT[rs2-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1
                    elif(isinstance(RAT[rs2-1], str)):  
                            its_robentry=RAT[rs2-1]
                            robnumber=int(its_robentry[3])
                            val_rs2=robtable[robnumber-1][3]
                            val_rs1=RAT[rs1-1] 
                            exec_cycle=instrs_table[robnumber-1][3] + 1  
                else:
                    val_rs1=RAT[rs1-1]
                    val_rs2=RAT[rs2-1]  
                    exec_cycle=cycle+1          
                
            RAT[rd-1]=robnum #updating/renaming RAT with ROB number entry
            print("RAT: ",RAT)
            cycle=cycle_calc(instruction_type,cycle,issue_cycle,instrs_table_entry,exec_cycle) #instruction table cycle calculations
            value=sub(val_rs1,val_rs2) #value of the operation calculation
            add_sub_rs_entry=add_sub_rs_entry-1
            robtable.append([robnum,instruction_type,rd,value]) # ROB table entry
            print("ROB table: ",robtable)
            print(" \n")
            rob_entry=rob_entry+1 

    return cycle,rob_entry,robtable,instrs_table,instrs_table_entry,add_sub_rs,add_sub_rs_entry,mul_div_rs,mul_div_rs_entry,load_store_rs,load_store_rs_entry
############################################ Taking input #####################
print("Enter all the instructions in binary: ")
cycle=1
rob_entry=1
robtable=[]
instrs_table=[]
instrs_table_entry=1
add_sub_rs=[]
add_sub_rs_entry=1
mul_div_rs=[]
mul_div_rs_entry=1
load_store_rs=[]
load_store_rs_entry=1
mem = {16: 15,17: 16}
instr = []
while True:
    try:
        line = input()
    except EOFError:
        break
    instr.append(line) #Press Ctrl+D to stop the input
print("\n")
print("Input Instructions are: ",instr)
print("\n")
ARF=[12,16,45,5,3,4,1,2,2,3]
RAT=ARF

for i in instr:
    cycle,rob_entry,robtable,instrs_table,instrs_table_entry,add_sub_rs,add_sub_rs_entry,mul_div_rs,mul_div_rs_entry,load_store_rs,load_store_rs_entry=ROB(i,cycle,rob_entry,robtable,instrs_table,instrs_table_entry,add_sub_rs,add_sub_rs_entry,mul_div_rs,mul_div_rs_entry,load_store_rs,load_store_rs_entry)

############################################## PRINTING FINAL VALUES###################################
print("Final RS entries")
print("LOAD STORE RS: ")
for i in load_store_rs:
    i[4]='R'+str(i[4])
    print(i)
print("ADD SUB RS") 
for i in add_sub_rs:
    print(i)
print("MUL DIV RS") 
for i in mul_div_rs:
    print(i)    
print("\n")
print ("Final ROB table entries")
for i in robtable:
    i[2]='R'+str(i[2])
    print(i)
print("\n")
print("Final Instruction Table: ")
for i in instrs_table:
    print(i)
print("\n")
print("Final RAT: ",RAT)
print("\n")
print("Final ARF: ")
ARF=RAT
count=0
for i in ARF:
    if(isinstance(i,str)):
        index=int(i[3])-1
        value=robtable[index][3]
        ARF[count]=value
        print(value)
        count+=1
    else:
        print(i)
        count+=1
print("\n")
