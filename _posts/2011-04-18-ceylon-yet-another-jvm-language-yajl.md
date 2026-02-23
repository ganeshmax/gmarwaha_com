---
layout: post
title: "Ceylon – Yet Another JVM Language (YAJL)"
date: 2011-04-18 12:00:00 +0000
tags: [General]
original_url: "/2011/04/18/ceylon-yet-another-jvm-language-yajl.html"
---

It is all too familiar, yet surprising; it is all too common, yet shocking; to see [yet another JVM language](http://en.wikipedia.org/wiki/List_of_JVM_languages) created to scratch an itch that countless other languages are already trying to solve. 


Of course Java is not expressive enough, it doesn’t have higher order functions, it doesn’t have modularity as a language feature, it doesn’t have clean way to do meta-programming, it does NOT have so many more features we love and does have so many more features we hate. These are most of what has frustrated Gavin King (the creator of Hibernate) as well and made him think about creating a new language – [Ceylon](http://relation.to/Bloggers/TalkAtQConBeijing). A few days ago, in his presentation at the [QCon Beijing 2011](http://www.qconbeijing.com/) he gave a first glimpse of the language features and a few code snippets showing its beauty. 


A lot of people have raised concerns and expressed strong opinions questioning a need for yet another language. [Scala](http://www.scala-lang.org/) fans, the [Groovy(++)](http://groovy.codehaus.org/) camp, [Gosu](http://gosu-lang.org/) and [Fantom](http://fantom.org/) hackers all think that Ceylon does not solve anything that is not solved already or could have been solved by just contributing to one of these modern languages. So, I am not going to be yet another anti Ceylon person but I am not a fan either.


I believe Ceylon is more of a strategic approach from RedHat than a language created out of true necessity. They would like to control a language and its followers like most other giant companies do today. Think about it. Oracle is controlling Java, Microsoft is controlling C# (VB, VC++, etc), Google is controlling Go (and Python?), Apple is controlling Objective C and VMWare is controlling Groovy. RedHat has just joined the party leaving only IBM out of the equation. I am sure they are not far behind. I just sincerely hope that they adopt an existing language (Scala?) instead of creating yet another one. 


That said, the language itself looks cool, is very expressive and adds a lot of syntactic sweetness to say the least. I just wanted to highlight a few of them here… 


**String Interpolation:**

In Java we use a “+” sign for string concatenation. There is no concept of string interpolation in either Java or Scala. In Groovy ${} construct is used while Ruby uses #{}. Ceylon’s syntax looks better than either of them though. It uses a “space” as the string interpolation operator and the result looks a lot cleaner.  Don’t you think?


```

String name;
writeLine("Hello " name "!");

```


**Getter:**

In Java we use getXxx() methods to get a property value. This looks like a method and quacks like a method and does not give the feeling of accessing a property at all. In Ceylon, a very simple innovation has resulted in much more succinct getter methods. They have decided to get rid of paranthesis to both define and call getter methods. Look at the last line of the following snippet. Does it look like a method call? NO. Does it look like accessing a property? Of course it does !!!


```

class Counter() {
   variable Natural count := 0;
   shared Natural currentCount {
      return count;
   }
}
Counter c = new Counter();
writeLine(c.currentCount);

```


**Constructor:**

In Ceylon there is no separate constructor. The class definition itself acts as a constructor as shown below. Since, there is no concept of method or operator overloading in Ceylon there is no necessity to have a separate method and this syntax induces a “Why didn’t I think of this before ?” moment… The necessity for an overloaded method is handled by optional /defaulted parameters concept. So, you don’t have to worry too much about it…


```

class Customer (String cName, Natural cAge, Date cDob) {
   variable String name :=  cName;
   …
}

```


**Builder:**

With the support of named parameters and higher-order functions and quite a bit of thought, a syntactic structure as expressive as given below has been achieved in a general purpose and statically typed language like Ceylon.


```

Html hello {
   Head head { title = "Squares"; }
   Body body {
      Div {
         cssClass = "greeting";
         "Hello" name "!";
      }
   }

```


And then there is the rest of the now so common features like array like access to Sequences (equivalent of List in Java), higher-order functions, Closures, Currying, etc


It is not like I loved every single feature of Ceylon. I hated a few, but I am reserving that rant for another post…