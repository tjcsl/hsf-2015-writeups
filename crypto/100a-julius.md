# Julius [(Asciicast)](https://asciinema.org/a/02s9diy99x10uw80bs53217cr)
## Problem
We are given an obfuscated string that looks like a flag: `synt{pnrf4e_jbhyq_or_ce0hq}`.

## Process
Given the problem name, this is probably a Caesar cipher. The most common variant of
this in CTFs seems to be ROT13, so we tried that in a Python shell, using the `codecs`
module.

## Solution
The solution is the rot13 encoded problem text `flag{caes4r_would_be_pr0ud}`.

