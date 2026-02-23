---
layout: post
title: "Groovy – Java keyword as a method name"
date: 2008-01-09 12:00:00 +0000
tags: [Groovy]
original_url: "/2008/01/09/groovy-%e2%80%93-java-keyword-as-a-method-name.html"
---

Java, like any other language has reserved words. We are not allowed to use these words as method names or variable names. Most of the times that is fine, but sometimes we may find that these reserved words form the best name for a method. Helplessly, with just a sigh, we name the method with its synonym instead. 


Groovy, being a JVM language, has the same set of restrictions. But since it is completely dynamic in nature, it handles this scenario a bit differently from within and allows us to use reserved words as method names. All you have to do is wrap the method name within quotes during method definition as shown below and you are done. Cool isn’t it?


```

class User {
  String name

  String "delete"() {
    name = ""
  }
}
def user = new User(name: "ganesh")
assert "" == user.delete() 

```