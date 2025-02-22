weight=int(input("Enter your weight(kg)\n"))
height=float(input("Enter your height(m):\n"))
body_mass_index=weight/(height**2)
print(body_mass_index)
if body_mass_index<18.5:
    print("Ohh! you are underweight..Tired of being called 'too thin'? Your body deserves care, nourishment, and strength—every step forward is a step toward a healthier you!")
elif 18.5<=body_mass_index<=24.9:
    print("Congratulations ..you have normal weight! Keep nourishing your body and mind.")
elif 25<=body_mass_index<=29.9:
    ptint("You are over weight!!!Don't be discouraged! Your journey to a healthier you starts today. Small steps lead to big changes!")
elif body_mass_index>=30:
    print("Obesity is just a phase, not your fate. Small changes, healthy habits—your journey to a better you starts now!")
else:
    print("wrong input")
'''
output:

Enter your weight(kg)
78
Enter your height(m):
1.59
30.853209920493647
Obesity is just a phase, not your fate. Small changes, healthy habits—your journey to a better you starts now!
'''
'''
output

Enter your weight(kg)
45
Enter your height(m):
1.555
18.61022942277272
Congratulations ..you have normal weight! Keep nourishing your body and mind.
'''