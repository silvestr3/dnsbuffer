# Receives a list of subdomains, resolves them to their IP addresses and returns a text file with 'host : ip' listed

#!/bin/bash

list=$(cat $1)
touch output.txt

for host in $list
do
        ip=$(ping -c1 $host 2>/dev/null | grep PING | awk -F'[()]' '{print $2}')
        echo "$host : $ip"
        echo "$host : $ip" >> output.txt
done
