# GG Filesystem [(Asciicast)](https://asciinema.org/a/3wre7ocysbzyr5lagsia56z2v)
## Problem
We are given a zip file with an ext3 filesystem image inside.

## Process
If the flag is somewhere on the filesystem in clear-text, `strings` is likely to find
it. We ran `strings` and `grep`ped for "flag" and found the flag.

## Solution
The flag is found in the filesystem image: `flag{thanks_extundelete}`.
