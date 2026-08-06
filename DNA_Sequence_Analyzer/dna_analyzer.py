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

#Adding transcription function to convert DNA to RNA
def transcribe_DNA(sequence): 
    """ Converts a DNA sequence into an RNA sequence.
    """
    return sequence.replace("T", "U")

#Creating codon table
CODON_TABLE = {
   "UUU": "F", "UUC": "F",
   "UUA": "L", "UUG": "L",
   "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
   "AUU": "I", "AUC": "I", "AUA": "I",
   "AUG": "M",
   "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
   "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
   "AGU": "S", "AGC": "S",
   "CCU": "P", "CCC": "P", "CCA": "P",
   "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
   "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
   "UAU": "Y", "UAC": "Y",
   "CAU": "H", "CAC": "H",
   "CAA": "Q", "CAG": "Q",
   "AAU": "N", "AAC": "N",
   "AAA": "K", "AAG": "K",
   "GAU": "D", "GAC": "D",
   "GAA": "E", "GAG": "E",
   "UGU": "C", "UGC": "C",
   "UGG": "W",
   "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
   "AGA": "R", "AGG": "R",
   "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
   "UAA": "*",
   "UAG": "*",
   "UGA": "*"
}

def translate_RNA(RNA_sequence):
    """ Translates an RNA sequence into a protein sequence.
    Stop translation when a stop codon is encountered."""
    protein = ""
    for i in range(0, len(RNA_sequence), 3):
        codon = RNA_sequence[i:i+3]

        if len(codon) != 3:
            break
        amino_acid = CODON_TABLE.get(codon)
        if amino_acid == "*":
            break
        if amino_acid:
            protein += amino_acid
    return protein
RNA_sequence = transcribe_DNA(DNA)
print("Transcribed RNA sequence: ", RNA_sequence)   

protein_sequence = translate_RNA(RNA_sequence)
print("Translated protein sequence: ", protein_sequence)