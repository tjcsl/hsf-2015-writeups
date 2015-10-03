# Do Not Support [(Asciicast)](https://asciinema.org/a/ahmxra8ru7d0ujx2ip5sh1et3)
## Problem
We are given a domain name `cyber-ninja.xyz` and asked to find information about
it.

## Process
We browsed to the web site http://cyber-ninja.xyz/ but found a parked domain page.
We then realized that the first letter of each word in the problem name gave us
the solution: DNS. We looked at the `TXT` records of the domain and found our flag.

## Solution
The flag is the `TXT` record of cyber-ninja.xyz: `flag{are_you_secretly_a_ninja?}`.
