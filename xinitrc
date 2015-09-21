#!/bin/sh
while true; do

    # Clean up previously running apps, gracefully at first then harshly
    killall -TERM matchbox-window-manager 2>/dev/null;
	sleep 2;
    killall -9 matchbox-window-manager 2>/dev/null;

    # Disable DPMS / Screen Blanking
    xset -dpms
    xset s off

    # Start the window manager (remove "-use_cursor no" if you actually want mouse interaction)
	matchbox-window-manager -use_titlebar no -use_cursor no &
done;
