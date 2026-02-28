---
layout: post
title: "Apple Pay – An attempt to demystify"
date: 2014-09-24 12:00:00 +0000
tags: [Apple Pay]
original_url: "/2014/09/24/apple-pay-an-attempt-to-demystify.html"
---

#### Update as of Jan 3, 2015


This post was written in the early days after ApplePay’s announcement, when most of us didn’t have access to enough information on its inner workings. Even with such limited information, many parts of the post turned out to be correct, but some turned out to be wrong too. Consequently, I have taken a **[second attempt at demystifying ApplePay in this other post]({{ site.baseurl }}/2015/01/03/apple-pay-an-attempt-to-demystify-take-2.html)** based on what we know at this time. The rest of this post is not modified.


When Apple announced [ApplePay](https://www.apple.com/iphone-6/apple-pay/) as a service on September 9th, 2014 and subsequently in their [press release](http://www.apple.com/pr/library/2014/09/09Apple-Announces-Apple-Pay.html), they mentioned a few key terms like [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html), Tokens, One time unique number, Device account number, dynamic security code and such. Take a look at the 4th paragraph in their [press release](http://www.apple.com/pr/library/2014/09/09Apple-Announces-Apple-Pay.html) to see what I mean. For the layman, this could mean that apple has used some complex security technology to make ApplePay secure; but for some people in the field of mobile payments and security, it was not very clear what Apple was trying to say. So, let’s try and dissect that, shall we?


For simplicity, we are only going to discuss about ApplePay in the context of a payment made at a physical [POS](javascript:void(0)) and not the mCommerce version of the service. This is only an educated attempt to understand the underlying implementation while the reality could well, be different.


Let’s start with the [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html) (SE). ApplePay stores the payment credentials inside the [SE]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html). It does not store them in the cloud and it does not store them within the host operating system. This means that none of the iOS apps will have access to the payment information stored within the [SE]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html).


#### What exactly is stored in the SE?


When, you as a customer add a credit card to your Passbook ([Mobile Wallet]({{ site.baseurl }}/2014/07/16/mobile-payments-what-is-a-mobile-wallet.html)), the simplest thing for the wallet to do would be to store the real payment credentials like the Primary Account Number (PAN) into the [SE]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html). But that is a naive implementation and Apple does not do that. ApplePay instead stores something called a token and some associated data inside the [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html).


#### What is a token?


Token is like a fake credit card number that looks and feels like a credit card number for most intents and purposes, but it is not the real deal. During transaction authorization the token would be `de-tokenized` into the real PAN before passing on to the Issuer for authorization. The entity that places a request to `de-tokenize` differs depending on the tokenization standard used. In proprietary tokenization technologies, an [Acquirer]({{ site.baseurl }}/2014/02/12/mobile-payments-who-is-an-acquirer.html) would be responsible for `tokenization` and `de-tokenization`. But, ApplePay uses the latest in [tokenization standard](http://www.emvco.com/specifications.aspx?id=263) created by [EMVCo](http://www.emvco.com/). In this case, the [payment network]({{ site.baseurl }}/2014/03/21/mobile-payments-who-is-a-payment-network.html) performs `de-tokenization`.


#### How is a token provisioned to the SE?


Now that we know that a Token is stored in the [SE]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html), the next step is to find out how it gets provisioned there in the first place. There are many ways in which this could have been implemented and we will not know for sure until Apple announces its implementation. But, here is an educated guess I would go with…


When a customer adds a credit card to their wallet, the [PAN](javascript:void(0)) details are submitted to ApplePay servers. ApplePay sends the information over to the corresponding [Issuer]({{ site.baseurl }}/2014/02/05/mobile-payments-who-is-an-issuer.html) bank asking for a Token in return. The [Issuer]({{ site.baseurl }}/2014/02/05/mobile-payments-who-is-an-issuer.html) bank calls a Token Service Provider (TSP) and requests for a token. As far as I know, the [payment network]({{ site.baseurl }}/2014/03/21/mobile-payments-who-is-a-payment-network.html) themselves play the role of TSP at present.


The [TSP](javascript:void(0)) vaults the [PAN](javascript:void(0)), maps it to a token and returns the token and a token-key. This token-key will later be used to generate a dynamic `cryptogram` at the [SE]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html). The [Issuer]({{ site.baseurl }}/2014/02/05/mobile-payments-who-is-an-issuer.html) receives a token and token-key, and adds a cvv-key to the mix. The cvv-key will be later used to generate a dynamic security code at the SE. The Issuer returns the token, token-key and cvv-key back to ApplePay. ApplePay, acting as its own Trusted Service Manager (TSM) provisions the token, token-key, cvv-key and maybe other data into the Secure Element. It is the Token that Apple calls as “Device Account Number” in its [press release](http://www.apple.com/pr/library/2014/09/09Apple-Announces-Apple-Pay.html).


#### What happens when a payment transaction is initiated?


When a customer taps or waves their iPhone in front of a point of sale terminal, a payment transaction is initiated. ApplePay uses [EMVCo’s Contactless](http://www.emvco.com/specifications.aspx?id=21) suite of specifications to communicate with the contactless reader terminal. When it is time for the Secure Element to send information to the terminal, it does two things. First, it generates a **dynamic cryptogram** using a combination of the token, token-key, transaction amount, transaction counter etc. Second, it generates a **dynamic CVV** value using the cvv-key. Finally, it passes the token, the dynamic cryptogram, the dynamic CVV and other payment and chip data elements to the terminal using the EMV specification.


Let’s stop for a moment here and review what just happened and compare that to Apple’s [press release](http://www.apple.com/pr/library/2014/09/09Apple-Announces-Apple-Pay.html) as quoted below.


> 

“Each transaction is authorized with a **one-time unique number** using your **Device Account Number** and instead of using the security code from the back of your card, Apple Pay creates a **dynamic security code** to securely validate each transaction.”- From the press release


From the quote above, the `Device Account Number` represents the `Token`, the `One-time Unique Number` represents the `dynamic cryptogram` and the `Dynamic Security Code` represents the `dynamic CVV`.


#### What happens during a payment transaction?


The contactless terminal receives the token, dynamic cryptogram, dynamic CVV and other data elements according to the [contactless EMV](http://www.emvco.com/specifications.aspx?id=21) specification (or contactless MSD for backwards compatibility) and sends them over to the [Acquirer]({{ site.baseurl }}/2014/02/12/mobile-payments-who-is-an-acquirer.html). The Acquirer doesn’t know or care if the incoming PAN is a token PAN or the real PAN. They just identifiy the payment network based on the BIN and send it over the corresponding payment network.


The [payment network]({{ site.baseurl }}/2014/03/21/mobile-payments-who-is-a-payment-network.html) identifies that it is a tokenized PAN and not a real PAN based on [BIN](javascript:void(0)) tables. Consequently, they send a request out to the [TSP](javascript:void(0)) to de-tokenize passing in the Token and the dynamic cryptogram. The TSP, among other things, validates the cryptogram using the token-key that it shared earlier during the provisioning process. If the cryptogram is valid, the TSP de-tokenizes and returns the real PAN back to the payment network. The payment network attaches the real PAN to the authorization request and sends it over to the Issuer for authorization.


The Issuer validates the dynamic CVV based on the cvv-key it shared earlier during the provisioning process. Then it authorizes the transaction depending on the customer’s account status. The authorization status flows back from the Issuer to the Payment network, back to the Acquirer and back to the Merchant where your receipt gets printed.


In conclusion, we saw how ApplePay does provisioning and how a payment transaction is processed. For some of us this is good enough information to understand the security strategy used by ApplePay. But some others may have more questions. What happens when the Card is lost? What happens when the phone is lost? What happens when the merchant is compromised? How does ApplePay handle these challenges? These are all very good questions, but this post has already become too big. So, I will address those follow-up questions in my next post. Stay tuned!


Reprinted from my own article [here](http://www.virtusa.com/blog/2014/09/applepay-an-attempt-to-demystify-apples-new-service/)



<div class="related-reading">
<p class="related-reading-title">Related Reading</p>
<ul>
    <li><a href="{{ site.baseurl }}/articles/mobile-payments-faq/">Mobile Payments FAQ and not so FAQ</a></li>
    <li><a href="{{ site.baseurl }}/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html">Apple Pay vs Google Wallet: The Secure Element</a></li>
    <li><a href="{{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html">What is a Contactless Chip Card?</a></li>
    <li><a href="{{ site.baseurl }}/2014/08/03/mobile-payments-what-is-nfc.html">What is NFC?</a></li>
    <li><a href="{{ site.baseurl }}/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html">What is NFC Card Emulation Mode?</a></li>
    <li><a href="{{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html">What is a Secure Element?</a></li>
</ul>
</div>

