# heya frens

i made dis lil CLI client for www.myriad.social and you can install it w/ one line on your Ubuntu / Debian-based linux.
Just open terminal and type one of dese commands:

```
curl -sSL https://myriad.social/cli | bash
```

or

```
wget -qO- https://myriad.social/cli | bash
```

Basic tings are working, including anonymous login, reading posts, filtering by username, writing posts, as well as Twitter imports.
Images are rendered in monochrome ASCII and rich text is simplified to regular console text.
It's retro af and pretty quick.

UPDATE: I haf installed the self-hosted Myriad AI here. Just enable after logging in if you wan to use it. 

WARNINK: This will install a relatively large LLM on your system.\n Make sure you have around 8 GB of free RAM, and either an NVIDIA GPU or an 8-core CPU. \nTested on decenter-1: Intel Evo i7, 16GB RAM, Intel GPU & decenter-2: Intel i9 / 32 cores, 32GB RAM, NVIDIA RTX 4070 Ti.

To do:

- comments
- likes / dislikes
- timelines
- friending
- trending
- curses integration so looks prettier
- Myriad AI integration
- crypto wallet logins (right now you have to add an email login to yer http://app.myriad.social account if you want to use dis CLI.)


This does NOT work on WSL or Termux yet becoz of sum dependencies, and may still break in distros that r non-GNOME. Alpha software, try at own risk, etc.
Gonna try fixing sum of da more egregious errors dis weekend

Anyway enjoy if u manage to run it, ping me if you haf any qs.
