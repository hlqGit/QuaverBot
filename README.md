# Quaver Bot
This bot automatically plays quaver by monitoring each lane! It isn't extremely good yet, but can usually do up to a 30 rated song. Depends on the charting obviously.

## Demo Video!
https://youtu.be/hsvOzRJPJt0

## Some Notes:
* A fast scroll speed is ideal. I found the best success rate at around 30-32.  
* You can make some adjustments to my code to get it to work with your system better such as:
  * Adjusting offset in keyboardhandle.py  
  * Changing the region you scan pixels at in main.py
  * Changing the color it looks for in main.py

By default, the flow skin is the only skin you can use with this program without customizing the code.

## Limitations and requirements
### Requirements
This uses a (very scuffed) method that runs a command to enter a key press.  
Is that ideal? No but every time I did it any other way it would break very badly.  
ANYWAYS make sure you have [**xdotool**](https://github.com/jordansissel/xdotool) installed, and you can install all the python requirements with requirements.txt
### [xdotool](https://github.com/jordansissel/xdotool) is an x11 automation tool
It is not compatible with windows or mac. I can make one that is in the future but for now just use linux #archlinux #itsbetter 

### Limitations
So because it isn't very optimized, it struggles badly when hold notes repeat too quickly. Also, extremely fast repetitive notes also mess with it. It just cannot detect the gaps in between the notes and will continue to hold even though it should not. 
## Important:
PLEASE don't use this competitively. I am not responsible for you or your account if you decide to use it and get scores removed and/or your account banned. If you want to use it, you can turn on non-competitive modifiers such as no fail and no scroll velocities.
