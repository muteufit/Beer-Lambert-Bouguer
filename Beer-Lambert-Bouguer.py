def Absorption():
    concentration = float(input("Enter Concentration (Molar): "))
    molar_absorptivity = float(
        input("Enter Molar Absorptivity (ε, L/(mol·cm)): "))
    path_length = float(input("Enter Path Length (cm): "))
    absorbance = molar_absorptivity * path_length * concentration
    return absorbance


def Concentration():
    absorbance = float(input("Enter Absorbance (A): "))
    molar_absorptivity = float(
        input("Enter Molar Absorptivity (ε, L/(mol·cm)): "))
    path_length = float(input("Enter Path Length (cm): "))
    concentration = absorbance / (molar_absorptivity * path_length)
    return concentration
