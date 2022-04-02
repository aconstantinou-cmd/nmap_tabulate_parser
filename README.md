# nmap_tabulate_parser

`python3 nmap_tabulate_parser.py -f nmap`

```
IP               Port  Protocol    State     Service
-------------  ------  ----------  --------  ----------------
192.168.0.1        21  tcp         closed    ftp
192.168.0.1        22  tcp         closed    ssh
192.168.0.1        23  tcp         closed    telnet
192.168.0.1        25  tcp         closed    smtp
192.168.0.1        26  tcp         closed    rsftp
192.168.0.1        53  tcp         open      domain
192.168.0.1        80  tcp         open      http
192.168.0.1        81  tcp         closed    hosts2-ns
192.168.0.1       110  tcp         closed    pop3
```

`python3 nmap_tabulate_parser.py -f nmap --open`

```
IP               Port  Protocol    State    Service
-------------  ------  ----------  -------  --------------
192.168.0.1        53  tcp         open     domain
192.168.0.1        80  tcp         open     http
192.168.0.22       22  tcp         open     ssh
192.168.0.42      135  tcp         open     msrpc
192.168.0.42     3389  tcp         open     ms-wbt-server
192.168.0.47     8888  tcp         open     sun-answerbook
192.168.0.79     8888  tcp         open     sun-answerbook
192.168.0.136      53  tcp         open     domain
192.168.0.145    8888  tcp         open     sun-answerbook
192.168.0.146    8888  tcp         open     sun-answerbook
192.168.0.177      53  tcp         open     domain
192.168.0.23       22  tcp         open     ssh
192.168.0.23      111  tcp         open     rpcbind

```
