---
layout: post
title: "LavaLamp for jQuery lovers!"
date: 2007-08-23 12:00:00 +0000
tags: [jQuery, jQuery]
original_url: "/2007/08/23/lavalamp-for-jquery-lovers.html"
---
Click on the above image to land in the [Lava Lamp Demo]({{ site.baseurl }}/projects/lavalamp/) page. Then, hover over it and feel for yourself, the nifty effect that Lava Lamp offers. What you just experienced is nothing but the LavaLamp menu packaged as a plugin for the amazing [jQuery javascript library](http://jquery.com). I personally believe that the effect rivals that of flash – Don’t you? Especially considering the fact that it is extremely light weight.


> 

Just so you know, it weighs just 700 bytes(minified)!


Often I have noticed, that the credits are usually granted towards the end. Just for a change, i am going to give my credits at the beginning. This effect was originally written by [Guillermo Rauch](http://devthought.com/cssjavascript-true-power-fancy-menu/) for the [mootools javascript library](http://mootools.net/). All I did was to port it for the benefit of jQuery lovers. Thanks Guillermo for inspiring the javascript world with such a nice effect. A special thanks to [Stephan Beal](http://wanderinghorse.net/home/stephan/) who named it “LavaLamp”, and to [Glen Lipka](http://commadot.com/) for generously helping with the image sprites. Many fellow jQuery lovers also helped shape this plugin with valuable feedback in the mailing list. Thanks a ton, all you guys.


As User Interface developers, we know that one of the first widgets our visitors use is a “Menu”. Capturing their attention right there is something that we always strive for, and I guess LavaLamp is a step in that direction. Before you get bored with all this useless talk, let me get you started on integrating LavaLamp into your jQuery powered site.


I hope you agree that a typical HTML widget consists of 3 distinct components.


- A semantically correct HTML markup

- A CSS to skin the markup

- An unobstrusive javascript that gives it a purpose


Now lets follow the above steps and implement the LavaLamp menu for your site. Remember, In the process of porting from mootools to jQuery, i have simplified both the javascript and CSS for your convenience. So, be informed that you will need to follow the instructions on this page to get the jQuery version running. Follow the instructions on [Guillermo Rauch’s](http://devthought.com/cssjavascript-true-power-fancy-menu/) page for the mootools version.


### Step 1: The HTML


Since most UI developers believe that an unordered list(ul) represents the correct semantic structure for a Menu/Navbar, we will start by writing just that.


```
        <ul class="lavaLamp">
            <li><a href="#">Home</a></li>
            <li><a href="#">Plant a tree</a></li>
            <li><a href="#">Travel</a></li>
            <li><a href="#">Ride an elephant</a></li>
        </ul>        

```


In the markup above, “ul” represents the menu, and each “li” represents a menu-item. At this point it is crucial to understand that we will be adding another artificial “li” to represent the background of the currently highlighted menu-item. Since the background itself is cosmetic and doesn’t represent a menu-item, we will be adding it from javascript. Just to make sure we are in sync, “you need not add this li”, the LavaLamp plugin will take care of it. Once added, the “li” representing the background will look like this.


```
        <li class="back"><div class="left"></div></li>

```


### Step 2: The CSS


You can skin this markup in many different ways to achieve your own personalized menu. The following style sheet is just one possibility. A few more possibilities are demonstrated in the “Bonus” section towards the end of this blog entry.


```
/* Styles for the entire LavaLamp menu */        
.lavaLamp {
    position: relative;
    height: 29px; width: 421px;
    background: url("../image/bg.gif") no-repeat top;
    padding: 15px; margin: 10px 0;
    overflow: hidden;
}
    /* Force the list to flow horizontally */
    .lavaLamp li {
        float: left;
        list-style: none;                    
    }
        /* Represents the background of the highlighted menu-item. */
        .lavaLamp li.back {
            background: url("../image/lava.gif") no-repeat right -30px;
            width: 9px; height: 30px;
            z-index: 8;
            position: absolute;
        }
            .lavaLamp li.back .left {
                background: url("../image/lava.gif") no-repeat top left;
                height: 30px;
                margin-right: 9px; 
            }
        /* Styles for each menu-item. */    
        .lavaLamp li a {
            position: relative; overflow: hidden;
            text-decoration: none; 
            text-transform: uppercase;
            font: bold 14px arial;
            color: #fff; outline: none;
            text-align: center;
            height: 30px; top: 7px; 
            z-index: 10; letter-spacing: 0; 
            float: left; display: block;
            margin: auto 10px;    
        }

```


Trust me, this is a simple style sheet. Follow along to understand what is done in each of its sections.


First, we style the “ul” with the bright orange background image and some basic properties like height, width, padding, margin etc. We use relative positioning because, that way we can absolutely position the background “li” relative to the “ul”. This helps by enabling us to move this background “li” freely within the context of the parent “ul”.


Next, we make the “li”s flow horizontally instead of vertically. By default, it flows vertically. There are a couple of techniques to do this. In this case, we are using the “float:left” to achieve this effect.


Next, we style the artifical “li” that represents the background of the currently highlighted menu-item. This uses the [sliding doors technique](http://alistapart.com/articles/slidingdoors). Also, notice the absolute positioning used as mentioned above.


Finally, we style the anchor that represents the actual clickable portion of each menu-item. These styles are mostly cosmetic and self-explanatory.


Some of the above rules may not be obvious if you are not very confident in how “positioning” works in CSS. For those, i highly encourage you to quickly read this article on [CSS positioning](http://www.barelyfitz.com/screencast/html-training/css/positioning/). It is short, sweet and very informative.


### Step 3: The Javascript


This is the easy part. Most of the javascript work is taken care by the Lava Lamp plugin itself. As a developer, you just have to include the mandatory and/or optional javascript files and fire a call to initialize the menu.


```
<script type="text/javascript" src="path/to/jquery.js"></script>
<script type="text/javascript" src="path/to/jquery.lavalamp.js"></script>
<!-- Optional -->
<script type="text/javascript" src="path/to/jquery.easing.js"></script>

<script type="text/javascript">
    $(function() { $(".lavaLamp").lavaLamp({ fx: "backout", speed: 700 })});
</script>    

```


Include a reference to the jQuery library and the LavaLamp plugin. Optionally, include the easing plugin as well. It has many cool effects, that are not contained in the core. For instance, the “backout” effect used in this demo is part of the easing plugin. You can download jQuery [here](http://code.jquery.com/jquery-latest.pack.js), Easing plugin [here](http://gsgd.co.uk/js/jquery.easing.1.1.js), and the LavaLamp plugin [here]({{ site.baseurl }}/jquery/lavalamp/js/jquery.lavalamp.js).


Next, in the document.ready event, fire a call to initialize the menu. You have the option to supply an easing “fx” , the “speed” with which the animation happens and a callback to be executed when a menu-item is clicked. They are optional, the default “fx” being “linear” and the default “speed” being “500” ms.


That’s it. At this point you should have a working version of LavaLamp menu for your site.


### Bonus


Just with some minor changes in the style sheet, you can get a totally different look n feel for the menu. And yes, the HTML markup and the Javascript remain the same. Click on the image below to experience the demo for this underline-imageless lavalamp.
Here is one more variation, again with just some minor changes to the style sheet. I know, they don’t look pretty, but all i am saying is that you are limited only by your imagination. Click on the image below to see the demo for this boxed-imageless lavalamp.
Finally, for your convenience, i have [zipped]({{ site.baseurl }}/jquery/lavalamp/zip/lavalamp-0.2.0.zip) up all the necessary files into a cohesive package. [Download it]({{ site.baseurl }}/jquery/lavalamp/zip/lavalamp-0.2.0.zip), and open the demo.html to see all the 3 variations in one page.


Feel free to leave a comment with your feedback, suggestions, requests etc.


## Update


Based on popular request, LavaLamp Menu has been updated to support jquery 1.2.x versions. [Download the zip file]({{ site.baseurl }}/jquery/lavalamp/zip/lavalamp-0.2.0.zip) for version 0.2.0 of LavaLamp and open the demo.html to check it out for yourself. Since Firefox 3 has some issues with $(document).ready() function, try using $(window).load() instead if you face any problems. Hopefully a future version of Firefox or jQuery will fix the problem.