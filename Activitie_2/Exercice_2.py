from Exercice_1 import BMI

if BMI < 18.5:
    print("Vous êtes en Sous-poids")
elif BMI < 25:
    print("Vous avez une Corpulence normale")
elif BMI < 30:
    print("Vous êtes en Surpoids")
elif BMI < 35:
    print("Vous avez une Obésité modérée")
elif BMI < 40:
    print("Vous avez une Obésité sévère")
else:
    print("Vous avez une Obésité morbide")
