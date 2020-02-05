# logger

Logger command for keeping quick and easy notes on engagements.

## Usage

```
usage: log.py [-h] [-l | -n NEW_LOG | -s | -d | message [message ...]]

Add log messages to a custom log

positional arguments:
  message               the log message

optional arguments:
  -h, --help            show this help message and exit
  -l, --list-logs       list previous log files
  -n NEW_LOG, --new-log NEW_LOG
                        create a new log file
  -s, --show-log        display the current log
  -d, --delete-log      delete the current log
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

* You can then view logs with `log -s`:

```
$ log -s
[*] Showing log: /home/m0rv4i/work/rt/my-engagement/2020-02-05/log.txt
[2020-02-05 14:45:03.590915] - sent phishing email to AThompson
[2020-02-05 14:47:16.177236] - got an implant on AThompson's box
```
This will also detail the current log.

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

