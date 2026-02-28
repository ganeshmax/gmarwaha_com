---
layout: post
title: "Ctrl + Key Combination – Simple Jquery Plugin"
date: 2009-06-16 12:00:00 +0000
tags: [jQuery]
original_url: "/2009/06/16/ctrl-key-combination-simple-jquery-plugin.html"
---

In a recent web application I was working on, I had a need for the “Ctrl + S” hotkey to save an entry to the database. Being a an avid jquery fan, I immediately searched the plugin repository for any plugin that fits the bill. I was not very surprised to find a very comprehensive [jshotkeys](http://code.google.com/p/js-hotkeys/) plugin. It was feature rich and addressed all the requirements for hotkeys in a jquery powered application and obviously my requirement was fulfilled as well.


But the basic issue (and advantage too) with any plugin is that it is written for a wide range of audience. So, although my requirement was only for a “Ctrl + key” combination, I had to part with my bandwidth for all other features this plugin offered. Like my famous [jCarouselLite]({{ site.baseurl }}/2007/08/09/jcarousel-lite-a-jquery-plugin.html) plugin, I like my javascript code kept to the minimum. So, I decided and wrote a short yet sweet plugin that would solve only the problem I have at hand. Unsurprisingly, the plugin code turned out to be only **195 bytes** (minified). Given below is the code for the same…


```

$.ctrl = function(key, callback, args) {
    var isCtrl = false;
    $(document).keydown(function(e) {
        if(!args) args=[]; // IE barks when args is null
        
        if(e.ctrlKey) isCtrl = true;
        if(e.keyCode == key.charCodeAt(0) && isCtrl) {
            callback.apply(this, args);
            return false;
        }
    }).keyup(function(e) {
        if(e.ctrlKey) isCtrl = false;
    });        
};

```


This is how it works:


**1. **You want to execute a function when the user presses a “Ctrl + key” combination.

**2. **You as a developer should call the plugin method and pass in 3 parameters.

**3. ***1st Param:* The “key” user should press while he is pressing Ctrl.

**4. ***2nd Param:* The callback function to be executed when the user presses “Ctrl + key”.

**5. ***3rd Param:* An optional array of arguments, that will be passed to the callback function.


In the code given below, when the user presses the “Ctrl + S” key combination, the anonymous callback function passed in as the second parameter is called. 


```

$.ctrl('S', function() {
    alert("Saved");
});

```


Here, when the user presses the “Ctrl + S” key combination, the anonymous callback function passed in as the second parameter is called with the arguments passed in as the third parameter.


```

$.ctrl('D', function(s) {
    alert(s);
}, ["Control D pressed"]);

```


Thats it. I feel it is simple yet effective and solves a common requirement in modern web applications. 


What do you think?


## Update


A comment provided by “A Nony Mouse” in this blog entry clarified that, we don’t have to store a boolean called “isCtrl” to check if the “Ctrl” key is down while another key is being pressed. It is enough to check for e.ctrlKey as it will return true if the “Ctrl” key is down even if another key is being pressed along with Ctrl. Based on that input the “Ctrl + Key” plugin has been updated. Take a look at the updated code below. For archiving purposes, I am leaving the original version of the code above without any changes.


```

$.ctrl = function(key, callback, args) {
    $(document).keydown(function(e) {
        if(!args) args=[]; // IE barks when args is null 
        if(e.keyCode == key.charCodeAt(0) && e.ctrlKey) {
            callback.apply(this, args);
            return false;
        }
    });        
};

```