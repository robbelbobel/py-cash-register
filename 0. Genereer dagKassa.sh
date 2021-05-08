#!/bin/bash
cd /home/pi/Desktop/Kassa
echo Naar dagKassa.txt schrijven!
python3 processLog.py
echo Log Genereren klaar!
read -p "Druk op enter om dit scherm te verlaten..."