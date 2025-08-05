ward_4a = [" Bed1: Kuria","Bed2: Fatuma"]

#new admission
ward_4a.append("Bed3: Viktor")
ward_4a.insert(1 , "Bed4: James")

print("Ward4A:", ward_4a)

#Discharge patients
discharged = ward_4a.pop(1)
print(f"Discharged: {discharged} remaining: {ward_4a}")