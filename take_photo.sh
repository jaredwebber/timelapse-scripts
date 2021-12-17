#!/bin/sh

HOME=/root
LOGNAME=root
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/root

cd /media/pi/SSD/Images
gphoto2 --camera "Canon EOS 1200D" --capture-image-and-download --filename "%Y.%m.%d.%H.%M.%S.CR2"