# snp-counter
Counts all SNP substitutions in .map file


Instructions:

    1) Copy snpCounter.py into any directory. If your terminal denies you access to other directories 
       containing your .map files, copy snpCounter.py directly into the folder with the .map files.
    2) Open a terminal in this directory, or change the directory of your terminal to the directory containing snpCounter.py
       (ie. for Linux: $ cd /home/Documents/folder_containing_data; for Windows: cd "C:\Users\username\Documents\folder containing data\")
    3) Type the following command: "snpCounter.py inputFile outputFile" for Windows or "python3 snpCounter.py inputFile outputFile" for Linux
       or "python snpCounter.py inputFile outputFile" for Mac, where "inputFile" is the name of the .map file you want to 
       analyze and "outputFile" is the name of the .csv output file the program will create for you. Specifying an output file is optional, and 
       the default output file is output.csv which will be created in the directory containing snpCounter.py.
       WARNING: the default output will overwrite any file in the directory named "output.csv" if no output file name is specified.

    Sample Linux command if snpCounter.py is in the same folder as the data:  $ python3 snpCounter.py ecoliGenome.map mutations.csv
    Sample Linux command if snpCounter.py is in a different folder:           $ python3 snpCounter.py home/Documents/data/ecoliGenome.map mutations.csv
      (both of the above two sample commands will write the output to mutations.csv inside the same folder as snpCounter.py)

Below is a sample run in the Windows Command Terminal, with snpCounter.py in the same directory as the .map data, and the 
output written to a sub-folder within this directory.
![image](https://user-images.githubusercontent.com/81862894/113482424-b640a200-946c-11eb-8222-c9cb69cf413d.png)
