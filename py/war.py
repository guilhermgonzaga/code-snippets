"""
Simulates repeated dice-based battles until conquest or defeat in the board game War based on
number of attack and defense troops. The dice mechanics implemented serve to get
the observed frequency of the two outcomes and output the chance of success.

Battle rules:
- Up to 3 troops per side per battle, though territory may hold more;
- Troops are sorted in decreasing order before pairing them;
- Unpaired troops don't interfere on the result;
- For each attacker-defender troop pair, the attacker succeeds iff it's score (die face)
  is greater than the defender's;
- The defender wins in case of equal scores;
- The number of available troops is updated with losses after battle.

Usage:
	Run the script with two command-line arguments for attackers and defenders,
	or input them interactively when prompted.
"""

from random import randint
from sys import argv

N_REPLICATIONS = 100_000  # Number of replications to average over


"""
In the real game, the score is set by die roll and sorted in decreasing order.
"""
def get_score(n):
	dice = [randint(1, 6) for _ in range(n)]
	dice.sort(reverse=True)
	return dice


def battle(n_attack: int, n_defense: int):
	assert 1 <= n_attack <= 3 and 1 <= n_defense <= 3, 'Rules limit players to 1-3 troops'
	attack_score = get_score(n_attack)
	defense_score = get_score(n_defense)
	attack_losses = 0
	defense_losses = 0

	for a, d in zip(attack_score, defense_score):
		if a <= d:
			attack_losses += 1
		else:
			defense_losses += 1

	return attack_losses, defense_losses


"""
Simulate battles with maximum allowed troops iteratively until one side loses.
Returns True if conquest is successful.
"""
def try_conquest(n_attack: int, n_defense: int):
	# Remaining attack and defense troops
	rem_attack, rem_defense = n_attack, n_defense
	while rem_attack > 0 and rem_defense > 0:
		n_atk = min(3, rem_attack)
		n_def = min(3, rem_defense)
		lost_atk, lost_def = battle(n_atk, n_def)
		rem_attack -= lost_atk
		rem_defense -= lost_def

	if rem_defense == 0:
		return True

	return False


def main():
	try:
		n_attack = int(argv[1])
		n_defense = int(argv[2])
	except (IndexError, ValueError):
		n_attack = int(input('Atacantes: '))
		n_defense = int(input('Defensores: '))

	print('A  x  D:  Prob.')
	n_conquests = 0
	for _ in range(N_REPLICATIONS):
		n_conquests += try_conquest(n_attack, n_defense)
	freq_conquest = n_conquests / N_REPLICATIONS
	print(f'{n_attack:<2d} x {n_defense:2d}:  {100*freq_conquest:3.0f}%')


if __name__ == '__main__':
	main()
