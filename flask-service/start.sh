#!/bin/bash


DI_INS=python3
APP_NAME=app_service.py
start(){
  is_starting
  if [ $? -eq 0 ]; then
    echo -e "程序: ${APP_NAME} 已经在运行 \033[32m 进程号: ${pid} \033[0m"
  else
    nohup $DI_INS -u $APP_NAME > $(date +'%y%m%d%s').log 2>&1 &
    pids=`ps -ef | grep $APP_NAME | grep -v grep | awk '{print $2}' `
    echo -e "程序: ${APP_NAME} 已启动 \033[32m 进程号: ${pids} \033[0m"
  fi
}

stop(){
  is_starting
  if [ $? -eq 0 ]; then
    kill -9 $pid
    echo -e "程序: ${APP_NAME} \033[31m 进程号: ${pid} 已停止运行 \033[0m"
  else
    echo -e "程序: ${APP_NAME} \033[31m 程序未启动 \033[0m"
  fi
}

is_starting(){
  pid=`ps -ef | grep $APP_NAME | grep -v grep | awk '{print $2}' `
  if [ -z "${pid}" ]; then
    return 1
  else
    return 0
  fi
}

restart(){
  stop
  start
  echo -e "\033[32m程序 ${APP_NAME} 重启成功 \033[0m"
}
case "$1" in
    "start")
        start
        ;;
    "stop")
        stop
        ;;
    "restart")
        restart
        ;;
    *)
        echo "$0 {start|stop|restart}"
        exit 0
        ;;
esac

