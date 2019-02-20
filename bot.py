'''
bot.py template for PRAW4

This file will be imported by all bots, and provides a standard way to log in.

You should never place this file in a git repository or any place where it will
get shared.

The requirements for this file are:

1   A function `anonymous` with no arguments, which returns a `praw.Reddit`
    instance that has a Useragent but is otherwise anonymous / unauthenticated.
    This will be used in bots that need to make requests but don't need any
    permissions.

2   A function `login` with optional parameter `r`, which returns an
    authenticated Reddit instance.
    If `r` is provided, authenticate it.
    If not, create one using `anonymous` and authenticate that.
    Either way, return the instance when finished.

The exact workings of these functions, and the existence of any other variables
and functions are up to you.


I suggest placing this file in a private directory and adding that directory to
your `PYTHONPATH` environment variable. This makes it importable from anywhere.

However, you may place it in your default Python library. An easy way to find
this is by importing a standard library module and checking its location:
>>> import os
>>> os
<module 'os' from 'C:\\Python36\\lib\\os.py'>

But placing the file in the standard library means you will have to copy it over
when you upgrade Python.

If you need multiple separate bots, I would suggest creating copies of this file
with different names, and then using `import specialbot as bot` within the
application, so that the rest of the interface can stay the same.
'''

import praw

CONTACT_INFO = 'daniel.sapkota15@my.northampton.ac.uk'
USERAGENT = 'xxx'
APP_ID = 'QESJL_MX8VryXw'
APP_SECRET = '33O4_jNduldzER_CGhg4qnqyEnY'
APP_URI = 'http://localhost'
APP_REFRESH = '32824298-NV8J767V1DNVgHiOQGTUskjI0cQ'
# https://www.reddit.com/comments/3cm1p8/how_to_make_your_bot_use_oauth2/

def anonymous():
    r = praw.Reddit(
        user_agent=USERAGENT,
        client_id=APP_ID,
        client_secret=APP_SECRET,
    )
    return r

def login(r=None):
    new_r = praw.Reddit(
        user_agent=USERAGENT,
        client_id=APP_ID,
        client_secret=APP_SECRET,
        refresh_token=APP_REFRESH,
    )
    if r:
        r.__dict__.clear()
        r.__dict__.update(new_r.__dict__)
    return new_r