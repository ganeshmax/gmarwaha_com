---
layout: post
title: "Twitter moves from Rails to Java"
date: 2011-04-11 12:00:00 +0000
tags: [General]
original_url: "/2011/04/11/twitter-moves-from-rails-to-java.html"
---

A colorful feather up Rails’ cap is on the ground now. Twitter has decided to [go away from RoR in favor of Java](http://engineering.twitter.com/2011/04/twitter-search-is-now-3x-faster_1656.html), this time for their entire search stack. [Earlier in 2008-09](http://www.artima.com/scalazine/articles/twitter_on_scala.html), they decided to move their message queue back-end from ruby to Scala (a Java Platform) and now it is the time for their front-end to move to Java as well. 


They have built a scalable platform called Blender that uses Java NIO based server (Netty) to be efficient in the face of heavy incoming traffic, replaced MySQL with a Java based Lucene search engine, created an engine that parallelizes execution of multiple backend services with dependency management and more. With this setup there is a 3X drop in search latencies and can scale to 10X more requests per machine. 


Wow, that is quite an achievement. Could this mean that Java is a better platform than Rails for high scalability needs?  Even if that is the case, for simpler scenarios, the beauty of RoR out-weighs Java’s performance.


They say that this change will enable them to rapidly iterate on search features in the coming months. That along with the news that [Twitter has hired 25 more employees](http://www.mediabistro.com/alltwitter/twitter-hires-6-5-of-its-workforce-in-one-swoop_b6342) kinda tells that Java’s code base is practically more maintainable than equivalent Ruby code – at least when the code base is huge and the team size is large. Or that could mean that this time they really put a lot of thought into designing a maintainable system than when they started out. But for smaller team size and code base, RoR is still an unbeaten champion.