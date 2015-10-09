# Back to Base6
## Problem
We are given a zip containing the text
```ZmxhZ3tp
745f7761735f
104 105 115 95 102 108
011000010110011101011111011011010111001001011111
NNZGCYTTL4======
<~Blm^+@<5dnF_tSDEaNs,0OK)ZI/~>
```

## Process
Given the problem name, these are probably encoded using different bases. The first five are quite quickly recognizable as Base64, Hexadecimal, Ascii, Binary, and Base32. Googling for more base-based encodings, we discovered Ascii85, which produces output similar to the last line of our text. Decoding each line, individually, we find the flag.

## Solution
The flag was `flag{it_was_his_flag_mr_krabs_it_was_numb3r_un0_y0}`.
