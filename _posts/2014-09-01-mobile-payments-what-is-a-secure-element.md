---
layout: post
title: "Mobile Payments: What is a Secure Element?"
date: 2014-09-01 12:00:00 +0000
tags: [Mobile Payments]
original_url: "/2014/09/01/mobile-payments-what-is-a-secure-element.html"
---
#### What is a Secure Element (SE)?


[GlobalPlatform](http://www.globalplatform.org/) defines Secure Element (SE) as a tamper-resistant platform capable of securely hosting applications and their confidential and cryptographic data in accordance with the rules and security requirements set forth by a set of well-identified trusted authorities. Put simply, a Secure Element can be considered to be a chip that offers a dynamic environment to store data securely, process data securely and perform communication with external entities securely. If you try to mess with it by tampering in any form, it may self-destruct, but will not allow you to gain unauthorized access.


While not all [NFC](/2014/08/03/mobile-payments-what-is-nfc.html) applications require security, those that involve financial transactions do. The Secure Element resides in highly secure cryto chips. It also provides delimited memory for each application stored in it and other functions that can encrypt, decrypt and sign the data packet.


In today’s smartphones, a Secure Element can be found as a chip `embedded` directly into the phone’s hardware, or in a `SIM/UICC` card provided by your network operator or in an `SD card` that can be inserted into the mobile phone.


To put things into context, when you are using an NFC enabled mobile device to [Tap & Pay](/2014/05/11/mobile-payments-what-is-tap-pay.html), the NFC controller goes into [card-emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) mode. The NFC controller itself does not deal with the data or processing associated with the payment transaction. It is just an interface that allows communication using standard protocols.


It is the Secure Element that actually emulates the [contactless card](/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html). It performs handshake with the terminal, sends the right responses to the right queries, generates dynamic cryptograms, authenticates the stored card and so on.  To take it a step further and be even more accurate, it is not the Secure Element that emulates the card. The software that emulates a [contactless card](/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) is the one that is stored inside the secure element in the form of payment applications or applets. The Secure Element provides secure storage and execution environment for the payment applications to do its job.


Secure Element is not a necessity to emulate contactless cards although it is the most secure to date. An alternative is to use Host-based Card Emulation (HCE) which moves the secure storage and execution environment to the cloud instead of the Secure Element. We will discuss `HCE` next.

<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
Welcome to the <a href="/2014/01/24/mobile-payments-faq-and-not-so-faq.html">Mobile payments FAQ and not so FAQ</a> series and you are on FAQ #14. The idea behind this series is to share and learn as much as possible about the field of mobile payments. If you like, you can read all of the FAQs on the <a href="http://www.gmarwaha.com/blog/category/mobile-payments/">Mobile Payments</a> category or by visiting the <a href="/articles/mobile-payments-faq/">Table of contents</a> page.</div>
