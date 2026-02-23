---
layout: post
title: "Hibernate – Difference between session''s get() and load()"
date: 2007-01-16 12:00:00 +0000
tags: [Hibernate]
original_url: "/2007/01/16/hibernate-difference-between-sessions-get-and-load.html"
---

Being an avid [hibernate](http://www.hibernate.org) fan, I have always defended it in my organization when people throw undue criticism at it in order to protect themselves. In one such debate, a colleague pointed out a pattern in our code-base that introduced needless performance degradation, and condemned hibernate    for it. I was glad he brought that up – for 2 reasons. First because, it sure was a problem and called for immediate attention. Second because, once again the problem was not with hibernate, but us.  If you look closely at domain driven applications, you will notice that a few core objects are directly referenced by most other objects.  Let me clarify what i mean with an example. In an [auction](http://caveatemptor.hibernate.org) application, for example, an Auction is held for an Item, a Bid is placed for an Item, a Buyer buys an Item. The common object referenced here is, well, an Item. This implies that whenever you create a new Auction or Bid you are constrained to supply a reference to Item. The most obvious way to achieve this is by getting a persistent instance of Item from the database using the [session.get()](http://www.hibernate.org/hib_docs/v3/api/org/hibernate/Session.html#get%28java.lang.Class,%20java.io.Serializable%29) method. This works, but it has its limitations.


```

Session session = << Get session from SessionFactory >>
Long itemId = << Get the item id from request >>

Item item = (Item) session.get(Item.class, itemId);

if(item != null) {
   Bid bid = new Bid();
   bid.setItem(item);
   session.saveOrUpdate(bid);
} else {
   // Handle the error condition appropriately
   log.error("Bid placed for an unavailable item");
}
```


Think about it… How many times will a bid be placed for an Item? Many… Every time a Bid is placed, is it wise to hit the database and retrieve the corresponding Item just to supply it as a reference? I guess not. That is where [session.load()](http://www.hibernate.org/hib_docs/v3/api/org/hibernate/Session.html#load%28java.lang.Class,%20java.io.Serializable%29) comes in. All the above scenarios remaining the same, if you just used session.load() instead of get(), hibernate will not hit the database. Instead it will return a proxy, or an actual instance if it was present in the current session, and that can be used to serve as a reference.  What does this buy you? At least 2 advantages. First, you save a trip to the database. Second, the error handling code just got elegant. Take a look at the code snippet below. Here we don’t handle erroneous conditions using null checks. Instead we use exceptions, which sounds appropriate in this scenario. Don’t they?


```

Session session = << Get session from SessionFactory >>
Long itemId = << Get the item id from request >>

try{
   Item item = session.load(Item.class, itemId);
   Bid bid = new Bid();
   bid.setItem(item);
   session.saveOrUpdate(bid);
} catch(ObjectNotFoundException e) {
   // Handle the error condition appropriately
   log.error("Bid placed for an unavailable item");
}
```


From the above piece of code, it is obvious that, an ObjectNotFoundException may be thrown if the actual Item representing the given item id cannot be found. What i am not clear about – and neither is hibernate documentation – is which method is more likely to cause this exception and why? session.load() seems to have a possibility to throw this exception, and so does saveOrUpdate() for the same fact that item for the given id/proxy is not available.  I would love to hear from people who have traveled this path and have an answer.  Also, it would be wonderful, if you could point out other differences between session.get() and load() that i may have missed.