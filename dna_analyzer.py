# Naming the DNA Sequence Analyzer Program
print("Welcome to the DNA Sequence Analyzer!")

#Asking the user to input a DNA sequence
DNA = input("Enter DNA sequence: ")

#Confirm the DNA sequence entered by the user
print("You entered: ", DNA)
DNA = DNA.upper()

#Finding the length of the DNA sequence
length = len(DNA)
print("Sequence length: ", length)

#Counting each base in the DNA sequence
print("A:", DNA.count("A"))
print("T:", DNA.count("T"))
print("G:", DNA.count("G"))
print("C:", DNA.count("C"))

#Calculate GC contents 
G = DNA.count("G")
C = DNA.count("C")
GC_content = ((G + C) / length) * 100
print("GC content:", round(GC_content, 2), "%")

#Calculate AT contents 
A = DNA.count("A")
T = DNA.count("T")
AT_content = ((A + T) / length) * 100
print("AT content:", round(AT_content, 2), "%")

#Calculate percentage of each base in the DNA sequence
A_percentage = (A / length) * 100
T_percentage = (T / length) * 100
G_percentage = (G / length) * 100
C_percentage = (C / length) * 100
print("Percentage of A:", round(A_percentage, 2), "%")
print("Percentage of T:", round(T_percentage, 2), "%")
print("Percentage of G:", round(G_percentage, 2), "%")
print("Percentage of C:", round(C_percentage, 2), "%")  