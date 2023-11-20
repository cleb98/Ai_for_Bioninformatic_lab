#statistic extraction from a fasta file
import sys

# Read input and output file names from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
gc_threshold = int(sys.argv[3])


# Open input file and read contents
with open(input_file, 'r') as f:
    contents = f.readlines()

# Initialize variables for counting single bases, low complexity sequences, and GC couples
num_a = num_t = num_c = num_g = 0
num_low_complexity = num_gc_higher_than_threshold = 0
gc_higher_than_threshold = {}

read_id = ''
sequence = ''
for line in contents:
    if line.startswith('>'):
        # è il read_id della sequenza
        read_id = line.strip()[1:]
        
    else:
        sequence = line.strip() # strip() rimuove gli spazi bianchi o \n
        
        # Count single bases
        num_a += sequence.count('A')
        num_t += sequence.count('T')
        num_c += sequence.count('C')
        num_g += sequence.count('G')
        # count low complexity sequences
        if sequence.count('A') == len(sequence) or sequence.count('T') == len(sequence) or sequence.count('C') == len(sequence) or sequence.count('G') == len(sequence):
            num_low_complexity += 1
        # count GC couples
        if sequence.count('GC') > gc_threshold:
            num_gc_higher_than_threshold = sequence.count('GC')
            # passo al dizionario la chiave read_id e il valore num_gc_higher_than_threshold
            gc_higher_than_threshold.update({read_id : num_gc_higher_than_threshold})


# write the statistics to the output file
with open(output_file, 'w') as f:
        f.write("num_A: " + str(num_a) + "\n")
        f.write("num_T: " + str(num_t) + "\n")
        f.write("num_C: " + str(num_c) + "\n")
        f.write("num_G: " + str(num_g) + "\n")
        f.write("num_low_complexity: " + str(num_low_complexity) + "\n")
        f.write("num_gc_higher_than_threshold: " + str(num_gc_higher_than_threshold) + "\n")
        f.write("gc_higher_than_threshold: " + str(gc_higher_than_threshold) + "\n")

    


            
        

