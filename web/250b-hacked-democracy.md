# Our Democracy Has Been Hacked [(Asciicast)](https://asciinema.org/a/5eczh34drnsn3w7yo6euwmbxn)
## Problem
The goal of this problem is to help Elliot find the code for his malware on a site
he used to use to store it. However, he has forgotten the path. We are given a URL
as a starting point.

## Process
The first thing we did was, of course, look at the webpage. It is a picture of a cat,
along with the text "Hello friend." It didn't seem to be very helpful, so we moved on.

We thought about common places where code might be stored. One of these places would be a
source control directory, for example, `.git` for the Git VCS. We opened
`http://54.152.37.157/.git/` in a web browser and found a directory listing. We then
recursively fetched the repository with `wget -r http://54.152.37.157/.git/`, so we
could clone it locally. In order to prepare for that, we removed all directory listings
with `find -type f -name 'index.*' | xargs rm`. Following that, we could `git clone` our
downloaded repository.

We looked around a bit, but found no helpful code. We decided to look at `git log`.
We found the flag in commit `8c71f479d8fb14ea538daa83e26530e0ac43c498`, which was
right after the initial commit.

## Solution
The flag is in the commit message for commit `8c71f479d8fb14ea538daa83e26530e0ac43c498`,
which can be obtained by `git log 8c71f479d8fb14ea538daa83e26530e0ac43c498`. The flag
is `flag{nothing_says_holidays_like_a_git_log}`.
