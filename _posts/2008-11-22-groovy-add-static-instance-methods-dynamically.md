---
layout: post
title: "Groovy – Add Static & Instance methods dynamically"
date: 2008-11-22 12:00:00 +0000
tags: [Groovy]
original_url: "/2008/11/22/groovy-%e2%80%93-add-static-instance-methods-dynamically.html"
---

Like Ruby and other dynamic languages in its Genre, groovy also allows us to add methods to a class dynamically at runtime. You need not restrict yourself to adding instance methods alone. Even static methods are supported. 


To showcase this, let’s create a class called User with name and email properties.


```

class User {
  String name, email
}

```


Now, let’s add a static newInstance() method to create a new instance of this class. Technically speaking this is not a method; it is a closure. This example is contrived, but I hope you get the idea.


```

User.metaClass.static.newInstance = {name, email ->
  new User(name: name, email: email)
}

```


Now, let’s add an instance method to update the “name” property of User. Here, the “delegate” references the “this” pointer. Remember, this is not a method; it is a closure.


```

User.metaClass.updateName = { name ->
  delegate.name = name
}

```


The very next line you can start creating a new instance of user using this dynamically added static method and instance method as shown below.  


```

User user = User.newInstance('ganesh', 'g@e.com')
assert 'ganesh' == user.name

user.updateName ("ganeshji")
assert "ganeshji" == user.name

```


It is not necessary that you add these new methods right below the class. You can add it anywhere in your code. As long as you call these methods after the lines that define these new methods are executed you should be fine.