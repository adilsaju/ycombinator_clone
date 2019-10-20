#!/bin/bash
#schedule the scrape.py script for interval of 5 min using cron
echo "*/5 * * * * cd ~/ycombinator_clone/ && source my_env/bin/activate && python manage.py runscript scrape" | sudo tee -a /var/spool/cron/crontabs/$(whoami)