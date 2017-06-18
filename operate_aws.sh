#!/bin/bash

python3 ec2_start.py

# Sleep for 2 minutes. ;)
sleep 2m

python3 ec2_stop.py
echo "Done!"

