# Andromeda [(Asciicast)](https://asciinema.org/a/8km34e37u3louz9nu59gyygck)
## Problem
We are given a zip file with an image, `andromeda.jpg`, embedded in it.

## Process
Given that this is a lower-level steganography challenge, we are expecting the
flag to be embedded somewhere in the image. As such, we used our old friend `strings`
on the image, and searched the output for the string "flag". This did not initially work,
but we tried it once more using a case-insensitive search and the flag was revealed.

## Solution
The solution can be found by running `strings` on the image and `grep`ping for
the string "flag" case-insensitively. The flag is `naqebzrqn`.
