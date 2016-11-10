1. Have `i3` and `dunst` installed.

2. Copy the files in `scripts` folder into `~/.i3/scripts` directory (create if it doesn't exist),
  and grant exec permissions.

3. Append the following lines to `~/.i3/config` file:
    ```
    # Volume controls
    bindsym XF86AudioLowerVolume exec $HOME/.i3/scripts/volume down
    bindsym XF86AudioRaiseVolume exec $HOME/.i3/scripts/volume up
    bindsym XF86AudioMute exec $HOME/.i3/scripts/volume toggle
    ```
