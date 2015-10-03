# Match the Hash [(Asciicast)](https://asciinema.org/a/7a4glsy7gcvpphy98z97wnh55)
## Problem
We are given a zip file with many images in it, and instructions to submit an MD5
hash.

## Process
Given the name of the problem, it is likely that we are supposed to find the MD5 of
matching/duplicate files. That's easy enough to do with a few shell commands. We used
the `md5sum` tool along with `sort` piped to `uniq -c` to find the duplicate/non-unique
hash.

## Solution
The solution is the MD5 hash that appears twice, `253dd04e87492e4fc3471de5e776bc3d`.
