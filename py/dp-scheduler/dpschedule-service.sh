#!/usr/bin/env bash

APP_NAME="dp-schedule"
PID_FILE="/tmp/.dpschedule.pid"

isRunning(){
    #echo "test pid file exist?"
    [  -f "$PID_FILE" ] || return 1
    read PID < "$PID_FILE"
    #echo "test $pid NonZero?"
    [ -n "$PID" ] || return 1
    #echo "test /proc/$pid exist? MAC don't have /proc"
    [ -d "/proc/${PID}" ] || return 1
    #[ -n "`ps axu |grep 'nsched.py' | grep $PID`" ] || return 1
    return 0
}
case $1 in 
    start)
        if isRunning ;then
            echo "$APP_NAME Already Running"
            exit 0
        fi
        
        mv nsched.log nsched.old.log
        #rm -f nsched.log 
        date=`date`
        echo "====================start at $date====================" >> nsched.log
        if nohup /usr/bin/python nsched.py ./conf/nsched.sample.conf --host=127.0.0.1 2>&1 >> nsched.log  &
        #if nohup /usr/bin/python nsched.py ./conf/nsched.sample.conf --host=192.168.7.103 2>&1 >> nsched.log  &
        then
            echo $! > $PID_FILE
            sleep 1
            if isRunning ;then
                echo "Start $APP_NAME Success"
                exit 0
            fi
        fi
        rm $PID_FILE
        echo "Start $APP_NAME Failed "
        exit 1
    ;;

    stop)
        if ! isRunning ; then
            echo "$APP_NAME Not Running"
            exit 0
        elif  kill $(cat $PID_FILE) ;then
            rm $PID_FILE
            echo "Stop $APP_NAME DONE"
            exit 0
        fi 

        echo "TRY HARD... "

        hardtries=0
        while isRunning ; do
            if [ $hardtries -gt 5 ] ;then
                break;
            fi 
            ((hardtries++))
            if kill -9 $(cat $PID_FILE) ; then
                rm $PID_FILE
                echo "Stop $APP_NAME DONE"
                exit 0
            fi
            sleep 1
        done
        echo "Stop $APP_NAME FAILED !"
        exit 1
    ;;

    status)
        if isRunning ; then
            echo "$APP_NAME is running."
        else
            echo "$APP_NAME is NOT running."
        fi
    ;;

    restart)
        $0 stop
        sleep 2
        $0 start
    ;;

    *)
        echo "Usage: $0 start|stop|restart|status"
esac
