fronter can be used to test a list of domain names against your CDN endpoint to validate if they are frontable. 

Censys.io is nice way to find possible frontable domains, especially if you use their API.

<p align="center">
  <kbd><img src="https://i.imgur.com/oca74rs.png"></kbd>
</p>

## Usage
1. Create a list of domain names
~~~
$ cat domains.txt 
www.suzuki.kanagawa.jp
cdn-atfujita-verizon.azure.aaq.jp
cdn.ambitenergy.jp
cdn.msjpdsi.com
cdn2.msjpdsi.com
images.suzuki.kanagawa.jp
jp.amari.com
jp.aorus.com
jp.mosaic-collection.com
jp.shama.com
jp.trip-fever.com
support.kinq.jp
td-cdn.aaq.jp
tile.cdn.mierune.co.jp
~~~


2. Run fronter 
~~~
python3 fronter.py -d rip-derbycon.azureedge.net -f domains.txt
[+] CDN Endpoint: rip-derbycon.azureedge.net

[+] Testing: www.suzuki.kanagawa.jp
[+] Testing: cdn-atfujita-verizon.azure.aaq.jp
[+] Testing: cdn.ambitenergy.jp
[!] Testing: cdn.msjpdsi.com
[+] Testing: cdn2.msjpdsi.com
[!] Testing: images.suzuki.kanagawa.jp
[+] Testing: jp.amari.com
[+] Testing: jp.aorus.com
[+] Testing: jp.mosaic-collection.com
[+] Testing: jp.shama.com
[+] Testing: jp.trip-fever.com
[!] Testing: support.kinq.jp
[+] Testing: td-cdn.aaq.jp
[+] Testing: tile.cdn.mierune.co.jp

[+] Done!
Login to VPS and find your frontable domains
cat /var/log/apache2/access.log | grep python-requests | awk -F"canary-" {'print $2'} | cut -d " " -f 1 | sort -u
~~~


3. Login to your VPS to see what domains are frontable 
~~~
$ cat /var/log/apache2/access.log | grep python-requests | awk -F"canary-" {'print $2'} | cut -d " " -f 1 | sort -u

cdn2.msjpdsi.com
cdn.ambitenergy.jp
cdn-atfujita-verizon.azure.aaq.jp
jp.amari.com
jp.aorus.com
jp.mosaic-collection.com
jp.trip-fever.com
td-cdn.aaq.jp
tile.cdn.mierune.co.jp
www.suzuki.kanagawa.jp
~~~
