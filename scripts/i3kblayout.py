#!/usr/bin/env python

import sys, os, re
import notify
from subprocess import check_output, check_call

def main():
    curLayout = check_output(['setxkbmap', '-query']).split(',')[0]
    curLayout = re.search('layout:\s+(.*)\n?$', curLayout).group(1)

    if len(sys.argv) < 2:
        print 'Usage:'
        print '  i3kblayout [-q | --query]'
        print '  i3kblayout layout1 [layoutN ..]'
        return

    if sys.argv[1] == '-q' or sys.argv[1] == '--query':
        print curLayout.upper()
        return

    allLayouts = sys.argv[1:]
    try:
        nextLayout = allLayouts[(allLayouts.index(curLayout) + 1) % len(allLayouts)]
    except ValueError:
        nextLayout = allLayouts[0]

    check_call(['setxkbmap', '-layout', nextLayout])

    showMsg(nextLayout)

def showMsg(nextLayout):

    idfile = os.getenv('HOME') + '/.i3/.notify_layout'
    if not os.path.exists(idfile):
        os.mknod(idfile)

    mid = open(idfile, 'r').readline()
    if mid == "":
        mid = 0

    mid = notify.notify('layout', mid, 'Layout: ' + nextLayout.upper(), '', '', 2000)
    open(idfile, 'w').write(str(mid))

if __name__ == '__main__':
    main()
