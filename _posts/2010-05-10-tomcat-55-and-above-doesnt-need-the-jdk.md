---
layout: post
title: "Tomcat 5.5 and above doesn''t need the JDK"
date: 2010-05-10 12:00:00 +0000
tags: [Tomcat]
original_url: "/2010/05/10/tomcat-5-5-and-above-doesnt-need-the-jdk.html"
---

Most of us who install Tomcat on our development machines wouldn’t have noticed that Tomcat versions before 5.5 required the full blown Java Development Kit (JDK) to be installed on the machine. Just installing the Java Runtime Environment (JRE) wasn’t enough. The JDK is meant for developers to be able to compile Java programs, and has the development tools such as the compiler, debugger and other development libraries. Tomcat versions prior to 5.5 used the Java compiler that comes with the JDK to compile JSP pages at runtime and consequently required a full blown JDK.


Tomcat versions 5.5 and above have a Java compiler (the Eclipse JDT Java compiler) packaged along with it. Now, this is used to compile the JSP pages dynamically instead of the JDK compiler. Hence, it is enough if we just install JRE starting from Tomcat version 5.5 and above.