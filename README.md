```
@@@@@@@  @@@@@@@@ @@@@@@@@ @@@@@@@   @@@@@@ @@@@@@@@  @@@@@@ 
 @@!  @@@ @@!      @@!      @@!  @@@ !@@     @@!      @@!  @@@
 @!@  !@! @!!!:!   @!!!:!   @!@@!@!   !@@!!  @!!!:!   @!@!@!@!
 !!:  !!! !!:      !!:      !!:          !:! !!:      !!:  !!!
 :: :  :  : :: ::: : :: :::  :       ::.: :  : :: :::  :   : :

usage: deepsea.py [-h] [--sid SID] [--type TYPE] [--target TARGET] [--list LIST] [--proxy PROXY]

optional arguments:
  -h, --help       show this help message and exit
  --sid SID        value of your PHPSESSID cookie
  --type TYPE      type to look for, default is email. possible values: ['email', 'username', 'name', 'ip', 'password',
                   'uid']
  --target TARGET  target to search for
  --list LIST      file with targets separated by newlines
  --proxy PROXY    Set Tor proxy (default: 127.0.0.1:9050)
```

client for deepsearch leak db. while pwdn is down, this seems like the best alternative : )

start tor, pass your PHPSESSID cookie and go
