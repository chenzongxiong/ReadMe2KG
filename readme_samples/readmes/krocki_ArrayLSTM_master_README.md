

# Array-LSTM
Implementation of recurrent array memory from "Recurrent Memory Array Structures" Technical Report

https://arxiv.org/abs/1607.03085

It is OK to use this code for research and other non-commercial purposes, please cite the report:

```
@article{rocki2016recurrent,
  title={Recurrent Memory Array Structures},
  author={Rocki, Kamil},
  journal={arXiv preprint arXiv:1607.03085},
  year={2016}
}
```

## Getting Started
to compile (with CUDA):

```
make PRECISE_MATH=0 cuda
```
or for precise FP64 (useful for debugging)

```
make PRECISE_MATH=1 cuda
```

CUDA version is most recent, CPU versions are outdated, OpenCL version is not really implemented

(Waiting for CUDA 8 final and heterogenous lambdas)

If you still wish to compile the CPU version run:

```
make cpu
```

## Usage
 
run like this
```
./deeplstm N B S GPU (test_every_seconds)
```
example (512 hidden nodes, 100 BPTT steps, batchsize = 64, GPU id = 0, run test every 1000s):

```
./deeplstm 512 100 64 0 1000
```

## Author
Kamil M Rocki (kmrocki@us.ibm.com)

## License
Copyright (c) 2016, IBM Corporation. All rights reserved.
 
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
