# Secret Meeting [(Asciicast)](https://asciinema.org/a/agfjixq1w5ew3wh79jwfeadou)
## Problem
We are given a zip file with a JPEG image, and told that the flag format is
`make_model` (where make and model are those of the camera that took the picture).

## Process
Camera make and model are found in the EXIF data of an image. Knowing this, we ran
`exiftool` on the image and found what we wanted:

```
Make                            : iPhone
Camera Model Name               : Samsung
```

## Solution
Substituting values into the flag format, the flag is `iPhone_Samsung`.
