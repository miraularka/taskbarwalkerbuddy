# Taskbar Walker Buddy
Inspired by a script on Acmlmboard/board2

# Taskbar Walker Buddy
A forum I used to visit back in the 2000's had a fun little javascript plugin of a goomba walking across the bottom of the browser window. You could click them to squish 'em. There was nothing to gain by doing this other than a little seratonin. I took that concept with me to a website I helped write back in 2017. My version had a slew of characters related to the community of the website as well as the ability to have multiple 'walkers' at any time. You would gain a coin by clicking and poofing them, some offering more than one. The coins could be earned in other ways as well and held their own community driven significance.

This is a somewhat recreation of that. Starting out it is merely randomly selected walkers; however instead of a website they roam your desktop. They should automatically detect the height of your taskbar and start moving along from one end to the other. They will go offscreen if you allow them, or you can end their journey early by clicking them. Right-clicking the currently active walker will open an About window with a few settings for you to configure.

## Adding New Walkers
Everytime the program is run it will initialize by loading all of the spritesheets within the /img/ directory. For every spritesheet you can expect to have one additional walker. Each spritesheet is divided in three rows of 32px columns (96px height total). Each column is also 32px wide to construct a square which constitutes a frame of animation. These animations can theoretically be as long and convoluted as you like. Top row is for moving LEFT, middle row is for moving RIGHT while bottom row is for when the walker is clicked (and resets to a another).

Note that the included spritesheets are meant as placeholders as well as templates to create more.


## Possible Additions
* Sounds - including individual and toggles
* Consume Mode - you won't see a repeat walker until all others have been clicked
* Multiple walkers!

Hope you enjoy it!
~Mirau
