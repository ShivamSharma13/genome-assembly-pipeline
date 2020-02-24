# Team2-GenomeAssembly
Hanchen Wang, Kristine Lacek, Rhiya Sharma, Shivam Sharma, Shuting Lin

## Pre-running installations

**The java runtime environment** is needed to install FastQC. this was done by the command 
wget https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u232-b09/OpenJDK8U-jdk_x64_linux_hotspot_8u232b09.tar.gz
java was then exported to the PATH

**FastQC** was downloaded using wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip and then subsequently unzipped. Permissions were then changed for the fastqc script using chmod 755 FastQC/fastqc.

**Fastp Binary** was downloaded using wget http://opengene.org/fastp/fastp
chmod a+x ./fastp


## Requisite software
**Prinseq v.0.20.4** -- [PRINSEQ](www.prinseq.sourceforge.net)

**ABySS v.1.5.2** -- [BC Cancer Agency](www.bcgsc.ca/platform/bioinfo/software/abyss)

**Fastqc v.0.11.2** -- [Babraham Bioinformatics](www.bioinformatics.babraham.ac.uk/projects/fastqc/)

**CISA v.1.3** -- [Contig Integrator for Sequence Assembly](sb.nhri.org.tw/CISA/en/CISA)

**Edena v.3.131028** -- [Genomic Research Laboratory - University of Geneva Hospitals](www.genomic.ch/edena.php)

**SPAdes v.3.5.0** -- [St. Petersburg Academic Univerity of the Russian Academy of Sciences](bioinf.spbau.ru/spades)

**Unicycler v0.4.8** -- 

**QUAST v.2.3** -- [St. Petersburg Academic Univerity of the Russian Academy of Sciences](bioinf.spbau.ru/quast)

**SMALT v.0.7.5** -- [Wellcome Trust Sanger Institute](https://www.sanger.ac.uk/resources/software/smalt)

## Scripts
### module_wranglePairedEnds.py
_Returns a dictionary of 'key : value' pairs._

### Below are templates...... still revamping
**Usage:** module_wranglePairedEnds.py \</path/to/input files/\>

### module_ABySS.py
_Generates hash of trimmed reads and invokes either SE or PE ABySS de novo assembly._
_Outputs contig file(s) in FASTA format in user-specified directory._

**Usage:** module_ABySS.py \</path/to/inputfiles/\> \</path/to/output directory/\>

### module_Edena.py 
_Generates hash of trimmed reads and invokes either SE or PE Edena de novo assembly._
_Output is a directory containing the contig and scaffold files in FASTA format._

**Usage:** module_Edena.py \</path/to/inputfiles/\> \</path/to/output directory/\>

### module_SPAdes.py
_Generates hash of trimmed reads and invokes either SE or PE SPAdes de novo assembly._
_Output is a directory containing the contig and scaffold files in FASTA format._

**Usage:** module_SPAdes.py \</path/to/inputfiles/\> \</path/to/output directory/\>

### module_Unicycler.py
_Generates hash of trimmed reads and invokes either SE or PE SPAdes de novo assembly._
_Output is a directory containing the contig and scaffold files in FASTA format._

**Usage:** module_Unicycler.py \</path/to/inputfiles/\> \</path/to/output directory/\>

### module_Prinseq.py
_User-friendly script to run prinseq with specified parameters._
_variable outPath (the output directory) is currently hard coded._

**Usage for unpaired read:** module_Prinseq.py -s \</path/to/read\> -l \<left-trim no.\> -r \<right-trim no.\>

**Usage for paired-end read:** module_Prinseq.py -p \</path/to/read1\> \</path/to/read2\> -l \<left-trim no.\> -r \<right-trim no.\>

### module_fastQC.py
_Invokes fastqc on raw read file(s)_

**Usage:** module_fastQC.py \</path/to/input files/\> \</path/to/output directory/\>

### module_Quast.py
_Locates contig/scaffold FASTA files and invokes Quast to generate assembly metrics._
_Quast metrics files are generated in the respective assembly directories._

**Usage:** See script for usage example

### module_QuastOut.py
Calculates scores for lists of quast evaluation results and outputs into tabular format.

**Usage:** See script for usage example
