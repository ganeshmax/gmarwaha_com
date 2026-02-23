---
layout: post
title: "JQuery: Waiting for Multiple Animations to Complete"
date: 2009-06-09 12:00:00 +0000
tags: [jQuery]
original_url: "/2009/06/09/jquery-waiting-for-multiple-animations-to-complete.html"
---

Have you ever come across a situation where you wanted to execute a certain piece of code after an animation has completed running? This is a very common use-case in modern web development. [jQuery](http://jquery.com) team knows it, and that is why they accept a callback function as argument for every kind of animation call. In the example below, we pass in a callback function that will be executed after the *“slideDown”* animation is complete. This is the usual scenario.


```

$("#animateMe").slideDown(function() {
	// This piece of code will be executed 
	// after the animation is complete
});

```


But, in many other scenarios you might want to wait for **multiple animations** to complete before executing a certain piece of code.  Lets assume that the two elements – “#element1” and “#element2” – are currently getting animated. Our goal is to execute a piece of code after both elements are finished with their respective animations. This is where it gets tricky. I was facing one such challenge today. The solution I have arrived at is to use the **“:animated”** pseudo-selector and “setInterval” to repeatedly check and wait until the animations have completed running. An example will clarify what I mean


```

var wait = setInterval(function() {
	if( !$("#element1, #element2").is(":animated") ) {
		clearInterval(wait);
		// This piece of code will be executed
		// after element1 and element2 is complete.
	}
}, 200);

```


In the example above, I use “setInterval” to repeatedly check if these two elements are NOT being “:animated”. If this condition is not met, then it means that atleast one of them is still getting animated. So, “setInterval” will check for the same condition again in 200 ms until the condition is met. If the condition is met, it means that the animations are complete. So, I immediately do a “clearInterval” and stop checking for this condition again. Any code written after this statement will get executed after both the animations are complete. 


Ofcourse, the same code can be modified for more than two elements as well. Some more work, and we can make it handle any number of elements. But, I was wondering if there was an easier, better and more efficient approach to solve the same challenge. If fellow jquery lovers are aware of such solutions please feel free to leave a comment.