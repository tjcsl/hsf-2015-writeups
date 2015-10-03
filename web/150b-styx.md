# Styx
## Problem
A question is posed: "What is my favorite song?" In addition, a hint alluding to
Google's spidering robot is provided.

## Process
We can assume the answer to the question is probably a Styx song, given the problem
title. The hint made us think about the web spidering process, and a file often
checked in that process (robots.txt). We found the flag at `https://hsf.csaw.io/robots.txt`.

## Solution
Run `curl https://hsf.csaw.io/robots.txt` or otherwise fetch the page to get the
flag: `flag{dom0_arigato_mr_roboto}`.
