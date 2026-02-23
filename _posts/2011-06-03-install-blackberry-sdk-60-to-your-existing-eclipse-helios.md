---
layout: post
title: "Install Blackberry SDK 6.0 to your existing Eclipse Helios"
date: 2011-06-03 12:00:00 +0000
tags: [Blackberry]
original_url: "/2011/06/03/install-blackberry-sdk-6-0-to-your-existing-eclipse-helios.html"
---

Blackberry provides a “Java plugin for Eclipse” that can be downloaded and used for eclipse-based blackberry development. But beware, what you download is not an eclipse plugin. Instead, it is a full eclipse download with the plugins pre-installed. I didn’t want a new copy of eclipse just for Blackberry development. I wanted to use my already well configured Helios installation to be used for Blackberry development as well. So, i chose to use the provided update site – *http://www.blackberry.com/go/eclipseUpdate/3.6/java* – to install the plugin to my existing Helios installation.


The issue is that, I was unable to install the plugin using the aforementioned update site and noticed that [others faced the same problem too](http://supportforums.blackberry.com/t5/Java-Development/Cannot-install-Eclipse-plugin-from-Update-site/td-p/779959). After a lot of failed attempts, I finally discovered a different way to solve the problem. I downloaded the full “Java Plugin for Eclipse” from the Blackberry download site and just copied all the net.rim.* files from the plugins and features directory to my Helios installation. 


Worked for me and I am a happy camper!