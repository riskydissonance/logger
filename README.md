# logger

Logger command for keeping quick and easy notes on engagements.

## Usage

```
usage: log.py [-h] [-l | -n NEW_LOG | -x | -d | -g GREP] [-s | -f | -m] [message [message ...]]

Add log messages to a custom log.

optional arguments:
  -h, --help            show this help message and exit
  -l, --list-logs       list previous log files
  -n NEW_LOG, --new-log NEW_LOG
                        create a new log file or switch to an old one
  -x, --show-log        display the current log
  -d, --delete-log      delete the current log
  -g GREP, --grep GREP  grep the log for a word or phrase

  -s, --success         add a success log message
  -f, --failure         add a fail log message
  -m, --remember        add a remind me message
  message               the log message
```

* First create a new log file with `log -n <log file location>`:

```
$ log -n ~/work/rt/my-engagement/2020-02-05/log.txt
[+] Log file added: /home/m0rv4i/work/rt/my-engagement/2020-02-05/log.txt
```

* Then log messages with `log <message>`:

```
$ log sent phishing email to AThompson
[+] Log message added to /home/m0rv4i/work/rt/my-engagement/2020-02-05/log.txt.
```

This will append a timestamped log to the file.
Different types of log messages can be added by using the -s (success), -f (failure) or -m (remember) options.

```
$ log -m retrieve dropbox
[+] Log message added to /home/m0rv4i/work/rt/my-engagement/2020-02-05/log.txt.
```

* You can view the whole log with `log -s`:

```
$ log -s
[*] Showing log: /home/m0rv4i/work/rt/my-engagement/2020-02-05/log.txt
[2020-02-05 14:45:03.590915] - sent phishing email to AThompson
[2020-02-05 14:47:16.177236] - got an implant on AThompson's box
```
This will also detail the current log.

* You can also grep the log with `log -g`:

```
$ log -g REMEMBER
[2020-02-06 12:27:17.500479] [REMEMBER] - do something
[2020-02-06 12:43:21.228919] [REMEMBER] - retrieve dropbox
```

* You can delete the current log with `log -d`.
* You can view the present and previous log files with `log -l`:

```
$ log -l
[*] Log files:
/home/m0rv4i/work/rt/my-older-engagement/2020-01-15/log.txt
/home/m0rv4i/work/rt/my-engagement/2020-02-05/log.txt
```

This list is stored in ~/.log-files.

## Shortcuts

The recommendation is to add a bash script for ease of running, e.g. add the below to `/usr/bin` if you clone this to `/opt`:

```
#!/bin/bash

python3 /opt/logger/log.py $@
``` 

For zsh add a function e.g. in your `.zshrc` as the 'log' command already exists for logarithms.

```
function log {
    command python3 /opt/logger/log.py $@
}
```

