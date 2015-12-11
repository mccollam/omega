Quick and dirty hack to list and summarize wifi access points

Prerequisites
-------------

You'll need to install python and wireless tools:
    opkg install python-light wireless-tools

Attach a USB storage device and mount it at /mnt (or wherever you prefer) to
avoid running out of disk space.

Gathering information
---------------------

Gather information with iwlist (which can be run multiple times):
    while true ; do iwlist wlan0 scan >> /mnt/results

Parsing
-------

Create a line-oriented record with parse.py:
     ./parse.py

(NB: this is currently hard-coded to look for a file called "results")

Displaying
----------

Use 'summary' or 'summary-oled' to display the results:
    ./parse.py | summary
    ./parse.py | summary-oled

summary-oled will display the summary information to the OLED display (useful
to run in a loop while using the Omega and scanner while not at a computer)
but does require that the OLED display be initialized before use.
