#!/usr/bin/python

import requests
import json
import sys


def main():
    domain = '.' + sys.argv[1]
    r = requests.get('http://dns.bufferover.run/dns?q=' + domain)

    json_resp = json.loads(r.text)
    output = open('dnsbuffer_'+domain[1:], 'w')

    for data in json_resp['FDNS_A']:
        print data
        output.write(data + '\n')

    output.close()


if __name__ == '__main__':
    main()
