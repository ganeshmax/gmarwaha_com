---
layout: post
title: "Mobile Payments: What is HCE?"
date: 2014-09-20 12:00:00 +0000
tags: [Mobile Payments]
original_url: "/2014/09/20/mobile-payments-what-is-hce.html"
---
#### What is HCE?


Previously, we discussed about [Secure Element](/2014/09/01/mobile-payments-what-is-a-secure-element.html) and how it enables payment transactions in [card-emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) mode. We also briefly discussed that SE is not the only choice available. Today, we also have HCE as an alternative. HCE stands for `Host-based Card Emulation`. As its name suggests, it has something to do with [card-emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) mode. But what does host-based mean? Before we talk about what host-based means, let’s review how things were before HCE.


Prior to HCE, the only way to emulate a card using a mobile [NFC](/2014/08/03/mobile-payments-what-is-nfc.html) device was to use a Secure Element. Let’s take the Android platform as an example. Here, the host operating system (Android in this case) and its apps do not get involved with a payment transaction at all.


![se-ce](http://www.gmarwaha.com/blog/wp-content/uploads/2014/09/se-ce.png)


When a consumer holds the device over an NFC terminal, the NFC controller in the device routes all data from the reader directly to the Secure Element. The Secure Element itself performs the communication with the NFC terminal, and no Android application is ever involved in the transaction. After the transaction is complete, an Android application can query the Secure Element directly for the transaction status and notify the user. This is the approach used by [ApplePay](https://www.apple.com/iphone-6/apple-pay/) as well


This SE based approach is inherently secure and that is a very big advantage. But, there are some downsides too. The SE owner owns the key to the kingdom. All others will have to go through complex business models, partnerships, and dependencies to gain access and it makes the whole process that much more complex and expensive. Moreover, the SE itself has only limited storage capacity and processing speed.


The alternative is to use Host-based Card Emulation. Here, the host operating system (Android) and its apps gets involved with a payment transaction.


![hce-ce](http://www.gmarwaha.com/blog/wp-content/uploads/2014/09/hce-ce.png)


When a consumer holds the device over an NFC terminal, the NFC controller in the device routes all data from the reader directly to the Host CPU on which Android applications are running directly. Then, an Android application (a Mobile Wallet) that deals with a particular payment application can do its magic and provide for the card emulation requests and responses.


Since the host CPU is inherently insecure, any mobile wallet worth its salt will not store the real payment credentials inside the phone. Google Wallet for example moves all such data to a hosted cloud environment, and that is where the secure storage and secure processing takes place. In essence, we have moved the Secure Element from inside a chip to a cloud environment (HCE Cloud) instead.


This approach has its downsides – like security and a need for data connection. This does not mean that your private information is vulnerable. We can still have a very high degree of security using other technologies. Payment card `Tokenization` is one of them and we will discuss it in an upcoming post. On the bright side, the complex business models, partnerships and access restriction to SE can be dramatically simplified. This enables payment application issuers to easily provision to the cloud and get it over with.


Using SE-based Card Emulation and Host-based Card Emulation is not an either-or scenario though. Android allows both to co-exist in the same NFC enabled device and offers tools and technologies to work with both of them as shown in the diagram below.


![se-hce-dual-ce](http://www.gmarwaha.com/blog/wp-content/uploads/2014/09/se-hce-dual-ce.png)


All the above diagrams were taken from [Android developers](https://developer.android.com/guide/topics/connectivity/nfc/hce.html) website.



<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
<ul>
    <li><a href="http://www.gmarwaha.com/blog/mobile-payments-faq/">Mobile Payments FAQ</a></li>
    <li><a href="/2014/08/03/mobile-payments-what-is-nfc.html">What is NFC?</a></li>
    <li><a href="/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html">What is NFC Card Emulation Mode?</a></li>
    <li><a href="/2014/09/01/mobile-payments-what-is-a-secure-element.html">What is a Secure Element?</a></li>
    <li><a href="/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html">Apple Pay vs Google Wallet : The Secure Element</a></li>
</ul>
</div>

