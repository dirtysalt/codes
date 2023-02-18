### mysql升级   
1. dp0上配置mysqldb（python 访问mysql的库,DONE）
2. dp1 上添加dp_routine/dm_routine 两个库,dptest1上安装mysql作为从库，配置master、slave (DONE)
3. dp-deploy 停止小时任务的提交crontab (升级时间点需要注意，升级时间不能有影响天级、周级、月级的任务提交）
4. 停止dp-schedule,(/data/dirlt/dp-scheduler/V2),由于新版中没有了sqllite，需要在pull前，完成历史数据库nsched.db的拷贝，先不获取最新的分支
5. sqllite数据库导入到mysql，具体过程如下：   
    * sqlite3 'nsched.db' '.dump jobTable' > /tmp/nsched-swap.sql
    * 修改/tmp/nsched-swap.sql 文件（替换"jobTable" 为jobTable； 修改create 字句中的force字段为isForce) ,重命名为/tmp/nsched-mysql.sql
    * 将/tmp/nsched-mysql.sql 导入到mysql
6. dp0获取最新的dp-schedule，运行run-nsched.py ,run-vier.py （绑定不同地址）,注意配置mysql地址和库以及配置文件修改
7. 运行、验证通过后，重启dp-deploy的小时任务（如果有小时任务没有提交，则需要手工完成），调度器页面手工标示需要重启的job


### dp-deploy 调整
5 * * * * /bin/bash -l -c "cd /home/dp/dirlt/dp-deploy/nsched;./hsubmit.py --host=127.0.0.1 --port=8000 --deploy-path=/home/dp/dirlt/dp-deploy/ >> /home/dp/dirlt/dp-deploy/nsched/hsubmit.log 2>&1"
10 0 * * * /bin/bash -l -c "cd /home/dp/dirlt/dp-deploy/nsched;./dsubmit.py --host=127.0.0.1 --port=8000 --deploy-path=/home/dp/dirlt/dp-deploy/ >> /home/dp/dirlt/dp-deploy/nsched/dsubmit.log 2>&1"
5 10 * * Mon /bin/bash -l -c "cd /home/dp/dirlt/dp-deploy/nsched;./wsubmit.py --host=127.0.0.1 --port=8000 --deploy-path=/home/dp/dirlt/dp-deploy/ >> /home/dp/dirlt/dp-deploy/nsched/wsubmit.log 2>&1"
0 14 1 * * /bin/bash -l -c "cd /home/dp/dirlt/dp-deploy/nsched;./msubmit.py --host=127.0.0.1 --port=8000 --deploy-path=/home/dp/dirlt/dp-deploy/ >> /home/dp/dirlt/dp-deploy/nsched/msubmit.log 2>&1"
