---
layout: post
title: "GWT – Not enough methods, expecting 3 saw 2"
date: 2011-05-04 12:00:00 +0000
tags: [GWT]
original_url: "/2011/05/04/gwt-not-enough-methods-expecting-3-saw-2.html"
---

In my current project we use GWT extensively. I also develop prototypes and POCs for clients using GWT when I am in presales mode. During one such prototype, when I was using GWT RPC to perform an AJAX call from the client to the server, I hit a road block. GWT was throwing me an error I couldn’t comprehend. 


```

java.lang.AssertionError: Not enough methods, expecting 3 saw 2

```


After a bit of fiddling and googling around, I realized that this was happening because I recently upgraded from version 2.0.3 to version 2.2. I guess the protocol GWT uses to serialize the data to be transported between the client and the server has changed between these two versions. Fair enough. But I don’t understand why I received that error although I created this project after upgrading to version 2.2. 


Anyways, I found out that for some odd reason the gwt-servlet.jar that was stuck to my lib folder was the older 2.0.3 version. When I replaced it with the 2.2 version of the jar file the problem got fixed. FYI, the 2.0.3 version of the jar is around 1.5 MB whereas the 2.2 version of the jar is around 4.5 MB. 


Meanwhile, I am working on a list of pros and cons for using GWT. Will be posting that soon…