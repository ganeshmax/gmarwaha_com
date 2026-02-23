---
layout: post
title: "jQuery UI: Calling widget methods directly"
date: 2011-09-30 12:00:00 +0000
tags: [jQuery]
original_url: "/2011/09/30/jquery-ui-calling-widget-methods-directly.html"
---

A typical [jQuery plugin](http://docs.jquery.com/Plugins/Authoring) is just another function attached to the jQuery object. As a plugin developer you write a function, attach it to jQuery.fn (just an alias for its prototype) and your plugin method is magically available to all jQuery instances. As a plugin user, you normally execute the plugin by calling a method on the jQuery object. Something like 


```

// jCarouselLite is the plugin in this case
$("#carousel").jCarouselLite(options); 

```


The above call returns the jQuery object on which the plugin was originally invoked. That way you can chain method calls and marvel at the beauty of our wide one-liner solution. But not for long!!!


What if you would like to control the behavior of the plugin after initialization? What if you want to stop() what the plugin is doing, maybe add() something to it or maybe even destroy() it? There was no easy answer to that question and every plugin developer was left to his own creativity to come out with a solution.


```

var $carousel = $("#carousel").jCarouselLite(options); 
$carousel.stop();  // You cannot do this
$carousel.run(); // Nope! You cannot do this either
$carousel.destroy(); // Nope! You get the idea...

```


While developing jQuery UI, the team there recognized this as a generic problem and came up with a generic solution. They called it the *Widget Factory* and popularized it as a way to develop **Stateful plugins** as opposed to traditional **Stateless plugins**. Take a look [here](http://ajpiano.com/widgetfactory/#slide1) to know more about how to develop jQuery plugins using the [Widget Factory Pattern](http://ajpiano.com/widgetfactory/#slide1). All jQuery UI widgets are examples of plugins developed using the Widget Factory. Lets take one interaction with the jQuery UI 


```

var $accordion = $(“#accordion”).accordion(options);
$accordion.accordion(“enable”); // Enable the accordion
$accordion.accordion(“activate”, 1); // Activate the second tab

```


As can be seen above, now you can interact with the Accordion after initialization by passing a method name as string. For instance, “enable” is a method that takes zero arguments and enables the accordion and “activate” is another method that takes one argument (an index) to be activated and opens up the accordion tab at that index. 


It works, but wouldn’t it be cool if we don’t pass in method names as strings and would get to call the methods directly on $accordion – like $accordion.enable()?


It so happens that the $accordion is not an instance of the widget itself, but a jQuery object that wraps the DOM element representing the accordion. In most situations that is what you will need and so that is what is given to you. 


The good news is that, the actual widget instance is stored with the corresponding DOM element using jQuery.data(). The plugin’s name is used as its key. Therefore, you can call $accordion.data(“accordion”) and enjoy direct access to all its plugin methods without retorting to indirect, string based approach anymore.


```

var $accordion = $(“#accordion”).accordion(options).data(“accordion”);
$accordion.enable(); // Enable the accordion
$accordion.activate(1); // Activate the second tab

```


Now you can have your cake and eat it too…