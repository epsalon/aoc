#!/usr/bin/env python3

import utils

def simulate(first_gen, rules, days):
	cur_gen      = first_gen
	total_offset = cur_gen.find('#')
	cur_gen      = cur_gen[total_offset:cur_gen.rfind('#') + 1]

	for d in range(days):
		cur_gen  = '....' + cur_gen + '....'
		next_gen = ''

		for i in range(len(cur_gen)-4):
			if cur_gen[i:i+5] in rules:
				next_gen += '#'
			else:
				next_gen += '.'

		offset   = next_gen.find('#')
		next_gen = next_gen[offset:].rstrip('.')

		total_offset += offset - 2

		if next_gen == cur_gen[4:-4]:
			break

		cur_gen = next_gen

	alive     = next_gen.count('#')
	days_left = days - d - 1
	idx_sum   = 0

	for i, p in enumerate(next_gen):
		if p == '#':
			idx_sum += i + total_offset

	return idx_sum + alive * days_left


utils.setup(2018, 12, dry_run=True)
fin = utils.get_input()

plants = fin.readline().replace('initial state:', '').strip()
fin.readline()

rules = set()

for line in fin:
	k, v = map(str.strip, line.split('=>'))

	if v == '#':
		rules.add(k)

ans = simulate(plants, rules, 20)
# assert ans == 1447

utils.submit_answer(1, ans)

ans2 = simulate(plants, rules, 50*10**9)
# assert ans2 == 1050000000480

utils.submit_answer(2, ans2)
