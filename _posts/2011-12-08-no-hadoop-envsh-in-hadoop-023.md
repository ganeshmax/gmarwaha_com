---
layout: post
title: "No hadoop-env.sh in Hadoop 0.23"
date: 2011-12-08 12:00:00 +0000
tags: [Hadoop]
original_url: "/2011/12/08/no-hadoop-env-sh-in-hadoop-0-23.html"
---

The first thing to do after downloading and extracting Hadoop is to set *JAVA_HOME* in the *$HADOOP_HOME/conf/hadoop-env.sh* file. Almost all documentation on Hadoop site expects the above configuration but I guess that was for version 0.20. When I downloaded Hadoop 0.23 today and looked for the hadoop-env.sh file, I could not find it anywhere in the extracted archive. 


After a bit of Googling I realized that things have changed in 0.23 version and now I will have to look for the file in the *$HADOOP_HOME/etc/hadoop* directory instead. Unfortunately I couldn’t find the file there either.


As a last resort I created a file named *hadoop-env.sh* in the *$HADOOP_HOME/etc/hadoop* directory and set my *JAVA_HOME* there. The one and only line in that file is given below. Fortunately after that addition, the hadoop command started working and everything went normal again.


```

export JAVA_HOME=/usr/lib/jvm/java-6-openjdk/

```