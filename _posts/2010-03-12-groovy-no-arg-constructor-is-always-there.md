---
layout: post
title: "Groovy: No-arg constructor is always there"
date: 2010-03-12 12:00:00 +0000
tags: [Groovy]
original_url: "/2010/03/12/groovy-no-arg-constructor-is-always-there.html"
---

Do you usually write a no-arg constructor for your Java classes? You don’t have to – unless you need to initialize something in that constructor. Behind the scenes, the Java compiler adds the no-arg constructor directly into the byte-code if none is provided. But when one or more overloaded constructors are provided for that class, the compiler doesn’t add the default no-arg constructor to the byte-code. This has been part of Java since the beginning. 


Fast forward to today. I was doing some work with Groovy. All of a sudden, i realized that i forgot to add a no-arg constructor inspite of adding multiple constructors to a class and the code was still working without errors. That is when I found out that the Groovy compiler adds the no-arg constructor to the byte-code regardless of other overloaded constructors. I just thought I should share this learning with the world and hence this blog!


Does JRuby, Jython, Scala and other JVM languages do it too? Will have to check…


Don’t get me started on why i should use overloaded constructors when Groovy provides dynamic constructors out of the box. The short answer is “API Requirement” from the client.