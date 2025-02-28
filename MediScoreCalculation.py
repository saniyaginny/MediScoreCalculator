# Medi score calculation function

# Functions to calculate the scores for each property

# Calculating the air property
def airScoreCalculation():
    while True: # If false, the function will repeat in case the user made a mistake entering values
        airValue = input("Enter whether the Patient is on air (A) or oxygen (O): ").upper() # Input for calculating Air or Oxygen property
        
        if airValue == "A":
            return 0
        
        elif airValue == "O":
            return 2
        
        else: 
            print("Invalid input.") # So the user can input the value again

airScore = airScoreCalculation() # Setting the value as the score so it can be used when calculating the final score
print("  ")

# Calculating the conscious property
def consciousScoreCalculation():
    while True:
    
        consciousValue = input("Enter whether Patient is Alert (A) or CVPU, Confusion (C), Voice (V), Pain (P), Unresponsive (U): ").upper() # Input for calculating Consciousness property
        
        if consciousValue == "A":
            return 0
        
        elif consciousValue in ["C", "V", "P", "U"]: # All these values result in the same end score
            return 3
        
        else: 
            print("Invalid input.") # So the user can input the value again

consciousScore = consciousScoreCalculation()
print("  ")

# Calculating the respiration rate property
def respirationScoreCalculation():
    while True:
    
        respirationRate = int(input("Enter the Respiration Rate of the Patient (per minute): ")) # Input for calculating the Respiration Rate property

        if respirationRate <= 8:
            return 3
        
        elif 9 <= respirationRate <= 11:
            return 1
        
        elif 12 <= respirationRate <= 20:
            return 0
        
        elif 21 <= respirationRate <= 24:
            return 2
        
        elif respirationRate >= 25:
            return 3
        
        else:
            print("Invalid input")

respirationScore = respirationScoreCalculation()
print("  ")

# Calculating the blood oxygen level property
def bloodOxygenScoreCalculation(airScore): # Passing the air score through this function so it can be used
    while True:

        bloodOxygen = int(input("Enter the SpO₂ level of the Patient (%): ")) # Input for calculating the Blood Oxygen level property

        if bloodOxygen <= 83:
            return 3
        
        elif 84 <= bloodOxygen <= 85:
            return 2

        elif 86 <= bloodOxygen <= 87:
            return 1
        
        elif  88 <= bloodOxygen <= 92 or (bloodOxygen >= 93 and airScore == 0): # Air score is used here as the normal score values are different depending on the air score
            return 0

        elif (93 <= bloodOxygen <= 94 and airScore == 2):
            return 1
        
        elif (95 <= bloodOxygen <= 96 and airScore == 2):
            return 2
        
        elif (bloodOxygen >= 97 and airScore == 2):
            return 3
        
        else:
            print("Invalid input")

bloodOxygenScore = bloodOxygenScoreCalculation(airScore)
print("  ")

# Calculating the temperature score property
def temperatureScoreCalculator():
    while True:

        temperature = float(input("Enter temperature of Patient (°C): ")) # Input for calculating the Temperature property
        
        temperature = round(temperature, 1) # To round the patient's temperature to 1 decimal place

        if temperature <= 35.0:
            return 3

        elif 35.1 <= temperature <= 36.0:
            return 1
        
        elif 36.1 <= temperature <= 38.0:
            return 0
        
        elif 38.1 <= temperature <= 39.0:
            return 1
        
        elif temperature >= 39.1:
            return 2
        
        else:
            print("Invalid input.")

temperatureScore = temperatureScoreCalculator()
print("  ")

# Calculating the bonus Capillary Blood Glucose during fasting property
def fastingGlucoseScoreCalculator():
    while True:

        fastingGlucose = float(input("Enter Capillary Blood Glucose of patient when fasting (mmol/L): "))

        fastingGlucose = round(fastingGlucose, 1) # To round the glucose values to one decimal place

        if fastingGlucose <= 3.4:
            return 3
        
        elif 3.5 <= fastingGlucose <= 3.9:
            return 2
        
        elif 4.0 <= fastingGlucose <= 5.4:
            return 0
        
        elif 5.5 <= fastingGlucose <= 5.9:
            return 2
    
        elif fastingGlucose >= 6.0:
            return 3
        
        else:
            print("Invalid input.")

fastingGlucoseScore = fastingGlucoseScoreCalculator()
print("  ")

# Calculating the bonus Capillary Blood Glucose 2 hours after eating property
def eatingGlucoseScoreCalculator():
    while True:

        eatingGlucose = float(input("Enter Capillary Blood Glucose of patient 2 hours after eating (mmol/L): "))

        eatingGlucose = round(eatingGlucose, 1)

        if eatingGlucose <= 4.4:
            return 3

        elif 4.5 <= eatingGlucose <= 5.8:
            return 2
        
        elif 5.9 <= eatingGlucose <= 7.8:
            return 0

        elif 7.9 <= eatingGlucose <= 8.9:
            return 2
        
        elif eatingGlucose >= 9.0:
            return 3
        
        else:
            print("Invalid input.")

eatingGlucoseScore = eatingGlucoseScoreCalculator()
print("  ")

# Calculating Medi score with all the properties added together
mediScore = airScore + consciousScore + respirationScore + bloodOxygenScore + temperatureScore + fastingGlucoseScore + eatingGlucoseScore

print("The patient's final Medi score:" , mediScore) # The output is user friendly
print("  ")

        





        






