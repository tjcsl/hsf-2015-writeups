# Movie Night
## Problem
We are given a zip file with an mp4 video inside.

## Process
Watching the video, we see that it is fairly normal, up until about 01:33, when
we see text fly across the screen. The text says "zit ysqu of ysqu{ezy_&_eioss}".

We assumed this is a substitution cipher, so we started guessing what the flag could
be, starting with "the flag is flag{":

```
zit ysqu of ysqu{ezy_&_eioss}
the flag is flag{?tf_&_?hill}
```

The only missing letter that makes sense is "c", to get "flag{ctf_&_chill}".

## Solution
The flag is the decoded text flying across the video at 01:33: `flag{ctf_&_chill}`.
