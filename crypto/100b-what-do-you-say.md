# What do you say? [(Asciicast)](https://asciinema.org/a/4jpd1m0eifsfledwhqf25rj92)
## Problem
We are given a very spooky string "doooot dootdootdootdoot dootdoooot dooootdoot dooootdootdoooot dootdootdoot dooootdoooot dootdooootdoot dootdootdoot dooootdootdoooot doot dootdooootdootdoot doot doooot dootdoooot dootdooootdootdoot dooootdootdoot dooootdooootdoooot dooootdooootdoooot doooot dooootdootdoot dooootdooootdoooot dooootdooootdoooot doooot".

## Process
Since there different numbers of "o"s in the "doot"s, we thought this looked like Morse
code. Given that, we used the `hackercodecs` library and some Python to decode it. The
equivalent to a dot is "doot" and the equivalent to a dash is "doooot".

## Solution
The solution is the Morse-decoded string: `THANKSMRSKELETALDOOTDOOT`
