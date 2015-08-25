# generateRandomSequence

A utility to generate random DNA/Protein sequences and output them to a file.

Use the flags "fans" to run the program. Command line options:
 -h	Help
 -f	File name
 -a	Alphabet (DNA/dna/PROT/prot)
 -n	Number of characters
 -s	Optional: make file fasta format with given title
 -w	Optional: width of fasta line (default:70)
      
The n flag accepts scientific notation such as 1e6 for 1 million. Here is an example:

`python generateRandomSequence.py -f 1mb.fasta -a DNA -n 1e6 -s seq1`

