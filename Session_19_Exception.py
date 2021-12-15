#Error
#amt = 100
#if (amt>150):
    #print("You are eligible to purchase") 
#else:
    #print("You are not eligible to purchase")
#---------------------------------------------#

#Exception
#num = 100
#result = 100/0
#print("The result is:",result)
#-----------------------------#

#Try and Except Block
#a = [1,2,3]

#try:  
    #print("Second Element : %d"%(a[1]))
    #print("Fourth Element : %d"%(a[3]))
#except:
    #print("An error occured")
#--------------------------------------#
def fun(a,b):
    try:
        c = ((a+b)/(a-b))

    except ZeroDivisionError:
        print("a/b results in 0")

    else:
        print(c)

    finally:
        print("This clause always executes")


fun(2,3)
fun(3,3)
#-------------------------------------------#
