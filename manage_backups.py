#!/usr/bin/env python
import requests
from argparse import ArgumentParser
from dnacentersdk import api
from dnacentersdk.exceptions import ApiError
import logging
import csv
import json
from  time import sleep, time, strftime, localtime
from dnac_config import DNAC, DNAC_USER, DNAC_PASSWORD
logger = logging.getLogger(__name__)

class TaskTimeoutError(Exception):
    pass

class TaskError(Exception):
    pass

def format_time(secs):
    fmt = "%Y-%m-%d %H:%M:%S"
    timestr = strftime(fmt,localtime(secs))
    return timestr

def show_backups(dnac):
    #logger.debug(data)
    result = dnac.custom_caller.call_api(method="GET", resource_path="api/system/v1/maglev/backup")
    for l in result.response:
        formatted = format_time(l['start_timestamp'])
        print("{}:{}:{}:{}".format(l['backup_id'],l['description'],l['start_timestamp'], formatted))

def delete(dnac, delete_id):
    result = dnac.custom_caller.call_api(method="DELETE", resource_path="api/system/v1/maglev/backup/{}".format(delete_id))
    print(result)

def purge(dnac, olderthan):
    now = time()
    result = dnac.custom_caller.call_api(method="GET", resource_path="api/system/v1/maglev/backup")
    for l in result.response:
        backup_time = l['start_timestamp']
        if backup_time + olderthan < now:
            formatted = format_time(l['start_timestamp'])
            backup_id = l['backup_id']
            print('delete {} {}'.format(backup_id, formatted))
            delete(dnac, backup_id)

if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('-v', action='store_true',
                        help="verbose")
    parser.add_argument('--delete',  type=str,
                        metavar='backup_id',
                        help='backup id to delete')
    parser.add_argument('--older',  type=int,  nargs='?',
                        const=604800,
                        metavar='older_than_seconds',
                        help='delete backups older than x seconds, default 1 week')
    args = parser.parse_args()
    args = parser.parse_args()

    if args.v:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.debug("logging enabled")
    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    dnac = api.DNACenterAPI(base_url='https://{}:443'.format(DNAC),
                                username=DNAC_USER,password=DNAC_PASSWORD,verify=False,debug=True)
    if args.delete:
        delete(dnac, args.delete)
    elif args.older:
        purge(dnac, args.older)
    else:
        show_backups(dnac)
        


