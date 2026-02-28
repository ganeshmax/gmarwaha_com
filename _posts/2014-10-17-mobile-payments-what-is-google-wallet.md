---
layout: post
title: "Mobile Payments: What is Google Wallet?"
date: 2014-10-17 12:00:00 +0000
tags: [Mobile Payments, Google Wallet]
original_url: "/2014/10/17/mobile-payments-what-is-google-wallet.html"
---
#### What is Google Wallet?


Google Wallet is a [mobile/digital wallet]({{ site.baseurl }}/2014/07/16/mobile-payments-what-is-a-mobile-wallet.html) developed by Google. Their grand vision probably is to replace the complete physical wallet with its virtual counterpart. They are not there yet, but in the process of marching towards their grand vision, they have created a few important services. We will discuss them one by one in a moment.


Google Wallet has been around since 2011 and has seen at least 3 major revisions. Each version had a very different technical approach to mobile payments mostly because of the politically difficult landscape that surrounds it. We will discuss each version, challenges faced and how they achieve mobile payments in separate posts later. In this post, we will assume the third (and latest) version of Google Wallet. This version was released along with Android Kit-Kat and it uses [Host-based Card Emulation]({{ site.baseurl }}/2014/09/20/mobile-payments-what-is-hce.html) instead of [Secure Element]({{ site.baseurl }}/2014/09/01/mobile-payments-what-is-a-secure-element.html) based [Card Emulation]({{ site.baseurl }}/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode.html).


As a consumer you can add your debit cards, credit cards, stored value cards, loyalty cards, gift cards etc. to your Google Wallet account either on their website or using the Google Wallet app on your smartphone. You may even add some money directly to your wallet account balance.


#### Pay at Physical POS:


Using this service, you can use your [NFC]({{ site.baseurl }}/2014/08/03/mobile-payments-what-is-nfc.html) enabled `Android` phone to purchase in-store by just [tapping]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-tap-pay.html) your phone against a contactless terminal. The contactless terminals are not Google specific; they already exist in the wild and support [contactless cards]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) from Visa (PayWave) and MasterCard (PayPass). Google just uses the same standard protocols used by the [Contactless cards]({{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) so as to be compatible with existing infrastructure.


![google-wallet-tap]({{ site.baseurl }}/assets/images/posts/google-wallet-tap.jpg)


Google has also developed a proprietary protocol on top of existing Contactless protocols to support making payments, redeeming coupons/offers and receiving loyalty all with just one tap. But for this to work, the merchants will have to upgrade their terminal to explicitly support Google’s own protocol.


But there is a big challenge with contactless terminals. Today, they are not very common with retailers in the United States. Most of the retailers still have only traditional [Magnetic Stripe]({{ site.baseurl }}/2014/04/10/mobile-payments-what-is-a-magnetic-stripe-card.html) terminals. Eventually, the expectation is that all merchants will have a contactless terminal, but in the meantime, we need a solution. To fill this gap, Google Wallet also offers a Debit card from MasterCard that has a [Magnetic Stripe]({{ site.baseurl }}/2014/04/10/mobile-payments-what-is-a-magnetic-stripe-card.html) interface. So, if a merchant does not have a contactless terminal, you can still use the Google Wallet Debit card to make a payment.


![google-wallet-debit-card]({{ site.baseurl }}/assets/images/posts/google-wallet-debit-card-300x221.jpg)


#### Pay Online:


Using this service, you can pay on eCommerce websites and mobile apps where you see the `Buy with Google` sign. Here, Google Wallet acts more like a digital wallet than like a mobile wallet. Google offers different APIs for sale of digital goods and sale of physical goods. The difference is that, for sale of digital goods, a seller need not have a separate relationship with a [payment processor]({{ site.baseurl }}/2014/02/12/mobile-payments-who-is-an-acquirer.html). Google will take care of the payment processing as a whole. On the other hand, for sale of physical goods, a seller would need to have a [payment processor]({{ site.baseurl }}/2014/02/12/mobile-payments-who-is-an-acquirer.html) and a merchant account with an [Acquirer]({{ site.baseurl }}/2014/02/12/mobile-payments-who-is-an-acquirer.html).


![google-wallet-buy-with-google-2]({{ site.baseurl }}/assets/images/posts/google-wallet-buy-with-google-2-291x300.png)


#### Pay Friends:


Using this service, you can use Google wallet to send money to anyone in the US with an email address. This service is generally used to pay friends, split bills and sometimes referred to as Person to Person payments or P2P for short. Recently, Google also added the ability to send money as an email attachment when using Gmail as the email provider.


![google-wallet-pay-friends]({{ site.baseurl }}/assets/images/posts/google-wallet-pay-friends-180x300.png)



<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
<ul>
    <li><a href="{{ site.baseurl }}/articles/mobile-payments-faq/">Mobile Payments FAQ</a></li>
    <li><a href="{{ site.baseurl }}/2014/08/03/mobile-payments-what-is-nfc.html">What is NFC?</a></li>
    <li><a href="{{ site.baseurl }}/2014/09/20/mobile-payments-what-is-hce.html">What is HCE?</a></li>
    <li><a href="{{ site.baseurl }}/2014/07/16/mobile-payments-what-is-a-mobile-wallet.html">What is a Mobile Wallet?</a></li>
    <li><a href="{{ site.baseurl }}/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html">What is Contactless Chip Card?</a></li>
    <li><a href="{{ site.baseurl }}/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html">Apple Pay vs Google Wallet : The Secure Element</a></li>
</ul>
</div>

