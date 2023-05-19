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
