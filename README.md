# MacroD
A collection of python scripts for Macrocycles project:

1) sNMR

Running a series of Gaussian calculations from *.xyz files. It copied xyz coordinate to "8e.g16" template
Input: 8e.g16 as a Gaussian template

> python3 sNMR.py

2) SnapshotsOpt

Running a series of geometry optimization from previous sNMR calculations by changing the level of theory and associated keywords.
Input: *.g16

> python3 SnapshotsOpt.py

3) Analysis
3a) getNMRshifts.py

Collect NMR chemical shifts, their deviation to exp. values, RMSE, and their relative energies with respect to lowest energy conformer.
-Output: *.csv file

How to use:
-provide a series of Gaussian *.log files

> python3 getNMRshifts.py

3b) analysis.py

Using dataframe to sort relevance conformers below 5 kcal/mol, below 10 kcal/mol, below 15 kcal/mol, and below 20 kcal/mol
Input: 8e.csv

> python3 analysis.py


