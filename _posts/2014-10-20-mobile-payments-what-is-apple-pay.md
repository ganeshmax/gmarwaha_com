---
layout: post
title: "Mobile Payments: What is Apple Pay?"
date: 2014-10-20 12:00:00 +0000
tags: [Mobile Payments, Apple Pay]
original_url: "/2014/10/20/mobile-payments-what-is-apple-pay.html"
---
#### What is Apple Pay?


ApplePay is a [mobile payment]({{ site.baseurl }}/2014/07/06/mobile-payments-what-is-mobile-payment.html) service developed by Apple and is scheduled to be operative starting October 20, 2014. It offers two different services and we will discuss them briefly here.


#### Service 1 – Pay in-store:


With this service you can use your [NFC]({{ site.baseurl }}/2014/08/03/mobile-payments-what-is-nfc.html) enabled iPhone 6 or iPhone 6 Plus or Apple Watch to purchase `in-store` by just [tapping]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-tap-pay.html) your phone against a contactless terminal and placing your fingers on the `Touch ID`. The contactless terminals are not Apple specific; they already exist in the wild and support [contactless cards]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) from Visa (PayWave) and MasterCard (PayPass). Apple just uses the same standard protocols used by the [Contactless cards]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) so as to be compatible with existing infrastructure.


![apple-pay-pos]({{ site.baseurl }}/assets/images/posts/apple-pay-pos.jpg)


To support such `in-store` payments, ApplePay stores the necessary payment data inside a [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html) embedded in the phone’s hardware itself. When you tap to pay, ApplePay uses [Secure Element]({{ site.baseurl }}/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html) based [card-emulation]({{ site.baseurl }}/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html) to transmit payment data to the contactless terminal. For a more detailed analysis of how ApplePay works behind the scenes, visit my blog post on [Apple Pay – An Attempt to Demystify]({{ site.baseurl }}/2014/09/24/apple-pay-an-attempt-to-demystify.html).


Beyond the basics, there are a few more interesting things that are unique to ApplePay. They are


- Real payment card data is never stored inside the phone’s [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html). A `token` – based on [EMVCo’s tokenization specification](http://www.emvco.com/specifications.aspx?id=263) – is stored instead. This way, merchants will never have access to real card details and that relieves the consumer from the fear of merchants being hacked (like the recent Target and Home Depot data breaches). Moreover, when you lose the phone, you don’t have to replace the real card. We can just provision new tokens to a new phone and be done with it.

- Every payment transaction is authenticated using Apple Touch ID (biometric fingerprint authentication). This is a very strong form of authentication, even better than the one offered by EMV based [`Chip n PIN`]({{ site.baseurl }}/2014/04/21/mobile-payments-what-is-a-contact-chip-card.html) cards.

- Even if you don’t have an iPhone 6 or iPhone 6 Plus (which are the only Apple phones with [NFC]({{ site.baseurl }}/2014/08/03/mobile-payments-what-is-nfc.html) and [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html)), you can still use ApplePay to pay at stores using a combination of Apple Watch and iPhone 5 or 5s.

- Apple does not take part in the payment authorization process and does not store any transaction related information in their servers. They don’t store your payment card details either. They are very particular about this because they want the [merchants]({{ site.baseurl }}/2014/03/07/mobile-payments-who-is-a-merchant.html) to know that Apple is not a threat to them like other wallet providers are and they want the consumers to know that their data is safe with themselves.


#### Service 2 – Pay in Mobile Apps:


Using this service, you can pay for items from within mobile apps that support ApplePay. If you have ever used the `iOS` or `OS-X` keychain to store and auto-fill passwords, this will look very familiar. Participating mobile apps will show a button labelled `Apple Pay`. Checking out is as easy as tapping that button and placing your finger on the Touch ID.


![apple-pay-app]({{ site.baseurl }}/assets/images/posts/apple-pay-app-160x300.png)



<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
<ul>
    <li><a href="{{ site.baseurl }}/articles/mobile-payments-faq/">Mobile Payments FAQ</a></li>
    <li><a href="{{ site.baseurl }}/2014/08/03/mobile-payments-what-is-nfc.html">What is NFC?</a></li>
    <li><a href="{{ site.baseurl }}/2014/10/17/mobile-payments-what-is-google-wallet.html">What is Google Wallet?</a></li>
    <li><a href="{{ site.baseurl }}/2014/09/24/apple-pay-an-attempt-to-demystify.html">Apple Pay – An attempt to demystify</a></li>
    <li><a href="{{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html">What is Contactless Chip Card?</a></li>
    <li><a href="{{ site.baseurl }}/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html">Apple Pay vs Google Wallet : The Secure Element</a></li>
</ul>
</div>

