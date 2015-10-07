# Where is My Key
## Problem
We are given a zip file containing the code for a [encryptor program](500a-where-is-my-key/encryptor.c), [a message](500a-where-is-my-key/message_1), [the encrypted version of that message](500a-where-is-my-key/message_1.enc), and [a different encrypted message](500a-where-is-my-key/message_2.enc).

## Process
We first take a look at the source [here](500a-where-is-my-key/encryptor.c).

This is the important part of the program:

```c
char k[] = "CENSORED";
	char c, p, t = 0;
	int i = 0;
	while ((p = fgetc(input)) != EOF) {
		c = (p + (k[i % strlen(k)] ^ t) + i*i) & 0xff;
		t = p;
		i++;
		fputc(c, output);
	}
	return 0;
```

The program simply takes a input file and encodes it using the string k. Our first step is to recover this string.

Looking at the code above, we can see that we are reading a character p from the input file and writing a character c to the output file. We have a plaintext/ciphertext pair! so we can simply solve for the characters in k.

```python
stng= ""
import codecs
inp="Hi! This is only test message."
out= codecs.decode("9E 97 40 81 D0 BC 93 B2 98 FF E7 C3 4E 31 69 5F 35 E1 E3 DC 09 EA A3 A0 C3 FA 05 52 A6 53".replace(" ",""), "hex")
c, p, t = 0, 0, 0;
k=""
for i in range(len(inp)): 
	p=ord(inp[i])
	c=ord(out[i])
	k+=chr(((c-i*i-p)^t) & 0xff) #all 0xff does is truncate the value
	t=p
print(k)
```

This prints the value `VeryLongKeyYouWillNeverGuessV`. I assumed the V was just from wrapping, and let `k="VeryLongKeyYouWillNeverGuess"`

Then, the next step is straightforward. We need to find plaintext characters that encode to their respective ciphertext characters in the second encoded message. 

```python
stng= ""
import codecs
out= codecs.decode("A4 95 82 88 59 D2 97 9B 8A B5 16 E8 05 C9 AE 6A 6F 97 E1 CD C2 72 52 A5 70 19 1C 55 B3 BE 07 4B 89 AE BD 32 C3 EB 32 81 6A 4F 95 73 55 6D DA 23 24 0C 44 B5 0B 35 CD 8A DC 1B 9E 32 7A 53 67 F7 B2 0D 81 1F 46 4C BC 4D 7A 9F FF A7 FA 69 64 F0 33 63 DE 01".replace(" ",""), "hex")
c, p, t = 0, 0, 0;
k="VeryLongKeyYouWillNeverGuess"
for i in range(len(out)): 
	for j in range(1,255):
		p=j
		if((p + (ord(k[i % len(k)]) ^ t) + i*i) & 0xff == ord(out[i])):
			stng+=chr(p)
			t=p;
			break;
print(stng)
```

Running this gives us the flag. 
## Solution
The message decrypts to`Nice job! You solved the challenge. Here is your flag: flag{3ncrypti0n_f0r_th3_w1n}`.

