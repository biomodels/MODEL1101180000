# MODEL1101180000: 

## Installation

Download this repository, and install with distutils

`python setup.py install`

Or, install using pip

`pip install git+https://github.com/biomodels/MODEL1101180000.git`

To install a specific version (in this example, from the 2014-09-16 BioModels release)

`pip install git+https://github.com/biomodels/MODEL1101180000.git@20140916`

## Usage

Importing the model package.

`import MODEL1101180000 as model`

Get the SBML string from the model

`print model.sbmlString`

If [python-libsbml](https://pypi.python.org/pypi/python-libsbml) bindings are
installed, the libsbml.SBMLDocument object is also accessible

`model.sbml`


# Model Notes


This is an SBML version with MesoRD annotations of the model described in:  
**Self-organized partitioning of dynamically localized proteins in bacterial cell division.**   
Barbara Di Ventura and Victor Sourjik. _Molecular Systems Biology_ 7:457 Jan
2011 doi: [10.1038/msb.2010.111](http://dx.doi.org/10.1038/msb.2010.111)

Abstract:  
How cells manage to get equal distribution of their structures and molecules
at cell division is a crucial issue in biology. In principle, a feedback
mechanism could always ensure equality by measuring and correcting the
distribution in the progeny. However, an elegant alternative could be a
mechanism relying on self-organization, with the interplay between system
properties and cell geometry leading to the emergence of equal partitioning.
The problem is exemplified by the bacterial Min system that defines the
division site by oscillating from pole to pole. Unequal partitioning of Min
proteins at division could negatively impact system performance and cell
growth because of loss of Min oscillations and imprecise mid-cell
determination. In this study, we combine live cell and computational analyses
to show that known properties of the Min system together with the gradual
reduction of protein exchange through the constricting septum are sufficient
to explain the observed highly precise spontaneous protein partitioning. Our
findings reveal a novel and effective mechanism of protein partitioning in
dividing cells and emphasize the importance of self-organization in basic
cellular processes.

This version of the model was downloaded from the MSB webpage (
<http://www.nature.com/msb/journal/v7/n1/datafiles/msb2010111-df5a.xml> ). It
contains information necessary for simulation encoded in annotations specific
to the tool MesoRD ( <http://mesord.sourceforge.net/> ).

This model originates from BioModels Database: A Database of Annotated
Published Models (http://www.ebi.ac.uk/biomodels/). It is copyright (c)
2005-2011 The BioModels.net Team.  
To the extent possible under law, all copyright and related or neighbouring
rights to this encoded model have been dedicated to the public domain
worldwide. Please refer to [CC0 Public Domain
Dedication](http://creativecommons.org/publicdomain/zero/1.0/) for more
information.

In summary, you are entitled to use this encoded model in absolutely any
manner you deem suitable, verbatim, or with modification, alone or embedded it
in a larger context, redistribute it, commercially or not, in a restricted way
or not..  
  
To cite BioModels Database, please use: [Li C, Donizelli M, Rodriguez N,
Dharuri H, Endler L, Chelliah V, Li L, He E, Henry A, Stefan MI, Snoep JL,
Hucka M, Le Novère N, Laibe C (2010) BioModels Database: An enhanced, curated
and annotated resource for published quantitative kinetic models. BMC Syst
Biol., 4:92.](http://www.ncbi.nlm.nih.gov/pubmed/20587024)


