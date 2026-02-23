---
layout: post
title: "JQuery: Wait for multiple animations to Complete – Take 2"
date: 2011-08-17 12:00:00 +0000
tags: [jQuery]
original_url: "/2011/08/17/jquery-wait-for-multiple-animations-to-complete-take-2.html"
---

In an [earlier blog post](/2009/06/09/jquery-waiting-for-multiple-animations-to-complete.html), I stated the need for a technique that helps determine when multiple animations have completed running, so that we can execute some code at that point. I also examined a technique using a combination of setInterval() based polling and checking for the *:animated* pseudo-class to achieve the result.


With the release of version 1.5, jQuery introduced the concept of **Deferred Objects**. It’s a pretty useful beast. You can find the full explanation [here](http://api.jquery.com/category/deferred-object/). In jQuery 1.5, the $.ajax() was enhanced to return a Deferred Object, but $.animate() was cheated without being given that honor. That was corrected with the release of jQuery 1.6 and now you receive a Deferred Object as a return value for $.animate() and its higher-level cousins. 


Using the returned Deferred Object, and another useful utility function named $.when() we don’t have to stoop down to using poll-based techniques to wait for multiple animations to complete. Take a look at the code below and you will agree that it can be done much more cleanly now. 


```

var animatingFoo = $("#foo").slideUp(1000);
var animatingBar = $("#bar").slideDown(3000);

$.when(animatingFoo, animatingBar).done(function() {
  // Do something useful
});

```


Here, both the slideUp() and slideDown() methods return a Deferred Object. Although we can attach the done() event-handler to the *animatingFoo* and *animatingBar* separately (which will get fired separately when the individual animations are complete), that is not what we are after. We want to execute our code after both the animations are complete. For this purpose we call in the help of a utility function $.when(). 


$.when() aggregates multiple deferred objects and returns a single deferred object. Now, if we attach our done() event-handler to the aggregated deferred object, it will get fired only after both the animations are complete, which solves our requirement.