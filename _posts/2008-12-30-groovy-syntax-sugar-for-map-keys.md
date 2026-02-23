---
layout: post
title: "Groovy – Syntax sugar for map keys"
date: 2008-12-30 12:00:00 +0000
tags: [Groovy]
original_url: "/2008/12/30/groovy-syntax-sugar-for-map-keys.html"
---

Groovy keeps putting a smile on my face again and again. This time it is for a cool syntax sugar that i found useful as well as clean. Lets get to the chase without too much of chit-chat. 


Let’s create a Map of people and their ages in groovy using literal syntax. You could write it this way…


```

Map people = [
   "John" : 24,
   "Steve" : 30,
   "Cathy" : 25 
];

```


Pretty straight-forward! But don’t you think the double quote around each name looks like unnecessary clutter. I thought so and I guess groovy developers thought so too. So, they made it easy on us and allowed us to just ignore the quotes. So, the same map can be written as shown below, without the quotes and groovy still understands what you mean. In this case, groovy considers the key to be of String data type. If you used numeric literals for keys, groovy would consider them as their appropriate numeric type. 


```

Map people = [
   John : 24,
   Steve : 30,
   Cathy : 25 
];

```


You may ask that this is well and good, but then how will i use my variables as keys? It so happens that many a times when we create a map using literal syntax we use only string literals or numeric literals as keys and not a variable reference. So, this syntax covers for most of the cases. But, if you definitely need to use your variables as keys, then you have two options. 


The first option is to not use literal syntax. Instead you could just use normal map.put() syntax to get the job done. But this doesn’t look groovy. 


```

Map people;
people.put(name1, 24)
people.put(name2, 30)
people.put(name3, 25)

```


The second option is to wrap the keys with parenthesis as shown below. This way you are explicitly telling groovy to consider them as variable references. 


```

Map people = [
   (name1) : 24,
   (name2) : 30,
   (name3) : 25 
];

```


Ok, now this syntax is more cluttered than the original one with quotes wrapped around them. I agree. But, considering the frequency with which this is going to be used, I think this is a better alternative.