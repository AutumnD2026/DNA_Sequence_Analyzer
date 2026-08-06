# Naming the DNA Sequence Analyzer Program
print("Welcome to the DNA Sequence Analyzer!")

#Asking the user to input a DNA sequence
DNA = input("Enter DNA sequence: "). upper()

#Adding DNA Sequence Validation
def validate_dna_sequence(sequence):
    valid_bases = ("ATGC")
    for base in sequence:
        if base not in valid_bases:
            return False
    return True
if not validate_dna_sequence(DNA):
    print("Invalid DNA sequence. Please enter a sequence containing only A, T, G, and C.")
    exit()

#Adding Reverse Complement Function
def reverse_complement(sequence):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    reverse_sequence = sequence[::-1]
    reverse_complement_sequence = ""
    for base in reverse_sequence:
        reverse_complement_sequence += complement[base]
    return reverse_complement_sequence

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

#Adding the reverse complement of the DNA sequence
reverse_comp = reverse_complement(DNA)
print("Reverse complement: ", reverse_comp)

#Calculate percentage of each base in the DNA sequence
A_percentage = (A / length) * 100
T_percentage = (T / length) * 100
G_percentage = (G / length) * 100
C_percentage = (C / length) * 100
print("Percentage of A:", round(A_percentage, 2), "%")
print("Percentage of T:", round(T_percentage, 2), "%")
print("Percentage of G:", round(G_percentage, 2), "%")
print("Percentage of C:", round(C_percentage, 2), "%")  

