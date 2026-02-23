---
layout: post
title: "Apple Pay vs Google Wallet : The Secure Element"
date: 2014-10-02 12:00:00 +0000
tags: [Apple Pay, Google Wallet]
original_url: "/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html"
---
Note: You can read all articles in this [series](http://www.gmarwaha.com/blog/apple-pay-vs-google-wallet/) by visiting the [Table of Contents](http://www.gmarwaha.com/blog/apple-pay-vs-google-wallet/)


Both [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html) and [ApplePay](https://www.apple.com/iphone-6/apple-pay/) are trying to solve the same set of problems – mobile payments at the physical POS and inside apps. They have many characteristics that are very similar, but they also differ in significant ways when it comes to implementation and user experience. In this series of blog posts, we will analyze a few similarities and differences one by one. We will start by talking about the `Secure Element` today.


A [Secure Element](/2014/09/01/mobile-payments-what-is-a-secure-element.html) (SE) securely stores card/cardholder data and does cryptographic processing. During a payment transaction it emulates a [contactless card](/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) using industry standard protocols to help authorize a transaction. The Secure Element could either be embedded in the phone or embedded in your network operator’s SIM card. We will generically refer to them as device-based Secure Element. More recently, with the introduction of [HCE](/2014/09/20/mobile-payments-what-is-hce.html) technology by Google, the definition of Secure Element has been expanded to include a secure cloud as well. We will refer to them as cloud-based Secure Element.


In the beginning, Google Wallet v1.0 started its journey by using the device-based Secure Element for [card emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html). This approach didn’t work out well for Google as most of the major network operators (Verizon, AT&T and T-Mobile) decided to support their own brand of wallet called [Softcard](http://gosoftcard.com/) (previously [Isis](https://www.paywithisis.com/)) and blocked access to the [Secure Element](/2014/09/01/mobile-payments-what-is-a-secure-element.html) for any other wallet providers. Google had no choice but to move on.
Today, Google wallet v3.0 does not use a device-based Secure Element. It uses a technology called [Host-based card emulation](/2014/09/20/mobile-payments-what-is-hce.html) (HCE) instead, where [card-emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) and the Secure Element are separated into different areas. For example, in HCE mode, when an [NFC](/2014/08/03/mobile-payments-what-is-nfc.html) enabled Android phone is tapped against a contactless terminal, the NFC controller inside the phone redirects communication from the terminal to the host operating system. Google wallet picks up the request from the host operating system and responds to the communication with a virtual card number and uses industry standard contactless protocols to complete the transaction. This is the [card-emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) part. The transaction proceeds and reaches the Google cloud servers where the virtual card number is replaced with real card data and authorized with the real Issuer. Since the real card data is securely stored in Google’s cloud servers, the cloud represents the [Secure Element](/2014/09/01/mobile-payments-what-is-a-secure-element.html) part. In general, this approach is considered less secure compared to the embedded SE approach. But there are some areas (like Lost & Stolen use-case) where it is more secure. We will discuss that in a different post.


NOTE: This doesn’t mean that Android operating system does not support device-based Secure element anymore. In fact it supports both device-based Secure Element and HCE using a routing table at the NFC controller level.


[ApplePay](https://www.apple.com/iphone-6/apple-pay/), in contrast, works using traditional device-based Secure Element. It does not use HCE technology. Consequently, Apple does not store the real card or token data in their cloud servers at all. The on-device Secure Element essentially performs [card-emulation](/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) in addition to secure storage. It sends payment data to the contactless terminal when you [Tap & Pay](/2014/05/11/mobile-payments-what-is-tap-pay.html). I have attempted to [demystify how ApplePay works](/2014/09/24/apple-pay-an-attempt-to-demystify.html) in one of my previous posts. In many ways it is similar to how Google Wallet v1.0 used to work (with some important differences).
First, ApplePay does not store the real card data inside the SE. This is in direct contrast to Google Wallet 1.0 and Softcard. Instead, they store a token that conforms to [EMVCo](http://www.emvco.com/) [tokenization](http://www.emvco.com/specifications.aspx?id=263) specification. It is this token (along with a cryptogram) that gets sent to the contactless terminal. During the authorization flow, the [card network](/2014/03/21/mobile-payments-who-is-a-payment-network.html) identifies the token, de-tokenizes them into real PAN with the help of a Token Service Provider (TSP) and sends the real PAN over to [Issuer](/2014/02/05/mobile-payments-who-is-an-issuer.html) for authorization.


Second, Apple owns and controls the Secure Element embedded inside the device thereby avoiding unnecessary challenges from the MNOs.


Finally, Apple significantly simplified the provisioning model. If they had to provision the real card details, they would have to depend on a complex and convoluted process. Fortunately, they provision a token instead and took the opportunity to simplify the process to a bare minimum.


In the next post, we will discuss how these two services differ when the device is lost or stolen.



<div class="related-reading">
<p class="related-reading-title">Related Reading</p>
<ul>
    <li><a href="http://www.gmarwaha.com/blog/apple-pay-vs-google-wallet/">Apple Pay vs Google Wallet – Article Series</a></li>
    <li><a href="http://www.gmarwaha.com/blog/mobile-payments-faq/">Mobile Payments FAQ</a></li>
    <li><a href="/2014/09/24/apple-pay-an-attempt-to-demystify.html">Apple Pay – An attempt to demystify</a></li>
    <li><a href="/2014/10/17/mobile-payments-what-is-google-wallet.html">What is Google Wallet?</a></li>
    <li><a href="/2014/10/20/mobile-payments-what-is-apple-pay.html">What is Apple Pay?</a></li>
    <li><a href="/2014/08/03/mobile-payments-what-is-nfc.html">What is NFC?</a></li>
    <li><a href="/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html">What is NFC Card Emulation Mode?</a></li>
    <li><a href="/2014/09/01/mobile-payments-what-is-a-secure-element.html">What is a Secure Element?</a></li>
    <li><a href="/2014/09/20/mobile-payments-what-is-hce.html">What is HCE?</a></li>
</ul>
</div>

