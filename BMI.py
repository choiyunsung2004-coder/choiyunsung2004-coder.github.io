import numpy as np 
import pandas as pd 


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
print ("Hello, Please enter your body weight in kg, and height in m (EX. 175cm = 1.75 m)")
while True:
        try:
            weight = float(input("Enter your body weight: "))
            height = float(input("Enter your height: "))
            BMI = (weight / (height ** 2))
            
            if BMI < 18.5:
                print(f"You're BMI is {BMI}, you are considered Underweight")
                break
            elif 18.5 <= BMI <= 24.9:
                print(f"You're BMI is {BMI}, you are considered Normal Weight")
                break
            elif 24.9 <= BMI <= 40:
                print(f"You're BMI is {BMI}, you are considered Overweight")
                break
            elif BMI > 40:
                print(f"You're BMI is {BMI}, you are considered Obese")
                break
       
        except ValueError:
            print("Invalid input. Please enter a number.")

import matplotlib.pyplot as plt
import numpy as np

plt.ylim(0, 60)
plt.xticks([])
plt.ylabel("BMI")
y1 = (y:=BMI)

plt.axhline(y1, label ='Your BMI')
plt.axhspan(0, 18.5, facecolor=('cornflowerblue'), label = 'Underweight')
plt.axhspan(18.5, 24.9, facecolor=('springgreen'), label = 'Normal Weight')
plt.axhspan(24.9, 40, facecolor=('orange'), label = 'Overweight')
plt.axhspan(40, 60, facecolor=('tomato'), label = 'Obese')


plt.title("BMI Graph")
plt.legend()
plt.show()
