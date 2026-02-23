---
layout: post
title: "Final Modifier for method arguments. What do you think?"
date: 2010-01-02 12:00:00 +0000
tags: [General]
original_url: "/2010/01/02/final-modifier-for-method-arguments-what-do-you-think.html"
---

The IT industry today is sodden with TLAs like SOA, ESB… and FLAs like AJAX, SOAP and JUNK. i was thinking about refreshing myself with some fundamentals again. Blogging about a basic concept may not be cool, but refreshing – don’t you think? I know what you are thinking. You are thinking that i am digressing too much. Ok, lets cut to the chase.


One of the best practices i follow religiously is to use final modifiers for method arguments where applicable. This is *“supposedly”* a best-practice written by somebody somewhere. Regardless of whether it is documented as a best-practice or not it is an important concept to understand and use. I have 2 valid reasons to use them for my method arguments. 


First, final variables cannot be modified. Come on, everybody knows that. Maybe, but its use is significantly enhanced when it is a method argument and more importantly when you are in a big team environment. 


Lets assume that a method takes *List* as its argument. Typically, the intention of that method is to work with the *List* – add to it, remove elements from it, use its elements in some way, sort it and what not. Consequently when the method returns, the *caller* can investigate the passed List and work with the modifications the *callee* introduced. But the *caller* will be on for a big surprise if the *callee* changes the instance that reference points to itself. 


We know that java uses “Pass by copy of reference”. If the *callee* points the received reference to a different *List* and then modifies this *List*, the *caller* will not be able to see any change at all. This is because the copy of the reference held by the *caller* still points to the same old *List*. More often than not this is done by mistake and is not intentional. If such a behavior is intentional, final modifier is not required. In all other cases since this leads to bugs in code, it is a good practice to use final modifier for method arguments.


Second, if the method uses the infamous anonymous inner-class syntax to do something, and that inner class wants to use the methods arguments, java requires those arguments to be declared final. This is more of a rule than a valid reason. 


Are there more valid reasons? I will be glad to receive information from you guys.