# Biophysical approach for GPCRs Automated Template Selection (Bio-GATS)

Biophysical approach for GPCRs Automated Template Selection (Bio-GATS).

## Getting Started

### Install dependencies

```shell script
pip install -r requirements.txt
```

### Install BLAST locally

The NCBI provides a suite of command-line tools to run BLAST called BLAST+. This allows users to perform BLAST searches on their own server without size, volume and database restrictions. BLAST+ can be used with a command line so it can be integrated directly into your workflow.

- Download and install BLAST command line tools [here](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)

**BLAST Help**

- BLAST documentation [here](https://biopython.readthedocs.io/en/latest/chapter_blast.html)
- Running BLAST from Python [here](https://gtpb.github.io/PPB18/assets/15_Running-BLAST_sys.argv)
- Download and install the BLAST+ package from [here](http://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
- BLAST manual can be found [here](http://www.ncbi.nlm.nih.gov/books/NBK1762/)
- Standalone BLAST Setup for Windows PC [here](https://www.ncbi.nlm.nih.gov/books/NBK52637/)
- Standalone BLAST Setup for Unix [here](https://www.ncbi.nlm.nih.gov/books/n/helpblast/chapter1/)
- Blast FTP Site [here](https://www.ncbi.nlm.nih.gov/books/NBK62345/)
- BLAST® Command Line Applications User Manual [here](https://www.ncbi.nlm.nih.gov/books/NBK279688/)

### Run code

```shell script
python main.py
```

## Known Issues

### [biopython no module named Bio](https://stackoverflow.com/questions/49848517/biopython-no-module-named-bio#answer-60529858) (for Windows users)

Rename directory `bio` to `Bio` inside `site-packages` directory.

**Aside**

- Path to `python` installation directory, use `where python` on Windows Command (only if Python is in Environment Variables)  
- Path to `site-packages` directory `Python\Python37\Lib\site-packages`

### [Error: mdb_env_open: There is not enough space on the disk.](https://www.biostars.org/p/413294/)

This is a known issue with the Windows release. The program `makeblastdb` attempts to allocate a very large amount of virtual memory. You can solve the problem by setting the a new BLAST environment variable `BLASTDB_LMDB_MAP_SIZE=1000000` See the BLAST setup [documentation](https://www.ncbi.nlm.nih.gov/books/NBK52637/) for details on how to set Windows environment variables. Once you change the variable, you'll need to close and reopen the command window where you were running BLAST for the new setting to take effect.
