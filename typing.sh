#!/bin/bash

# Initialize score
score=0

# Start the game timer
start_time=$(date +%s)

while true; do
  # Generate a random word
word=$(shuf -n 50 -e a b c d e f g h i j k l m n o p q r s t u v w x y z | tr -d '\n')

  # Display the word
  echo "Type the word or press q to quit:"
  echo "$word"

  # Get user input
  read user_input

  # Check if the user wants to quit
  if [[ $user_input == "q" ]]; then
    break
  fi

  # Compare input to word
  if [[ $user_input == $word ]]; then
    echo "Correct!"
    score=$((score + 1))
  else
    echo "Incorrect. Try again."
  fi
done
