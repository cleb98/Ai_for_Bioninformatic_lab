import sys

input_file_1 = sys.argv[1]
input_file_2 = sys.argv[2]
output_file = sys.argv[3]

#usa questi path in debug
# input_file_1 = 'script/file1.fa'
# input_file_2 = 'script/file2.fa'
# output_file = 'script/fasta_output.fa'

read_id1 = ''
read_id2 = ''
sequence1 = ''
sequence2 = ''

with open(input_file_1, 'r') as file1:
# ciclo sul primo file per estrarre le sequenze 
    for line1 in file1:
        if line1.startswith('>'):
            read_id1 = line1.strip()[1:]
        else:
            sequence1 = line1.strip()
            with open(input_file_2, 'r') as file2:
                for line2 in file2:
                    if line2.startswith('>'):
                        read_id2 = line2.strip()[1:]
                    else:
                        sequence2 = line2.strip()
                    if sequence1 == sequence2:
                        sequence2 = '' # svuoto la seq2 per evitare che al prossimo giro di ciclo venga confrontata con la seq1 e quindi scritta nel file di output anche se non corrisponde al read_id del ciclo
                        with open(output_file, 'a') as f: # a sta per append, e serve per fare l'append di un file
                            #check se il file è vuoto altrimenti scrive in coda
                            f.seek(0, 2)  # sposta il cursore alla fine del file
                            f.write('>'  + read_id1 + ' ' + read_id2 + '\n')
                            f.write(sequence1 + '\n')


# ciclo sul secondo file per trovare se c'è una sequenza uguale a quella del primo file
# se la trovo, la scrivo nel file di output