from random import randrange

points = 0

while True:
	print(points)

	keep_playing = input('Do you want card? ')
	if keep_playing.lower() == 'yes':
		card = randrange(2, 11)
		print(card)
		points += card
	elif keep_playing.lower() == 'no':
		break
	else:
		print('Yes or no?')

if points == 21:
	print('You won!')
elif points > 21:
	print('You lost.')
else:
	print('You missed it by', 21 - points, 'points.')
