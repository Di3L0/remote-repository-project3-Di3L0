> Project 3 Design Document

- **Developer**: [Abdiel Quiroz]
- **Collaborator(s)**: [ enter names of collaboratos]


## Algorithmic steps of `password_8chars()` function
- **Input**: 3 strings: `letters`, `caps`, `numbers`
  - a string of  lowercase letters
  - a string of uppercase letters
  - a string of decimal digit characters
- **Output**: a string, representing a passowrd of 8 characters, chosen 
  randomly from the three strings

- **Design**: 
1. Define the accumulator named 'my_password'.  Initialize it with empty list
2. Define all of the possible characters by adding together the lists of letters, caps and numbers and storing them in a variable called 'possibles'
3. Use for loop to run 8 iterations of possible characters (possibles) through the random.choice method of generating random characters (stored as variable 'ran_char'). 
4. Construct a variable called 'my_password1' by taking the variable 'ran_char' andding that variable to 5. Return the characters stored in 'my_password1'.   


## Algorithmic steps of `password_4words()` function
- **Input**: 3 lists of words
  - a list of nouns, a list of verbs, a list of adjectives
- **Output**: a string, representing a password that concatenates 3 words, 
  each randomaly selected from each of the lists

- **Design**: 
1. Define the accumulator as an empty list that is initialized as 'fourwords'
2. Define a variable (called 'password_4words') made up of the lists nouns, verbs and adj added together.
3. Use for loop to run 4 iterations of the range function 
4. The function 'random.choice' will run through the the variable 'password_4words' and store the result in 'ran_string'. 
5. 'ran_string will be added to previously stored items in 'fourwords' to create the accumulating string 'fourwords'.
6. Return 'fourwords'


## Algorithmic steps of `password_4words_better()` funcction
- **Input**: Same as the input for `password_4words()`
- **Output**: Same as the output for `password_4words()`, but some of 
  the letters are replaced with number characters or special characters:
  - 'o' is replaced with '0'
  - 'l' is replaced  '!'
  - 'a' is replaced with '@'
  - 'e' is replaced with '3'
- Hint: Don't redo the work that `password_4words()` does. 

- **Design**: 
1. Initialize the accumulator as an empty string; initialize as 'better_pass'
2. Call 'password_4words' and store it's data inside a newly created variable (callded'newpassword').
3. Run the .replace function on the variable 'newpassword', to replace all of the 'o's with '0' and store that information in 'better_pass'.  
4. Take 'better_pass' and replace all of the 'l' characters with '!' and store the resulting data back into 'better_pass'
5. Take all of the characters 'a' in 'better_pass' and replace them with '@'; store the newly updated information in 'better_pass'
6.  Use the .replace funciton to switch all of the 'e' characters in 'better_pass' for '3' and store the updated information in 'better_pass' 
7. Return the string 'better-pass'