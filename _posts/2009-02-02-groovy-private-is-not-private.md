---
layout: post
title: "Groovy: Private is not private"
date: 2009-02-02 12:00:00 +0000
tags: [Groovy]
original_url: "/2009/02/02/groovy-private-is-not-private.html"
---

If I have to name one language that I thoroughly enjoy programming in, it has got to be Groovy. I work with it almost on a daily basis although the platform for my day job doesn’t require it. Personally, I love groovy for the obvious reasons and also for the not so obvious reason – It has some sentimental value to me since I have been following this language since its inception.


That said, one of the things that surprised me while using groovy was its *Private* modifier. It seems groovy completely ignores its mere presence. I am used to the unavailability of *privates* in javascript for a pretty long time and so I religiously follow naming conventions to separate private from public assets. I have never used similar naming conventions for groovy because I thought the concept of private existed. Unfortunately, I was wrong. Let us dive into a few short examples to see what I mean…


```

class User {
   String firstName;
}

def user = new User()
user.firstName = "John"
println user.firstName

```


This is a typical POGO. *firstName* is private by default. Public *Setters and Getters* are generated automatically at compile time. When the caller uses this property, he will actually be using the public Setter or Getter instead of directly accessing the field. Typical groovy stuff…


On the flip side, if you don’t want groovy to generate the Getters and Setters at compile time, then you should modify the field using a private keyword as shown in the snippet below.


```

class User {
   private String firstName;
}

def user = new User()
user.firstName = "John"
println user.firstName

```


Now, groovy won’t generate the Getters and Setters for *firstName*. But if you run the above code, you will be surprised to see that the field is still accessible. The caller is able to set and get the *firstName*.


I thought maybe groovy is probably not suppressing the Getter and Setter generation due to some bug and that is the reason why this field is still accessible. But that is not the case, as you can see in the next example. In this snippet, you can see that I use groovy’s “.@” syntax to access the field directly and the field is still accessible. 


```

class User {
   private String firstName;
}

def user = new User()
user.@firstName = "John"
println user.@firstName

```


Then I tried private methods. No surprise there, since I got used to the surprise by now. Yes, the private methods are also directly accessible. 


```

class User {
   private String firstName;
   private String name() {
      firstName;
   }
}

def user = new User()
user.@firstName = "John"
println user.name()

```


Thank god though. There was some silver lining. Java classes aren’t able to access all of these private fields, properties and methods. It is only the other groovy scripts that are able to access it. The example below will demonstrate the same. 


```

class User {
   private String firstName;
}

class UserTest {
   public static void main(String args[]) {
      User user = new User();
      System.out.println(user.firstName); // compile error
      System.out.println(user.getFirstName()); // compile error
      System.out.println(user.name()); // compile error
   }
}

```


After some googling, I found a few jira issues [here](http://jira.codehaus.org/browse/GROOVY-1875), [here](http://jira.codehaus.org/browse/GROOVY-1063) and [here](http://jira.codehaus.org/browse/GROOVY-1591). 


After going through these links, it looks like this was a bug in groovy from the beginning, but nobody bothered to fix it because for such a dynamically and reflectively capable language *private* is just a documentation anyways.