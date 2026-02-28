---
layout: post
title: "Mobile Payments: What is NFC Card Emulation Mode?"
date: 2014-08-07 12:00:00 +0000
tags: [Mobile Payments, NFC]
original_url: "/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html"
---
#### What is NFC Card Emulation Mode?


An [NFC](/2014/08/03/mobile-payments-what-is-nfc.html) enabled device can operate in three different modes – `reader/writer` mode, `peer-to-peer` mode and the all important `card-emulation` mode.


In **Reader/Writer mode**, an NFC device behaves as a reader for NFC tags, such as the [contactless smart cards](/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) and RFID tags. It detects a tag immediately in close proximity by using collision avoidance mechanism. Once detected, it can either read data from or write data to the detected tag. Smart posters are an important application for this mode.


In **Peer-to-Peer mode**, two NFC enabled devices can exchange information between each other. This is the mode used by Android Beam technology. Exchanging photos, business cards and money transfer between friends are some of the applications for this mode.


In **Card-emulation mode**, an NFC device behaves like a [contactless smart card](/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html). In this mode, the mobile phone does not generate its own RF field; the NFC reader creates this field instead. So, as long a mobile platform supports the emulation of protocols surrounding `ISO/IEC 14443` that regular contactless cards use, we should be good. Both Android and Blackberry does that and can therefore be used to emulate contactless cards. In this mode, we can use our mobile phone in place of credit cards, debit cards, transit cards, access cards and so on.

<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
Welcome to the <a href="/2014/01/24/mobile-payments-faq-and-not-so-faq.html">Mobile payments FAQ and not so FAQ</a> series and you are on FAQ #13. The idea behind this series is to share and learn as much as possible about the field of mobile payments. If you like, you can read all of the FAQs on the <a href="{{ site.baseurl }}/tags/mobile-payments/">Mobile Payments</a> category or by visiting the <a href="/articles/mobile-payments-faq/">Table of contents</a> page.</div>
