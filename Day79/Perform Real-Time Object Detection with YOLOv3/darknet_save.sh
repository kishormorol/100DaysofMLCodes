#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "ERROR! Usage: help/video filepath"
    exit
fi

./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights $1 -prefix pictures
avconv -i pictures_%08d.jpg video.mp4
avconv -i video.mp4 -i $1 output.mp4

rm pictures_*.jpg video.mp4
