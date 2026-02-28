---
layout: post
title: "jCarousel Lite – A jQuery plugin"
date: 2007-08-09 12:00:00 +0000
tags: [jQuery, jCarouselLite]
original_url: "/2007/08/09/jcarousel-lite-a-jquery-plugin.html"
---
[jCarousel Lite]({{ site.baseurl }}/projects/jcarousellite/) is a [jQuery](http://jquery.com) plugin that carries you on a carousel ride filled with images and HTML content. Put simply, you can navigate images and/or HTML in a carousel-style widget. It is super light weight, at about *2 KB in size*, yet very flexible and customizable to fit most of our needs.

**Did I mention that it weighs just 2 KB?**


As if that wasn’t enough, the best part is yet to come… You don’t need any special css file or class name to get this to work. Include the js file. Supply the HTML markup. Then, construct the carousel with just a simple function call.


Visit the [project]({{ site.baseurl }}/projects/jcarousellite/) page for more information. There you can find a lot of [demos]({{ site.baseurl }}/projects/jcarousellite/demo/) and exhaustive documentation. This blog entry is just a teaser for further exploration.


Installing and getting it to work is as trivial as following the 3 steps given below…


#### Step 1:


Include a reference to the jQuery library and the `jCarouselLite` plugin. You can download [jQuery here](http://jquery.com) and [jCarouselLite here]({{ site.baseurl }}/jquery/jcarousellite/download.php). If you like interesting effects, include the [Easing plugin](http://gsgd.co.uk/sandbox/jquery/easing/) as well (Optional). You may also want to use a [compatibility easing plugin](http://gsgd.co.uk/sandbox/jquery/easing/) if you want to use old easing names. If you would like to navigate the carousel using mouse wheel, then include the [mouse-wheel plugin](https://github.com/brandonaaron/jquery-mousewheel) as well (Optional).


```
<script type="text/javascript" src="path/to/jquery.js"></script>
<script type="text/javascript" src="path/to/jquery.jcarousellite.js"></script>

<!-- Optional -->
<script type="text/javascript" src="path/to/easing.js"></script>
<script type="text/javascript" src="path/to/mousewheel.js"></script>

```


#### Step 2:


In your HTML file, provide the markup required by the carousel (a `div` enclosing an `ul`). You also need the navigation buttons, but these buttons need not be part of the carousel markup itself. An example follows…


```
<button class="prev">&laquo;</button>
<button class="next">&raquo;</button>

<div class="any-class">
    <ul>
        <li><img src="image/1.jpg" style="width:150px; height:118px;"></li>
        <li><img src="image/2.jpg" style="width:150px; height:118px;"></li>
        <li><img src="image/3.jpg" style="width:150px; height:118px;"></li>
        <li><img src="image/4.jpg" style="width:150px; height:118px;"></li>
        <li><img src="image/5.jpg" style="width:150px; height:118px;"></li>
    </ul>
</div>

```


#### Step 3:


Fire a call to the plugin and supply your navigation buttons. You just managed to architect your own carousel.


```
$(function() {
    $(".any-class").jCarouselLite({
        btnNext: ".next",
        btnPrev: ".prev"
    });
});

```


If you have any comments/suggestions/requests, feel free to drop in a comment or reach @ganeshmax in twitter.


 


#### Update


Based on popular request, jCarouselLite has been updated to support jquery 1.2.x versions. Goto the [download page]({{ site.baseurl }}/projects/jcarousellite/#download) and download version 1.0.1 to enjoy jquery 1.2.x support. Since Firefox 3 has some issues with $(document).ready() function, try using $(window).load() instead if you face any problems. Hopefully a future version of Firefox or jQuery will fix the problem.