#!/bin/sh

cd /media/pi/SSD
gphoto2 --capture-image-and-download --filename "%Y.%m.%d.%H.%M.%S.CR2"