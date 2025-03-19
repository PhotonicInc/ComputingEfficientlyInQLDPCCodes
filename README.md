# Computing Efficiently in QLDPC Codes

This repository contains data to reproduce the results and figure of the paper [Computing Efficiently in QLDPC Codes](https://arxiv.org/abs/2502.07150).

## Paper abstract

It is the prevailing belief that quantum error correcting techniques will be required to build a utility-scale quantum computer able to perform computations that are out of reach of classical computers. The QECCs that have been most extensively studied and therefore highly optimized, surface codes, are extremely resource intensive in terms of the number of physical qubits needed. A promising alternative, QLDPC codes, has been proposed more recently. These codes are much less resource intensive, requiring up to 10x fewer physical qubits per logical qubit than practical surface code implementations. A successful application of QLDPC codes would therefore drastically reduce the timeline to reaching quantum computers that can run algorithms with proven exponential speedups like Shor's algorithm and QPE. However to date QLDPC codes have been predominantly studied in the context of quantum memories; there has been no known method for implementing arbitrary logical Clifford operators in a QLDPC code proven efficient in terms of circuit depth. In combination with known methods for implementing T gates, an efficient implementation of the Clifford group unlocks resource-efficient universal quantum computation. In this paper, we introduce a new family of QLDPC codes that enable efficient compilation of the full Clifford group via transversal operations. Our construction executes any m-qubit Clifford operation in at most O(m) syndrome extraction rounds, significantly surpassing state-of-the-art lattice surgery methods. We run circuit-level simulations of depth-126 logical circuits to show that logical operations in our QLDPC codes attains near-memory performance. These results demonstrate that QLDPC codes are a viable means to reduce, by up to 10x, the resources required to implement all logical quantum algorithms, thereby unlocking a much reduced timeline to commercially valuable quantum computing.

## Directory Layout
    src
    ├── stim_circuits
    │   ├── shyps_r3_logic_circuits                 # stim circuits for the logic simulations of the [49, 9, 4] SHYPS code
    │   ├── shyps_r3_memory_circuits                # stim circuits for the memory simulations of the [49, 9, 4] SHYPS code
    │   ├── shyps_r4_memory_circuits                # stim circuits for the memory simulations of the [225, 16, 8] SHYPS code
    │   ├── surface_code_d4_memory_circuits         # stim circuits for the memory simulations of the distance-4 surface code
    │   ├── surface_code_d8_memory_circuits         # stim circuits for the memory simulations of the distance-8 surface code
    │   └── reading_stim_circuits.py                # python file to load stim circuits
    │
    └── figure_raw_data                             # raw data to reproduce the figures from the paper

The working directory contains two folders `stim_circuits` and `figure_raw_data`.

The `stim_circuits` folder contains subdirectories containing the stim circuits used for simulating a particular code family (shyps or surface), code size ('r' parameter for shyps and distance for surface), number of codeblocks (this is only used for circuits implementing SHYPS codes), configuration (memory or logic), and types of detectors present in the circuit (this is only used for circuits implementing SHYPS codes).
The circuits themselves are named according to this convention along with the physical error probability of the noise they include. For example, the circuit for a distance 4 surface code memory simulation at a
physical error_probability of `p=0.001` would be named `surface_code_distance4_memory_simulation_circuit_p_0.001.stim`. Alternatively, the memory circuit for a [[49, 9, 4]] SHYPS code that uses only Z detectors for that same value of the physical error probability would be named `shyps_r3_one_codeblock_distance4_memory_simulation_Z_detectors_circuit_p_0.001.stim`. The `stim_circuits` folder also includes a python script called `reading_stim_circuits.py` that can be used to import our stim circuits to python. The simulations that produced Figures 1, 2, 5, and 6 of the paper can be recreated with the circuits in the `stim_circuits` directory.

The `figure_raw_data` folder contains the CSV files of the simulation results used to generate the logical error rate plots shown in Figures 1, 2, 5, and 6. Each file includes data corresponding to the physical error rate (`physical_error_rate`), the number of shots (`num_shots`), and the number of errors (`num_errors`). The observed logical error rate is defined as the ratio of num_errors to num_shots. For further details on how the logical error rates per syndrome extraction round are computed, as well as how the error bars are derived from the observed logical error rates, please refer to the Appendix of the paper.

## System Requirements

### Hardware Requirements

Loading the `stim` cicuits included in this repository requires only a standard computer with enough RAM to support the operations defined by a user. For minimal performance, this will be a computer with about 2 GB of RAM. Running Monte Carlo simulations of the circuits we provide requires more performant hardware. For simple testing and quantum memory simulations a computer with 16 GB of RAM and 4 cores with 1.8 GHz/core will be sufficient. To run simulations of logic using the circuits in `src/stim_circuits/shyps_r3_logic_circuits` in a reasonable amount of time (1-3 days) we recommend a machine with at least 32 GB of RAM and 16+ cores and 1.8 GHz/core.

### Software Requirements

The code contained in this repository has been tested on a *Windows*-11 Business operating system. It should also be compatible with Mac and Linux operating systems.

## Software Dependencies

The code contained in this repository can be run with a working version of python and `stim` (https://github.com/quantumlib/stim). 

Stim can be installed into a python 3 environment using pip: `pip install stim`.

## Attribution

If you use this data in your research, please cite as follows:
```
@misc{malcolm2025computingefficientlyqldpccodes,
      title={Computing Efficiently in QLDPC Codes}, 
      author={Alexander J. Malcolm and Andrew N. Glaudell and Patricio Fuentes and Daryus Chandra and Alexis Schotte and Colby DeLisle and Rafael Haenel and Amir Ebrahimi and Joschka Roffe and Armanda O. Quintavalle and Stefanie J. Beale and Nicholas R. Lee-Hone and Stephanie Simmons},
      year={2025},
      eprint={2502.07150},
      archivePrefix={arXiv},
      primaryClass={quant-ph},
      url={https://arxiv.org/abs/2502.07150}, 
}
```
