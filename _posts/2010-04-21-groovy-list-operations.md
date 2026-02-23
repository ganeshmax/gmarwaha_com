---
layout: post
title: "Groovy: List Operations"
date: 2010-04-21 12:00:00 +0000
tags: [Groovy]
original_url: "/2010/04/21/groovy-list-operations.html"
---

Anybody who has programmed in Java for sometime would attest to how frustrated they could get while operating on the Collection API. Even simple operations demand unnecessary lines of code increasing the LOC and reducing expressiveness of the intended logic. Fortunately, Java has noticed the pain and has been adding utility classes to the Collections API to improve readability of the code since Java 5. Even better, there are a couple of libraries, [Lambdaj](http://code.google.com/p/lambdaj/) and [op4j](http://www.op4j.org/), that implement the powerful *[Fluent interface](http://martinfowler.com/bliki/FluentInterface.html)* that takes readability to the next higher plane.


Libraries and utilities are good for Java, but we are still bound by the constraints of the language itself. Isn’t it? That is where Groovy steps in. Groovy is in a totally different league when it comes to expressiveness of code. It was designed with the “Principle of least surprise” in mind. Best of all, Groovy source compiles to java byte-code thereby only adding a jar file as a dependency to your projects.


To whet your appetite, here are a few code snippets for list operations in Groovy that will make you smile…


**Create lists in groovy:** Keeping the literal notation the same, you can define different implementations of the collections framework


```

// Returns an ArrayList by default
def personalities = ["Steve", "Bill", "Larry"]

// Returns a LinkedList
def personalities = ["Steve", "Bill", "Larry"] as LinkedList

// Returns a String array
def personalities = ["Steve", "Bill", "Larry"] as String[]

```


**Basic list operations:** There are many more operations. But this gives you a feel for how easy it is to add, remove and retrieve elements off of the list


```

// Defines a list of strings
def personalities = ["Steve", "Bill", "Larry"]

// Retrieving an element
assert "Larry" == personalities[2]

// Retrieving a range of elements
assert ["Bill", "Larry"] == personalities [1..2]

// Adding an element
assert ["Steve","Bill","Larry","Scott"] == (personalities<<"Scott")

// Removing an element
assert ["Steve", "Bill", "Larry"] == (personalities -= ["Scott"])

```


**Other cool operations:** These are some operations that you typically don't find in Java. Correct usage of these operations will lead you towards strong and idiomatic Groovy programming.


```

// Transforming one list into another
assert [2,4,6] == [1,2,3].collect{ it*2 }

// Finding every element matching the closure
assert [1,3] == [1,2,3].findAll{ it % 2 == 1 }

// Print each element of the list
[1,2,3].each{ println it }

// Spread Dot operator operates on every element of the list
assert [1,2,3] == ["a", "bb", "ccc"]*.size()   

// Spread operator is used to pass a list as method parameters
def add(a, b, c) { return a+b+c }
assert 6 == add(*[1,2,3])

```


There are many many more features that support the Collections framework. To list it all is not the intention of this post, rather this post is intended to give a quick feel for how easy it is to write Groovy code when dealing with a Collection of objects.