import sys
import random


sys.stdout.write('Write max number\n')
max_num = int(sys.stdin.readline().strip())

sys.stdout.write('Write min number\n')
min_num = int(sys.stdin.readline().strip())

if min_num >= max_num:
    print('The number must be bigger than the min number')
    sys.exit()

for count in range(5):
    ans_num = random.randint(min_num, max_num)

    sys.stdout.write('Guess the number\n')
    guess_num = int(sys.stdin.readline().strip())

    if guess_num == ans_num:
        print('You are correct!!')
        break
    else:
        print(f'You are wrong. The correct number was {ans_num}')
        print(f'You can try {4 - count} more left')

else:
    print('You cannot try any more')