import random
print('I am thinking of a number between 1 and 10.')
answer = random.randint(1, 10)
guess = -1 # Give it a dummy value.
tries_left = 5

while guess != answer and tries_left > 0:
  guess = int(raw_input('What\'s the number? '))
  tries_left = tries_left - 1  # they've just used a try

  if guess != answer:
    
    if guess < answer:
      print "%d is too low" % guess
    elif guess > answer:
      print "%d is too high" % guess

    if tries_left == 0:
      print "You ran out of guesses!"
    else: 
      print "You have %d guesses left" % tries_left

  else:
    print 'You win!'

