# exiTor

```txt
 ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌            ▐░▌ ▐░▌       ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌        ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌    ▐░▌         ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌        ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ 
▐░▌            ▐░▌ ▐░▌       ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌  ▄▄▄▄█░█▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                            
                Check if an IP address is a Tor exit node
                        By L4ser Security Labs
                                v1.0.0
```

- - -
Check if an IP address is a Tor exit node

A Tor exit relay, or exit node, is the computer through which your traffic emerges onto the internet to reach its destination. If you load a Web site through Tor, the web server will think the exit node’s IP address is your own computer’s IP address.

ExiTor allows you to verify if an IP address is a valid tor exit node.

## Install on Linux, Mac OS, Windows

```bash
  git clone https://github.com/lagosnomad/exiTor.git
  cd exiTor
  pip3 install -r requirements.txt
```

## Usage

```txt
usage: exitor.py [-h] [-ip IP]

Check if an IP address is a Tor exit node

optional arguments:
  -h, --help  Shows this message and exits
  -ip IP      IP Address
```

## Examples

```bash
  # Show exiTor help message
  python3 exitor.py -h

  # Verify an IP address 
  python3 exitor.py -ip 5.2.69.5
```
