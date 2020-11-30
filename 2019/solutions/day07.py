#!/usr/bin/env python3

from utils import advent
from itertools import permutations
from lib.intcode import IntcodeVM

advent.setup(2019, 7, dry_run=True)
fin = advent.get_input()

program = list(map(int, fin.read().split(',')))
vms = [IntcodeVM(program) for _ in range(5)]
max_signal = float('-inf')

for inputs in permutations(range(5), 5):
	out = [0]

	for vm, inp in zip(vms, inputs):
		out = vm.run([inp, *out])

	if out[0] > max_signal:
		max_signal = out[0]

assert max_signal == 212460
advent.submit_answer(1, max_signal)

max_signal = float('-inf')

for inputs in permutations(range(5, 10), 5):
	out = [0]

	for vm, inp in zip(vms, inputs):
		out = vm.run([inp, *out], n_out=1)

	last_signal = out[0]

	while all(vm.running for vm in vms):
		for i, vm in enumerate(vms):
			out = vm.run(out, n_out=1, resume=True)

			if not vm.running:
				break

			if i == 4:
				last_signal = out[0]

	if last_signal > max_signal:
		max_signal = last_signal

assert max_signal == 21844737
advent.submit_answer(2, max_signal)