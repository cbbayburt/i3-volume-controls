#!/bin/bash
# This script prepends the output from i3kblayout to i3status output
# Further text may be appended in JSON format

i3status --config $HOME/.i3status.conf | while :
do
    read line
    layout=$($HOME/.i3/scripts/i3kblayout -q)
    # The keyboard icon is from FontAwesome
    layout="[{\"full_text\": \" $layout\"},"
    echo "${line/[/$layout}" || exit 1
done
