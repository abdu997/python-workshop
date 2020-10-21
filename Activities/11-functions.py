"""
    In this activity we will write a program that calculates a patient's PCO2.
    I plagarized the definition of that from the good folks at globalrph.com
        "The PCO2 equation puts into physiologic perspective one of the most 
        common of all clinical observations: a patient’s respiratory rate and breathing effort. 
        The equation states that alveolar PCO2 (PACO2) is directly proportional to the amount of 
        CO2 produced by metabolism and delivered to the lungs (VCO2) and inversely proportional 
        to the alveolar ventilation (VA). While the derivation of the equation is for alveolar PCO2, 
        its great clinical utility stems from the fact that alveolar and arterial PCO2 can be assumed 
        to be equal."
    Write a program that prompts for a patients amount of CO2 produced by metabolism (VCO2) and 
    the alveolar ventilation (VA). Pass the values to a function called PCO2 that retursn the 
    patient's PCO2 using the equation PCO2 = VCO2 * 0.86 / VA
"""