height=float(input("Enter your Height:"))
weight=float(input("Enter your Weight:"))

height=height/100

bmi=weight/(height*height)
print("BMI IS:",bmi)

if(bmi>0):
    if(bmi<=16):
        print("underweight")
    
    elif(bmi<=25):
        print("healthy")

    else:
        print("overweight")