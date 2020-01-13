# IDEAS ON IMPLEMENTING THIS

## GLOBAL VARIABLES

- lives
- score
- time left
- power-ups active
- speed of the game

## CLASSES

### 1. PERSON

This is a base class for the charcters in the game  

He has the following attributes:

- x position on the screen
- y position on the screen
- height
- width
- character for filling him/her/it

and the following functions:

- initialize itself
- render itself to the screen
- kill itself

### 2. PLAYER

Denotes the Mandalorian who is controlled by the player.

He inherits from `PERSON` and has the following attributes:

- bullets

and the following functions:

- move left
- move right
- move up
- move down
- gravity
- Shoot bullets
- be attracted by the magnet

### 3. SHIELDED PLAYER

He inherits from `PLAYER` and has the following extra functions:

- remove shield

### 3. BOSS

Denotes the boss enemy Viserion, the flying dragon

He inherits from `PERSON` and has the following attributes:

- ice balls
- lives

and the following functions:

- throw ice balls
- follow along y axis
- die

### 4. OBSTACLES

A base class that denotes all the possible obstacles in the game

It has the following attributes

- length
- width
- x position
- y position
- shape

and the following functions:

- Display it

### 5. FIRE BEAMS

Denotes the large yellow laser/fire beams

It inherits from OBSTACLES and has the following attributes:

- length
- orientation

and has the following functions

- check if it is colliding with the player
- be destroyed

### 6. MAGNET

Denotes a magnet that can appear out of nowhere and attract the player

It inherits from OBSTACLES and has the following attributes

- length
- width
- force of attraction
- is on screen

and the following functions

- attract the player
- be destroyed

### 7. COINS

Denotes moneyy!

It inherits from OBSTACLES and has the following attributes

- value
- how it looks like

and the following functions

- be collected
- display it

### 8. POWER-UPs

Denotes power-ups: shield and speed-boost

It inherits from OBSTACLES and has the following attributes

- value
- how it looks like
- type of the power-up
- time for which it stays active

and the following functions

- be collected
- display it

### 9. SCENE

Creates the background beautiful stuff :)

It has the following attributes

- width
- height
- scene start index

and the following functions

- create env effects (like a beautiful background filled with trees)
- create random obstacles
- create random enemies
- create coins
- create powerups

## FEATURES

(to be built later)

## THINGS LEFT TO DO

[x] Collision with beams
[ ] power-ups
[x] globalize the speed of the game
[x] bullets
[ ] destroy beams
[ ] main boss guy
[x] display the life remaining
[x] display the time remaining
[ ] display the powerups active
[ ] Bossy
[ ] make life red in color with white bg
[ ] make time left green in color with white bg
[x] bullets (again)
[ ] make the hero white backgrounded with cyan trim color
[x] limited and displayed the number of bullets
