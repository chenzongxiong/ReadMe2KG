The groups of order p^6 where prime p >= 7

M.F. Newman, E.A. O'Brien, and M.R. Vaughan-Lee


In this repository are files providing electronic access via Magma to presentations for groups of order p^6 where p >= 7.

The files are organised by isoclinism family Phi1, ..., Phi43.  These are copies of the files distributed as part of the SmallGroups library in Magma and reflect the presentations stored in [arXiv]. They were prepared originally as part of [NOVL]. 

For detailed instruction see the Magma online manual at http://magma.maths.usyd.edu.au/magma/ 

Here's a quick guide to load the contents of one of these files into Magma. 

% magma

AttachSpec ("spec");

import "Phi6.m": EasterfieldPhi6;

// return all groups of order 11^6 in Phi6 

X := EasterfieldPhi6(11);

[NOVL] M.F. Newman, E.A. O'Brien, and M.R. Vaughan-Lee,
Groups and nilpotent Lie rings whose order is the sixth power of a prime, J. Algebra, 278, 383-401, 2004.

[arXiv] M.F. Newman, E.A. O'Brien and M.R. Vaughan-Lee,
Presentations for the groups of order $p^6$ for prime $p \geq 7$, https://arxiv.org/abs/2302.02677

