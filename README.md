# BIOL-7200
File -> alagwankar3_overlapBED
1) OVERLAP Question:
   This is a very common task in genome analysis. Oen, we want to find functional elements that
overlap with other elements, e.g. transcription start sites contained in transposable elements,
predicted transcription factor binding sites within DNase hypersensitivity sites, or even some set of
genes or horizontally transferred regions. Maybe you found some peaks in your ChIP-seq data and you
want to see if those overlap with known enhancers, or perhaps you have a set of SNPs and you would
like to know what genes they fall in. If you do not know what those words mean, go look them up!
Comparing ALL coordinates of the first set versus ALL coordinates of the second set will work for small
sets only. That method scales with the multiplication of the sizes of the two sets. If you have 106
members in each set (not at all unrealistic) do you want to make 1012 comparisons? You need to find a
better way.
What your script should do:
1. Take in two files that contain sets of coordinates in BED format. You can assume that the
contents of both files are sorted by chromosome, start and stop. Having the data sorted allows
you to greatly speed up the process of the overlap.
Definitions for BED file format can be found:
https://genome.ucsc.edu/FAQ/FAQformat#format1
2. Take in an option for the minimum percent overlap, i.e. percent of bases of any given member
of the first set that must be in a member of the second set to be counted as overlapping.
3. Print to a file the members of the first set which overlap with the second set and meet the
minimum overlap and other conditions specified. Each overlap should only be printed once in
this manner.
4. Allow an option to print both the member of the first set and the member of the second set
that it overlaps with on the same line, in effect ʻjoiningʼ the rows.

2)SNP calling pipeline
You will be required to create a pipeline for calling Single Nucleotide Polymorphisms (SNPs).
Underlying biology and problem description: We are living in the post-genomic era where
sequencing genomes now takes under a day; thousands of genomes have been sequenced and
assembled. Many (not all) organisms, whether prokaryote or eukaryote, now have a complete
reference (or a canonical) genome sequenced and assembled already. Given that assembling
genomes de novo requires substantial expertise along with computational and human resources,
a more practical approach of analyzing genomes is to map the genomic reads to an existing
reference. This approach is also referred to as genome re-sequencing.
Once you have your reads mapped to an existing reference strain, the process can diverge into
multiple directions depending on the nature and objective of the project. One common direction
is to call variants. Variants are simply the bases in your sample’s genome that are different from
the corresponding bases in the reference genome. These differences can (or cannot) lead to a
range of phenotypic differences either directly (as is the case in amino acid changes or
nonsynonymous changes) or indirectly (a change of base in the splice site leading to change in
splicing pattern or change in the regulatory region leading to enhanced or depleted gene
expression). In this exercise, we will write a pipeline for mapping genomic reads to a reference
genome and calling SNPs from the mapping. You have seen most of these commands before, be
sure to use the WGS/WES Mapping to Variant Calls – Version 1.0 as a guide

3) All to fasta
   Converting FASTQ, MEGA, EMBL, SAM, VCF, GenBank formats of a sequence to FASTA format.
  
4) SWalign and NWalign
   Main assignment: Needleman-Wunsch (NW) algorithm
Max score: 100 points
This is an example of another complex problem that has a rather simple solution. NW algorithm
is a classical bioinformatics algorithm designed to obtain optimal global alignment for a given pair
of sequences. The algorithm falls under the class of dynamic programming which in simple
language is the class of algorithm that work by breaking a problem into subproblems, solving each
subproblem and joining the solutions to reach the global solution.
The algorithm can be divided into three steps:
1. Initialization: Construction of the matrix with the two sequences as each axis and selection
of a suitable scoring system. For simplicity, let’s have three types of scores:
a. Match = +1
b. Mismatch = -1
c. Gap = -1
2. Matrix filling: Filling the matrix based on the scoring system. This occurs one row at a time,
starting from the topmost row. Each cell in the matrix derives the value from the adjacent
cells located to the left, top-left or on top of the current cell. The match score is added or
gap/mismatch penalty is subtracted from these adjacent cells and the maximum value is
carried over to the current cell (Figure 1).
3. Backtracking: Once the matrix has been filled up, backtracking is done to compute the
optimal alignment(s). The backtracking step starts from the very last cell filled in the matrix
(the bottom-right cell) and proceeds to the first cell filled in matrix (the cell with 0 in the
upper left corner of the matrices in Figure 1). This backtrack path is computed by moving
through the adjacent cells (cells to the left, top-left and on top of the current cell) with the
maximum score such that the path has the maximum total score (Figure 2). If multiple
paths exist, then all of them are considered to be the optimal paths. This path is converted
to an alignment by the following rule: the path moves diagonally to the left if there is a
match or if the maximum score of the adjacent cells is present in the diagonal left cell. If
either of these are true, the two corresponding characters from each sequence are aligned
together. When the maximum score is obtained by moving horizontally, then a gap is
introduced in the sequence on the vertical axis, and if the path moves vertically, then a gap
is introduced in the sequence on the horizontal axis.
Backtracking rules:
1. Always take the diagonal when the diagonal is either (1) the highest score or (2) tied for
highest score
2. If the diagonal is not the highest score, take the "Up" if it is either (1) the highest score or
(2) tied for highest score.
3. Take the "Left" if the diagonal and “Up” are not the highest
For the purpose of this assignment, you will only observe a single optimal path with the above
rules in the test sequences we use. You will not have to worry about multiple, optimal paths. 
