import random
choice=random.randint(1000,10000)
print(choice)
num_str=str(choice)
compound=0
print(choice)
correct=0
count=1
control=int(input("enter how many attempts do you wanna try"))
while(count<=control):
    num=int(input("try to guess number"))
   
    numm_str=str(num)
    print(num)
    if(choice==num):
        print("you entered correct number ")
        break    
    else:        
        for i in range(0,4):
            
        
            if(num_str[i]==numm_str[i]):
            
                print("you entered number is  correct")
                print(numm_str[i])
                correct=correct+1
                print(f"no of corect values       {correct}")
               
    
        compound=compound+1