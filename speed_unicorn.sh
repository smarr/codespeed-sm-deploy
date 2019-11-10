#!/bin/bash
set -e
NAME=$1
LOGFILE=/var/log/gunicorn/${NAME}.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3

# user/group to run as
USER=www-data
GROUP=www-data
cd /home/www-data/${NAME}
source /home/www-data/speed/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec /home/www-data/speed/bin/gunicorn wsgi:application -w $NUM_WORKERS \
    -b 127.0.0.1:8076 \
    --user=$USER --group=$GROUP --log-level=warning \
    --log-file=$LOGFILE 2>>$LOGFILE
