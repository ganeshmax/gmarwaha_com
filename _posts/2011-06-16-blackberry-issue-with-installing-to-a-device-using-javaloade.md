---
layout: post
title: "Blackberry – Issue with Installing to a device using Javaloader"
date: 2011-06-16 12:00:00 +0000
tags: [Blackberry]
original_url: "/2011/06/16/blackberry-issue-with-installing-to-a-device-using-javaloader.html"
---

After I successfully finished developing the first part of my new Blackberry application, I code-signed it so that I can see it on an actual device. There are many ways to deploy your under-development application to the device. You can directly use the “Debug” menu in eclipse and select `Debug As -> Blackberry Device`. With your device connected to the USB port, eclipse will automatically deploy your application. Behind the scenes eclipse uses a command line tool called `JavaLoader` to deploy the application. Consequently, you can use “JavaLoader” directly from the command-line as well.


There are a few other ways as well. For instance, you can use the Blackberry desktop manager software to deploy `ALX` files, or you can deploy `OTA` using `JAD` files and so on. Although the last two methods are primarily used for the production deployment, the first two methods can be used for development deployment.


When I wanted to deploy using the first method for the first time, eclipse was showing a progress bar for too long with no feedback. I cancelled the operation and tried again with no change in attitude from eclipse. So, i decided to directly use `JavaLoader`. I used the command…


```
JavaLoader.exe -u load path_toyour_app.cod

```

and got the error…


```
Connecting to device...debug: HRESULT error during Open: 80040154
Error: unable to open port

```

My excitement wained off for the moment. Won’t it be good if everything worked well at first attempt?

#### Solution:


Install the Blackberry Desktop Manager. When you connect your blackberry using the USB cable, make sure the desktop manager says it is connected. Then you can use `javaloader` to load the app into your mobile without the command-line error or without Eclipse showing attitude.


NOTE: I am wondering why wouldn’t it open the app by default when i deploy it. Why do I have to browse through the application list or the download directory and run the application by myself.