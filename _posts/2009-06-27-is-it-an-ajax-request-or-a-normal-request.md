---
layout: post
title: "Is it an AJAX Request or a Normal Request?"
date: 2009-06-27 12:00:00 +0000
tags: [General]
original_url: "/2009/06/27/is-it-an-ajax-request-or-a-normal-request.html"
---

In modern web application development, many a times you would want to know if the incoming HTTP Request is an AJAX request or just a Normal request. Have you come across this requirement? I have, and the solution that I found turned out to be pretty straight-forward and I will be sharing it with you here. 


Whenever an AJAX request is sent to the server, a special header named *X-Requested-With* with a value of *XMLHttpRequest* is attached to the request. So, a simple check to see whether the *X-Requested-With* header has a value of *XMLHttpRequest* solves the challenge. An example will give you more clarity. Take a look at the examples of *isAjax()* methods in two famous server-side programming languages – Java and PHP. 


**Java:**


```

public static boolean isAjax(request) {
   return "XMLHttpRequest"
             .equals(request.getHeader("X-Requested-With"));
}

```


**PHP:**


```

function isAjax() {
   return (isset($_SERVER['HTTP_X_REQUESTED_WITH']) 
              && 
            ($_SERVER['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest'));
}

```


From the code above, it should be clear that if the method returns *true*, then you received an AJAX request. If the method returns *false*, you received a Normal HTTP Request.


Now you know how to find out if it is an AJAX request or not. But how is it useful? What do you do with it?


Have you heard of the term *Unobtrusive javascript*. Come on, It is a buzzword these days. There is a lot to writing Unobtrusive javascript code, but one of its features – Progressive Enhancement – stands out from the rest. Again, let me explain this with an example.


Let us assume that you have designed a beautiful looking web page with tabbed navigation. Being a hard-core AJAX fan and an efficiency aficionado you don’t like to bring back a full page with the headers and the footers and the sidebars when your user clicks on a *Tab*. Instead you would love to bring back only the content area for the tab via AJAX and innerHTML it into its respective place. Correct? The good programmer inside you has also told that you should not hard-code the URL for the AJAX call in your javascript. Instead, your tab should be designed as an *anchor* whose *href* attribute points to the URL for the content. So far so good? Now, when the user clicks on the *Tab*, you collect the URL from its *href* attribute and fire an AJAX call to the server. The server obediently accepts the request and sends back the content just for the active tab.  


```

<ul>
   <li><a href="{{ site.baseurl }}/tab1.page" rel="#tab1">Tab 1</a></li>
   <li><a href="{{ site.baseurl }}/tab2.page" rel="#tab2">Tab 2</a></li>
   <li><a href="{{ site.baseurl }}/tab3.page" rel="#tab3">Tab 3</a></li>
</ul>

<div>
   <div id="tab1">Content for Tab1</div>
   <div id="tab2"> Content for Tab2 </div>
   <div id="tab3"> Content for Tab3 </div>
</div>

```


You would like to believe that all is well and good… Unfortuntately this is where the challenge of *Progressive Enhancement* begins. How do you plan to support browsers with JavaScript disabled. Yes, there are quite a few people who still do that for the fear of script related worms. How do you plan to support automated bots? Don’t you want the Google bots and the Yahoo bots to index all your pages with full content? Do you know what these users will see? They will see a half-baked page with just the active tab’s content and no styles – not even the header, footer or the sidebar. I am sure you don’t want this to happen. That is when the *isAjax()* method comes useful.


Whatever you did on the client side – HTML, CSS and javascript – is great and perfect. You separated the behavior from style and markup. So, you don’t have to touch it. You just need to do a small bit of work on the server-side. 


In our case, when JavaScript is disabled, the browser will take over and execute its default behaviour of firing a Normal request to the URL specified in the *href* attribute. When JavaScript is enabled, JavaScript will take over and will fire an AJAX request to the same URL. In both cases the same server-side resource (like in Java or PHP) will receive the request. Now that you have decided to support *Progressive Enhancement*, you will have to check if the incoming request is an AJAX request or a Normal request using the *isAjax()* method shown earlier. In case of an AJAX request, you will send back only the content area of the tab thereby providing an efficient version of your application to JavaScript enabled users. In case of a Normal request, you will send back an entire page including the tab’s content, thereby providing a less efficient yet fully functional version of your application to JavaScript disabled users. 


```

// Pseudo Code
if(isAjax(request) {
   return "Content area for the tab";
} else {
   return "Full page including tab content";
}

```


Now you can feel proud that you are not one of those who just talk about Unobtrusive JavaScript but you are one of those who have implemented it. I sincerely hope this article was useful. Feel free to drop in a comment with suggestions and/or feedback.


## Update 1:


Based on the input provided by a [buddy called Sabob](http://www.dzone.com/links/users/profile/261337.html) from [dzone](http://www.dzone.com/links/is_it_an_ajax_request_or_a_normal_request.html), *X-Requested-With* is set only by AJAX libraries like jQuery, Mootools, Prototype etc. If you are coding AJAX by hand, then you will have to explicitly set this header while sending a request. More importantly you should somehow abstract it using good OO principles so that you don’t have to explicitly code this line every time you send an AJAX request.