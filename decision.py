print("The subjects to be Entered are:physics,math,programming,Biology,chemistry,circuits,AI concept,statistics")


str1=input("enter the subject 1:")
str2=input("enter the subject 2:")

if(str1=="math" and str2=="physics") or (str1=="physics" and str2=="math"):
    print("Apply for the Mechanical engineering")
    
elif(str1=="programming" and str2=="math") or (str1=="math" and str2=="programming"):
    print("Apply for computer Engineering")

elif(str1=="Biology" and str2=="chemistry") or (str1=="chemistry" and str2=="Biology"):
    print("Apply for Biotechnology Engineering")
    
elif(str1=="circuits" and str2=="math") or (str1=="math" and str2=="circuits"):
    print("Apply for Electronics Engineering")
 
elif(str1=="programing" and str2=="statistics") or (str1=="statistics" and str2=="programming"):
    print("Apply for the AI&DS Engineering")
    
    
elif(str1=="programing" and str2=="AI concept") or (str1=="AI concept" and str2=="programing"):
   print("Apply for AI&ML Engineering")
   
   
else:
    print("suitable branch Not Found")
    
