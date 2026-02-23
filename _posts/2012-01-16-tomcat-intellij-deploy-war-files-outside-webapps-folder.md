---
layout: post
title: "Tomcat & IntelliJ – Deploy war files outside webapps folder"
date: 2012-01-16 12:00:00 +0000
tags: [Tomcat]
original_url: "/2012/01/16/tomcat-intellij-deploy-war-files-outside-webapps-folder.html"
---

At present I am working on developing an **Android** application that needs to be supported by a slew of REST services hosted in the cloud. I chose [Google App Engine](https://appengine.google.com/) based on its support for Java, Groovy and most importantly Spring. I developed a Spring MVC based REST application and used *ContentNegotiatingViewResolver* to negotiate content based on request URL extensions. For example, an XML response will be returned if the request URL ends with *.xml*, a JSON response for *.json* and an HTML response if he URL doesn’t have any extension. Don’t get me started on Accept Header versus URL extension based content negotiation. That is a rant for another day. 


I was attempting to Serialize a *Map<Enum, List<Model>>*. All was well and I was able to retrieve both HTML and JSON representations, but when I tested retrieving the XML representation, *JAXB* complained that it cannot handle a *Map* instance in the root although *Jackson* was totally cool about it. As usual, Googling revealed that JAXB expected a Container class at its root which I didn’t want to create. I didn’t want to give up either. So, I tried my luck using *XStreamMarshaller*. This time GAE complained that XStream used a restricted API. WTH?


Just out of curiosity, I wanted to check if XStreamMarshaller would work as expected when used outside of GAE. So, I created a Tomcat context file “myapp.xml” with the following definition and carefully placed it inside *TOMCAT_HOME/conf/Catalina/localhost*. I could have just started Tomcat from *TOMCAT_HOME/bin/startup.bat* to check if it works, but being an IDEA addict, I created a Run Configuration for the IDEA Tomcat plugin and started the server from inside IDEA. But the app refused to even be discovered, let alone be deployed. After a few frustrated attempts, I tried starting Tomcat directly outside IDEA. Thankfully the app got deployed successfully and to my surprise, the XStreamMarshaller skillfully streamed out the serialized XML. Problem Solved!


```

<?xml version='1.0' encoding='utf-8'?>
<Context docBase="PATH_TO_MY_APP"
         reloadable="true"
         path="/myapp">
</Context>

```


But, why didn’t the app get deployed when I started Tomcat from inside IDEA? After all, I have linked IDEA to my local Tomcat installation and the script it executes is clearly in my *TOMCAT_HOME/bin* folder. Then, why why why in the world does the app refuse to be discovered? The solution came in the form of CATALINA_BASE. It seems that IDEA copies the contents of *TOMCAT_HOME/conf* folder into its HOME folder with some name like *Unnamed_MyApp* and sets this folder to be the *CATALINA_BASE*. That explains why “myapp.xml” is so totally ignored by Tomcat. Then, I navigated to “Tomcat Run Configuration -> Startup/Connection -> Environment Variables” and added CATALINA_BASE as an environment variable and pointed it to your local TOMCAT_HOME folder. After this configuration change IDEA started Tomcat as expected and my app was both discovered and deployed. Another Problem Solved!


But the real problem – JAXB complaining about Map and GAE rejecting XStreamMarshaller as restricted – is yet to be solved. Maybe I should try one of the CastorMarshaller, XmlBeansMarshaller or JibxMarshaller. 


Any ideas?