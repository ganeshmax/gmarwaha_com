---
layout: post
title: "jCarouselLite version 1.1 released !"
date: 2014-10-09 12:00:00 +0000
tags: [jCarouselLite]
original_url: "/2014/10/09/jcarousellite-version-1-1-released.html"
---

It has been quite a while since I worked on updating the [jCarouselLite project](/projects/jcarousellite/). Meanwhile, the community has shown its love by actively contributing features and defect fixes. It is always a pleasant experience to see such active participation by the community, but there is also a challenge.


Many of the mods were spread around different websites, GitHub forks, Stack Overflow answers and comments. Consequently, it was not easy for a new user to start using it. So, I thought I should give some order to this by collecting them all back into the [original project](https://github.com/ganeshmax/jcarousellite) and that is exactly what I have done here… and much more…


Heads up! The plugin still weighs only 2 KB.


Given below is a list of items that has changed, leading to the release of version 1.1. Visit the [project page](/projects/jcarousellite/) and [change log](http://www.gmarwaha.com/jquery/jcarousellite/change-log.php) for more details.


- Added a [Github](https://github.com/ganeshmax/jcarousellite) project. Feel free to raise any new defects or feature requests here

- Updated to support [jquery 1.11.x](http://jquery.com) version

- Fixed a few defects


- We were skipping items in a particular rare combination of `circular:true` mode and `scroll/visible/start` options. Fixed

- We were jumping to the top of the page when the navigation buttons are disabled in `circular:false` mode. Fixed

- We were unintentionally styling grand-children of the main `UL and LI`. Now it will style only the top level `UL and LI`. Fixed

- In `circular:false` mode, in a particular combination of `total/visible/scroll` options, we were unable to navigate to the last few items. Fixed

- In `auto-scroll` mode, the Interval was not getting reset when `next/prev` navigation button was clicked. Fixed

- In `circular:false` mode, with `start:0`, the `prev` button was not getting disabled. Fixed

- Fixed an issue with some minification libraries


- Changes to the project site


- Introduced a [Styling page](http://www.gmarwaha.com/jquery/jcarousellite/styling.php) to help you understand the default styling and ways in which you can apply custom styling to your carousel

- Revamped the [Demo page](/projects/jcarousellite/demo/) to make it cleaner and more beautiful. It is easier to view-source now than it was before

- Updated the styling in [Demo page](/projects/jcarousellite/demo/) to reflect the custom styling in S[tyling page](http://www.gmarwaha.com/jquery/jcarousellite/styling.php)


- Added default options globally. This way you can set the default options using `$.fn.jCarouselLite.options` once instead of passing them for every carousel you create

- Removed the separate `width()` and `height()` functions and replaced with `jQuery.outerWidth(boolean)`


At present, I am working on a few new features to the plugin and a few more additions to the project site. It will make this plugin even more useful and flexible. You can expect a 1.2 release for these enhancements in the next couple of weeks. Thanks again everyone for showing extraordinary interest in this simple and light weight carousel.