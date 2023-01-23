#!/bin/bash

# https://netflixtechblog.com/java-in-flames-e763b3d32166

cwd=`dirname $0`
cd $cwd
java -cp attach-main.jar:$JAVA_HOME/lib/tools.jar net.virtualvoid.perf.AttachOnce $@
sudo chown root /tmp/perf-*.map
cd -
