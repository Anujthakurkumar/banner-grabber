# Banner Grabber

A simple Python TCP banner grabbing tool using the standard `socket` library.

## Usage
    python3 banner_grabber.py

Enter the target IP and port when prompted.

## Example
    $ python3 banner_grabber.py
    what ip address do u want to collect banner from ? 192.168.24.132
    what port do u wan tro collect banner from ? 22
    b'SSH-2.0-OpenSSH_9.6\r\n'

## Notes
Works on services that send a banner on connect (SSH, FTP, SMTP).

## Disclaimer
For educational use and authorized testing only (your own lab or systems you
have written permission to test).
