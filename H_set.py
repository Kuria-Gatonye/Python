#sterile items
sterile_lab = {"Microscope","Centrifigure","Pippete"}
sterile_er = {"Stethoscope","Defribrator","Sutures"}

#contaminated items
contaminated ={"Defibrator","Sutures","Pippete"}

sterile_er -= contaminated
print("Sterile er equipment", sterile_er)
sterile_lab -= contaminated
print("Sterile lab equipment", sterile_lab)

all_sterile = sterile_lab | sterile_er
print("All equipment:" ,all_sterile)
print(contaminated)