# setup

- open [index.html](index.html)
  - click setup
    - if this doesn't work make sure you can use showDirectoryPicker
  - select the folder containing the wordlists
    - when returning to the page it will remember the folder you have selected
  - when clicking start, it will choose 6 unique wordlists, and remove them from the list of available lists
    - when reloading they will again become available to pick from
  - when a word is shown, by clicking on a box, that word will not be a valid word to pick from that word list until all words are cleared by clicking the clear used words button
    - this data is not cleared on reload
  - if a wordlist has less than 7 words left unused it will not be treated as a valid wordlist, which will be shown by the loaded wordlists count shown when first loading in a new folder or reloading the page
  - click start to generate the pyramid
  - click the box to show the words in the box
    - after doing so, there will have 7 words appear on the left
    - when the other person guesses a word correctly, lclick
    - if you decide to pass, rclick
    - the words must be guessed in order, the current word is highlighted in white, skipped words are highlighted in red, and correct words are highlighted in green
    - if you skip words but reach the end with time left you will have a chance to retry the skipped words, but are unable to skip the words again
  - you can set the time limit for each round by changing the time limit in the timer time input 

- open the [scoresheet](./scoresheet.html)
  - add the players names in the top row
  - whenever a player scores add their score to the next box below their namme, after doing so the input will lock and spawn a new one below to continue adding scores

- the scoresheet will add each players scores and display each players totals and rank them accordingly
- the scoresheet has icons for 1st, 2nd, and 3rd place

- when adding custom word lists make sure that each word is on its own line inside a file called BOX_NAME inside the selected folder
