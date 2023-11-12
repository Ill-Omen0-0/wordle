# WORDLE GAME CLONE
## Video Demo: [youtube link](https://youtu.be/FD-NmM2AAWs)
## Description:
Well the title is pretty self explanatory, my 'CS50 FINAL PROJECT' is a Wordle clone implemented using HTML, CSS, JS and Flask.
### how to run
load the all the files as it is, in the terminal cd to the project directory and type 'flask run' and open the link that appears in the terminal window.
### About Wordle
The Worlde is a famous game where you are supposed to predict a 5 letter given 6 chances.
### Rules
The rules are as follows:
1. You are supposed to guess the 5 letter hidden word(well not exactly if you click inspect on the webpage I made put the correct/hidden word in the console - for testing purposes).
2. You have limited amount of guesses, 6 tries.
3. Each time you guess a word, the letters will be highlighted/colored to provide hints so you can make better guess next try.
Those would follow the following color code:
    - Green: Correct letter in the correct position.
    - Yellow: Correct letter but in the wrong position.
    - Gray: Incorrect letter.
4. If you guess the word correctly you won!, in case you didn't no worries you can try again with a new hidden 5 letter word.

### Features
- Color clues
- A visual keyboard in the site to assist touch-screens which would be smart phone friendly.
- Dark mode and Light mode option (in the top right of the page there's a toggle for that).
- A pop up showing the results, hidden word, how many tries it took you(if you won that is).
    - a button saying 'reload to play again' which reloads the pages for you in the popup(device friendly I suppose, you could also press 'Ctrl+R').
- A wide variety of words to guess from.
- The guesses must be a valid word, else it would say 'invalid word', but don't worry you can just press the 'Backspace' key to undo the previously inputed letter, just like typing.
- After you enter the fifth letter of the word it won't automatically count it as guess, in order to guess you need to press 'Enter'.
