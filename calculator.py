import math

def fact(n):                                         # factorial
    f=1;
    s=n
    for i in range(1,n):
        f=f*s;
        s=s-1;
    return(f)

def calr(n): 
    if n == '1':                                      #sum
        print("\tAddition")
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:")) 
        print("\n",a,"+",b,"=",a+b)
    elif n == '2':                                   #difference
        print("\tSubtraction")
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:")) 
        print("\n",a,"-",b,"=",a-b) 
    elif n == '3':                                   #multiplication 
        print("\tMultiplication")
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:")) 
        print("\n",a,"*",b,"=",a*b)
    elif n == '4':                                   #division     
        print("\tDivision")    
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:")) 
        print("\n",a,"/",b,"=",float(a/b))
    elif n == '5':                                   #x^n
        print("\tPower")
        a=int(input("Enter Number:"))
        b=int(input("Enter exponent:"))
        c=b
        x=1
        while (b!=0):
            x=x*a;
            b=b-1;
        print("\n",a,"^",c,"=",x)
    elif n == '6':                                  #logarithm
        print("\tLogarithm")
        a=int(input("Enter Number:"))
        b=int(input("Enter base:"))
        print("Result is:",math.log(a,b))
    elif n == '7':                                  #natural logarithm
        print("\tNatural Logarithm")
        a=int(input("Enter Number:"))
        print("Result is:",math.log(a))
    elif n == '8':                                  #nCr
        print("\tCombination(nCr)")
        a=int(input("Enter Number(n):"))
        b=int(input("Enter Number(r):"))
        c=a-b
        print("Result :",fact(a)/(fact(b)*fact(c)))
    elif n == '9':                                 #nPr
        print("\tPermutation(nPr)")
        a=int(input("Enter Number(n):"))
        b=int(input("Enter Number(r):"))
        c=a-b
        print("Result :",fact(a)/fact(c))
    elif n == '10':                                #e^x
        print("\tExponential")
        a=int(input("Enter Number:"))
        print("Result is:",math.exp(a))
    else:
        print("Some error occured,Try again")
 

# main program    
print("""
       Calculator
    :::::::::::::::::
""")

print(""" Select One Operation:
For addition→ Enter 1
For subtraction→ Enter 2
For multiplication→ Enter 3
For division→ Enter 4
For X^n→ Enter 5
For logarithm→ Enter 6
For natural logarithm→ Enter 7
For nCr→ Enter 8
For nPr→ Enter 9
For e^x→ Enter 10
    """)
c=1
while(c!=0):
    o = input("Enter operation:") #opertion
    calr(o)                   #function calling
    c=int(input("Do you want to continue?(1-Yes/0-No):"))


