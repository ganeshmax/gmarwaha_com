---
layout: post
title: "Mobile Payments: What is NFC?"
date: 2014-08-03 12:00:00 +0000
tags: [Mobile Payments, NFC]
original_url: "/2014/08/03/mobile-payments-what-is-nfc.html"
---
#### What is NFC?


NFC stands for Near Field Communication. It is a standard defined by the [NFC Forum](http://nfc-forum.org/), a global consortium of hardware, software, credit-card, banking, network-providers and others who are interested in the advancement and standardizing this technology. As the name implies, it’s a set of short-range wireless communication standards used in mobile phones and other electronic devices. It operates on the frequency of 13.56 MHz with data transfer of up to 424 kilobits per second.


[NFC](javascript:void(0)) and `RFID` (Radio Frequency Identification) are sometimes used interchangeably, but NFC is really a newer version or extension of RFID. RFID waves can have very long ranges as they are generally used in manufacturing, inventory and object tracking. In contrast, NFC limits the range of communication to within `2 to 4` inches. This makes NFC more suitable for secure applications like payments.


NFC allows you to share small payloads of data between an NFC tag and an NFC enabled phone or between two NFC enabled phones. This may sound more like `Bluetooth` because it is also a communication technology between two bluetooth enabled devices over a short range. Yes, they are similar in that aspect, but they are also different in other aspects. For instance, NFC doesn’t need a pairing process; it can read from passive NFC tags; it consumes low power; it connects to its target very quickly ( one tenth of a second) etc. These qualities make NFC a good candidate for mobile payments. Bluetooth has other advantages that makes it a better choice for a different set of use cases. We will discuss about Bluetooth, BLE and Beacons in a different post.


 


![]({{ site.baseurl }}/assets/images/posts/nfc.jpg)


[Contactless cards]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html), that we discussed in an earlier post, behave like NFC tags and emit NFC style radio frequency signals when provoked by a contactless reader terminal. So, in theory, a mobile phone with an NFC controller can do the same as long as they conform to the protocols defined by payment networks. And that is exactly what is happening when you use a Google or Isis wallet. We will discuss how this happens in practice in an upcoming post on `card-emulation` mode for NFC.


So, can you just replace all of your [contactless]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) credit and debit cards with Google wallet or Isis wallet and call it a day. Not yet. There are a couple of reasons for that.


First and foremost, today, contactless terminals/readers are not plentiful. There are just over 200K contactless terminals across US. The advantage of using your contactless plastic card is that it also comes with a [magstripe]({{ site.baseurl }}/2014/04/10/mobile-payments-what-is-a-magnetic-stripe-card.html) for backward compatibility with traditional terminals. We do not have that luxury with an NFC enabled phone.


Second, provisioning a contactless application to an NFC enabled phone is a much more complicated process involving a larger ecosystem of participants like `SP TSM`, `SE TSM`, `MNO`, Issuing banks and the complexity involved with security, key management and `over-the-air` provisioning cannot be discounted either. Technically, these have been solved, but not all Issuing banks are ready to invest in it yet. That said, the industry is slowly, yet steadily moving towards a digital wallet. So, it is going to happen sooner rather than later, but don’t hold your breath.

<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
Welcome to the <a href="{{ site.baseurl }}/2014/01/24/mobile-payments-faq-and-not-so-faq.html">Mobile payments FAQ and not so FAQ</a> series and you are on FAQ #12. The idea behind this series is to share and learn as much as possible about the field of mobile payments. If you like, you can read all of the FAQs on the <a href="{{ site.baseurl }}/tags/mobile-payments/">Mobile Payments</a> category or by visiting the <a href="{{ site.baseurl }}/articles/mobile-payments-faq/">Table of contents</a> page.</div>
