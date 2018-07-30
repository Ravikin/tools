#!/bin/bash
#TheRavikin 2018
#theravikin.pl

DISK="/dev/sda"
DNAME=$(echo ${DISK} | awk -F'/' '{print $NF}')
DATE=$(date +%s)

RS=$(iostat -dx ${DISK} | grep ${DNAME} | awk '{print $4}')
WS=$(iostat -dx ${DISK} | grep ${DNAME} | awk '{print $5}')


# timestamp in epoch | read i/o per sec | write i/o per sec
echo -e "${DATE} | ${RS} | ${WS}" >> iop.log
exit 0;
