# Python for Genomics

Foundational Python scripts and notebooks for handling biological sequences: FASTA parsing, GC content, reverse complements, codon-related operations, and sequence comparisons.

## Folder guides

- [Python sequence-analysis assessment](Final%20Exam/README.md)

## Repository guide

| Topic | Files |
| --- | --- |
| FASTA input | [fasta_read.py](fasta_read.py), [Files/](Files/) |
| Sequence composition | [gc_percentage.py](gc_percentage.py), [function_gc_percen.py](function_gc_percen.py) |
| Strand and codon operations | [function_rev_comp.py](function_rev_comp.py), [function_stop_cod.py](function_stop_cod.py), [dnautil.py](dnautil.py) |
| Sequence validation/comparison | [valid_aa.py](valid_aa.py), [compare_prefix.py](compare_prefix.py) |
| Python foundations | String operations, lists, loops, functions, modules, and file I/O scripts at the root |
| Course exercises | `coursera_qs*.py`, [final_exam.py](final_exam.py), and [Final Exam/](Final%20Exam/) |

## Working with the examples

Use Python 3. Inspect each script for hard-coded sequences or input filenames before running it from the repository root. Some examples require additional libraries, such as Biopython; notebooks require Jupyter. There is no consolidated environment lockfile or unified command-line interface.

These are small educational examples, with course exercises kept separately from research analyses. They demonstrate the sequence-programming foundations behind larger workflows.

## Biological interpretation

Check sequence alphabet, strand, case, ambiguous bases, and coordinate conventions before extending an example. GC content describes composition; it does not by itself establish function. A reverse complement represents the opposite DNA strand, while a candidate coding segment needs an explicit frame and genetic-code assumption.

Continue with [DNA sequencing algorithms](https://github.com/AnkitMukherji/Algorithms-for-DNA-Sequencing) and [bioinformatics algorithm notebooks](https://github.com/AnkitMukherji/Bioinformatics-Algorithms).
