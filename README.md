# snp-counter
Counts all unique SNP mutations in a .map file

## Prerequisites
A current installation of Python is required. For best results, please use Python 3.x and the latest PIP version.
 
For further information on how to install Python and update PIP, please go to the [Python Download Page](https://www.python.org/downloads/), and for installation help please go to the [Python Installation Help Page](https://wiki.python.org/moin/BeginnersGuide/Download)

> *NOTE for Windows users*: both PowerShell and Command Terminal require double quotes ("") around directories containing spaces.
 
> *NOTE for Linux, MacOS users*: the Terminal requires double quotes ("") around directories containing spaces.


## Instructions:
1) Copy *snpCounter.py* into any directory. If your terminal denies you access to other directories containing your *.map* files, copy *snpCounter.py* directly into the folder with the *.map* files.

2) Open a terminal in this directory, or change the directory of your terminal to the directory containing *snpCounter.py*
   
   ie. for Linux/MacOS: 
      ```
      $ cd ~/Documents/"folder containing data"
      ```
   
      for Windows:
      ```
      cd "C:/Users/username/Documents/folder containing data/"
      ```
        
3) Run the following command:

   for Linux/MacOS
    ```
    python3 snpCounter.py <inputFile> <outputFile>
    ```

   for Windows
    ```
    snpCounter <inputFile> <outputFile>
    ```

   **WARNING: the default output *will overwrite* any file in the directory named "*output.csv*" if no output file name is specified. Similarly, any existing file in the output directory with the same name as the output specified in the second argument *will be overwritten*.**

## Example
   On Linux/MacOS:
    
   if *snpCounter.py* is in the same folder as the data
   ```
    $ python3 snpCounter.py ecoliGenome.map mutations.csv
   ```
   if *snpCounter.py* is in a different folder:
   ```
   $ python3 snpCounter.py Documents/data/ecoliGenome.map mutations.csv
   ```
   (both of the above two sample commands will write the output to "*mutations.csv*" inside the same folder as *snpCounter.py*)
   
## Usage
Takes up to 2 input arguments, and requires valid *.map* file, generated from FASTA data, as first input argument.
| Settings | Description |
| --------- | ----------- |
| inputFile | Valid *.map* file generated from FASTA data. |
| outputFile | (OPTIONAL) Name of output file to be generated. |

Help documentation (including usage and output information) can be accessed using the following command.
```
snpCounter.py help
```

## Output
| Output File | Description |
| --------- | ----------- |
| filename | Count of position specific SNP mutations, in a comma separated plain text list. Default output is '*output.csv*' and will be generated in same directory as *snpCounter.py*. Recommended output is *.csv* format |


This program was written with *Python 3.9.2 on Windows10 Pro Build 19041* and tested on both *Windows10 Pro Build 19041* and *Ubuntu 18.04.5 LTS*
