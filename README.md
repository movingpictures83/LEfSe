# LEfSe
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: prefix
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin for biomarker discovery using Linear discriminant analysis Effect Size (LEfSe) (Segata et al, 2011).

The plugin expects as input a text file of keyword, value pairs.  The keywords, and their corresponding definitions, are:
inputfile (Input file containing samples and abundances)
class (row of the inputfile containing class information, starts from 1)
subclass (row of the inputfile containing subclass information, starts from 1, -1 if no subclass)
subject (row of the inputfile containing sample identifiers)
outputdir (directory for output images)

The inputfile of samples and abundances is expected to be in matrix format, with entries on each row tab-delineated.  Columns correspond to samples.  With the exception of the class, subclass and subject rows (see above), rows correspond to taxa and entry (i, j) is the abundance of taxa i in sample j.

The plugin will output several files, all starting with (prefix):

(prefix).res: Output of LEfSe (textual)
(prefix).bargraph.png: Bargraph image
(prefix).cladogram.png: Cladogram image

In addition, outputdir will hold bargraph images for each potential biomarker.

This code is built largely around the LEfSe source code, hosted by the Huttenhower Lab:
https://bitbucket.org/nsegata/lefse/src

This code is under license and a copy of their license is supplied in license.lefse.txt

We have modified this code slightly and included this modified version.  Most of our changes pertained to upgrades associated with Python 3.
