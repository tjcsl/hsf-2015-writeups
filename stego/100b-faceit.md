# Face It [(Asciicast)](https://asciinema.org/a/dtgeg0c8b62aww3t7i9dkl0ga)
## Problem
We are given a PDF essay on the topic of facial recognition.

## Process
We assumed the flag was somewhere in the PDF. Searching for the string "flag"
confirmed our suspicions, but we were unable to see the flag, as it was behind
an image. We used the `pdftotext` tool from the `xpdf` library in order to extract
the text from the image, then `grep`ped for the string `flag`.

## Solution
Extract the text from the PDF, and search for the string `flag`. The flag is `rec0gn1z3`.
