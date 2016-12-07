#!/usr/bin/python2.7
# -*-coding:utf-8-*-

import os
import sys
os.chdir('/home/ankiy/log')
if '/home/ankiy/log' not in sys.path:
    sys.path.append('/home/ankiy/log')
"""
inotify != pyinotify

"""

from inotify import adapters
from inotify import constants

# 要监控的文件路径
PATH = '/home/ankiy/log/detect_folder/sys_statistic.json'

def main():
    i = adapters.Inotify()

    i.add_watch(PATH, mask= constants.IN_ALL_EVENTS)

    try:
        for event in i.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event

                print "WD=(%s) MASK=(%s) COOKIE=(%s) LEN=(%s) MASK->NAMES=%s WATCH-PATH=[%s] FILENAME=[%s]" \
                      %(header.wd, header.mask, header.cookie, header.len, type_names,watch_path, filename)

                if type_names == ['IN_MODIFY']:
                    print "The file is modified."
    except KeyboardInterrupt:
        print "WATCH END"

    finally:
        i.remove_watch(PATH)

if __name__ == '__main__':
    main()