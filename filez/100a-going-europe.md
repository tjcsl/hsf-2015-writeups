# Club Going Europe on a Tuesday [(Asciicast)](https://asciinema.org/a/9xky4233jr8qze9fgl2dylvcf)
## Problem
We are given a zip file with a note about reading the dictionary. The zip file contains
a password-protected zip file with a single file "flag.txt".

## Process
Given the mention of a dictionary, we assumed that we should attempt a dictionary attack
on the zip file password. We did this using `/usr/share/dict/cracklib-small`. Once successfully
cracked, we were unable to unzip the file, and `flag.txt` contained the flag.

## Solution
The flag is the text of flag.txt when hungry.zip is extracted with password "turkey":
`flag{dont_hurt_me_john}`.
