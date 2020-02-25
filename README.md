# Team2-GenomeAssembly
Kristine Lacek, Shivam Sharma, Shuting Lin, Rhiya Sharma, Hanchen Wang,

## Pre-running installations

**Conda is the recommended way of installing tools.**

**The java runtime environment** is needed to install FastQC. this was done by the command 
wget https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u232-b09/OpenJDK8U-jdk_x64_linux_hotspot_8u232b09.tar.gz
java was then exported to the PATH

**FastQC** was downloaded using wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip and then subsequently unzipped. Permissions were then changed for the fastqc script using chmod 755 FastQC/fastqc.

**Fastp Binary** was downloaded using wget http://opengene.org/fastp/fastp
chmod a+x ./fastp


## Requisite software
**ABySS version 1.5.2** 

**SPAdes version 3.5.0** 

**Unicycler version 0.4.8**

**MaSuRCA version 3.3.5**

**SKESA version 2.3.0**

**Velvet version 1.2.10**

**QUAST version 2.3** 


## Scripts Usage:


**Step 1**  Pre-assembly trimming needs to be carried out using Fastp, which can be done using the QC_trim.py and supplying the input data through arguments.

**Step 2**
  Since the fastq files might be coming from different instruments producing reads of different lengths, we've created create_manifest_file.py which prepares prerequiste information required for scripts downstream.
  
**Step 3**
  Rest of functionalities will be automated through the backbone.py script (our cool name for a manager or pipeline script). The backbone.py script encapsulates different wrapper python script that are invoked internally to produce a genome assembly file.
 
**Step 4**
  The final step is running quast on the assemblies and observing which assembler is working the best. The quast functionality is integrted into our pipeline as well and should execute automatically when the backbone.py script is finished running.
