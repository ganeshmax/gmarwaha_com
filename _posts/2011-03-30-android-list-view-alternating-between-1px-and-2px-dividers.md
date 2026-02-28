---
layout: post
title: "Android: List View alternating between 1px and 2px dividers"
date: 2011-03-30 12:00:00 +0000
tags: [Android]
original_url: "/2011/03/30/android-list-view-alternating-between-1px-and-2px-dividers.html"
---

Have you faced a problem with Android ListView where the dividers alternate between 1 pixel and 2 pixel thickness although you have specifically styled it to 1px? I am sure many have, but for some reason they seem to ignore it. I say this because I noticed this problem in quite a few apps in the market. When I found the same problem in one of my apps, I decided to fix it although it was not at the top of my priority list. 


![1px_wrong](/assets/images/posts/1px_wrong.png)


The first solution I came up with was more of a work-around. Instead of using a 1px divider line, I tried using a 1px thick image as @drawable. It worked out surprisingly well on my HTC Desire but was not without its own problems. On low-end android phones the dividers started to blink when the user scrolls the list. Sometimes they disappeared and never re-appeared. I guess it is some kind of a refresh problem. I even noticed this kind of behaviour in a few market apps. So, that approach didn’t work out very well… 


Then after quite a bit of fiddling around, I found out the root cause of the problem. My app was running in compatibility mode!!! Man, how could I have not noticed that? Anyway, when I tried setting the minSdkVersion in my android manifest to version 4 and the targetSdkVersion to the version 8 the problem disappeared completely. I could now use a plain 1px divider line and there were no problems. 


![1px_right](/assets/images/posts/1px_right.png)


```

  <uses-sdk android:minSdkVersion="4"
          android:targetSdkVersion="8"
    />

```


I just thought of sharing it with the world just in case someone runs into the same road block…