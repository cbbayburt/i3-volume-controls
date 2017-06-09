# i3controls #

## Features ##
 - Volume, brightness and keyboard layout control key bindings.
 - Notification messages for volume level and keyboard layout using **dunst**.
 - Status indicators for volume level and keyboard layout for either **i3status** or
   **py3status**.

## Requirements ##
 - python >= 2.7
 - [i3wm](i3wm.org)
 - [py3status](github.com/ultrabug/py3status)
 - [dunst](github.com/dunst-project/dunst)

## Installation ##
1. Copy the files in `scripts` folder into `~/.i3/scripts` directory (create if it doesn't exist),
  and grant exec permissions.

2. Append the lines in `i3config.example` to your i3 config file (`~/.i3/config`).

3. (If you want to use py3status) append the lines in `i3status.conf.example` to your
  `i3status.conf` file.
