#
# Copyright 2025, Photonic Inc. All Rights Reserved.
#
"""
This is an example script that can be used to load the stim
circuits in this directory into a list.
"""
import stim
stim_circuits = []
error_probabilities = [5e-05, 0.0001, 0.00025, 0.0005, 0.001]

for p in error_probabilities:

    path = f'two_shyps_r3_codeblock_random_clifford_logical_simulation_circuit_p_{p}.stim'
    with open(path) as f:
        print(f'Importing stim circuit for p={p}')
        stim_circuits.append(stim.Circuit(f.read()))

# We can print out some data about the circuits:
print('--- Circtuit Elements ---')
print(f'Number of qubits: {stim_circuits[0].num_qubits}')
print(f'Number of measurements: {stim_circuits[0].num_measurements}')
print(f'Number of detectors: {stim_circuits[0].num_detectors}')
print(f'Number of observables: {stim_circuits[0].num_observables}')
