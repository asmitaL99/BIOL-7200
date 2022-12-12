#bin/bash
gunzip=1;
verbose=1;
realign=1;
while getopts "a:b:r:e:o:f:z:v:i:h" option
do
	case $option in
		        a)reads1=$OPTARG;;
			b)reads2=$OPTARG;;
			r)ref=$OPTARG;;
			e)output=$OPTARG;;
			o)millsFile=$OPTARG;;
			f)realign=$OPTARG;;
			z)gunzip=$OPTARG;;
			v)verbose=$OPTARG;;
			i)index=$OPTARG;;
			h)echo"This is my SNP calling pipeline
				a) and b) will take the input read files which are in Fq format
				r)will take the reference genome file
				e)then we will map a) & b) to reference file and get output file
				o) will take the indels file as the input
				realign,verbose and gunzip can be 0 or 1 but i have assigned them as 1 as of now above" && exit;;
		esac
	done;
if [[ $verbose -eq 1 ]]
then
     echo "this will do the file check 1 and exit if the input read files are not found" 
fi;
if [[ $reads1 == *.fq ]] 
then
     echo "first file exists"
else
     echo "input read1 file does not exist" && exit
fi;
if [[ $reads2 == *.fq ]] 
then
     echo "second file exists"
else
     echo "input read2 file does not exist" && exit
fi;
if [[ $verbose -eq 1 ]] 
then
     echo "this will do the file check 2 and exit if the reference genome isnt found"
fi;
if [[ $ref == *.fa ]]
then
     echo "reference genome exists"
else
     echo "reference genome aint here" && exit
fi;
if [[ $verbose -eq 1 ]]
then
	echo "we need to do file check 3 and see if a vcf file already exists, if so then we need to remove it or ask the user if we can overwrite it"
fi
#if [[ -f *.vcf ]]
#then 
#	echo "a vcf file already exists , now if you want to overwrite it press 1 or else press 0"
#	read $answer
#fi;
#if [[ $read -eq 1 ]]
#then 
#	echo "deleting"
#	rm *.vcf;
#else 
#	echo "exiting" 
#	exit
#fi;
#Now we should start working on the actual pipeline 
bwa index $ref
#Now we should map our input read files to the reference genome
bwa mem -R '@RG\tID:foo\tSM:bar\tLB:library1' $ref $reads1 $reads2 > lane.sam
#Now as our initial mapping is done lets create our dict and fai files 
samtools faidx $ref
samtools dict $ref -o ref.dict
#Now we can go ahead and run the fixmate step as its helpful to first clean up read pairing info
if [[ $verbose -eq 1 ]]
then 
     echo "running fixmate now"
fi;
samtools fixmate -O bam lane.sam lane_fixmate.bam
if [[ $verbose -eq 1 ]]
then
     echo " need to run the sort command now"
fi;
#Now we will sort our output bam file a bit more
samtools sort -O bam -o lane_sorted.bam lane_fixmate.bam
if [[ $verbose -eq 1 ]]
then
     echo " need to do the index for lane sorted files"
fi;
#we should also index the sorted bam file
samtools index lane_sorted.bam
#Lets start working on the realignment part now
if [[ $realign -eq 1 ]]
then
     echo "lets start improving this and realign it using GATK"
     java -Xmx2g -jar ~/GenomeAnalysisTK.jar -T RealignerTargetCreator -R $ref -I lane_sorted.bam -o lane.intervals -known $millsFile --unsafe 
# reduce the number of miscalls of INDELs so it is helpful to realign raw alignment
     java -Xmx4g -jar ~/GenomeAnalysisTK.jar -T IndelRealigner -R $ref -I lane_sorted.bam -targetIntervals lane.intervals -known $millsFile -o lane_realigned.bam --unsafe
fi
if [[ $verbose -eq 1 ]]
then
	     echo " need to do the index for lane realigned files"
fi;
#we need to index this output realigned bam file as well
samtools index lane_realigned.bam
if [[ $verbose -eq 1 ]]
then
	             echo " now onto the variant calling pipeline"
fi;
#Now we can start the variant calling part which uses bcftools mpileup and will create the final vcf file
bcftools mpileup -Ou -f $ref lane_realigned.bam | bcftools call -vmO z -o $output
#we index our vcf file using tabix
tabix -p vcf $output
#Now we should unzip the file
if [[$gunzip -eq 1 ]]
then 
     echo "we should gunzip"
     gunzip $output
fi
#Now the VCF file needs to be converted into a bed format
if [[ $verbose -eq 1 ]]
then 
    echo"lets convert it to bed format now"

fi; 
sed 's/#//g' $output > new.vcf
awk '{print $1 "\t" $2 "\t" $2+(length($5)-length($4)) "\t" (length($5)-length($4))}' new.vcf > new.bed
sed 's/chr//g' new.bed > final.bed
awk -F '\t' '$4 == 0' final.bed > snps.txt
awk -F '\t' '$4 != 0' final.bed > indel.txt
#now we need to use awk and start position and last position cha kiti ATGC bases ahet te baghun calculate hoyla pahije  mhanun he has written ref and alt cha difference calculate kar lmao
#awk '{print $1 "\t" $2 "\t" $2+(length($5)-length($4)) "\t" (length($5)-length($4))}' new.vcf > new.bed
#sed 's/chr//g' new.bed > final.bed
#awk '{$4 == 0} final.bed > snps.txt
#awk '{$4 != 0} final.bed > indel.txt

#[main] Real time: 11177.311 sec; CPU: 11465.376 sec