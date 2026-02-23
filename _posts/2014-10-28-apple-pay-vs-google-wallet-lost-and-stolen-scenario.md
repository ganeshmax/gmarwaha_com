---
layout: post
title: "Apple Pay vs Google Wallet : Lost and Stolen Scenario"
date: 2014-10-28 12:00:00 +0000
tags: [Apple Pay, Google Wallet]
original_url: "/2014/10/28/apple-pay-vs-google-wallet-lost-and-stolen-scenario.html"
---

Note: You can read all articles in this [series](http://www.gmarwaha.com/blog/apple-pay-vs-google-wallet/) by visiting the [Table of Contents](http://www.gmarwaha.com/blog/apple-pay-vs-google-wallet/)


Both [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html) and [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html) give very good attention to security. In fact we can even make a blanket statement that almost all mobile wallet services are at least slightly more secure than the traditional [Magnetic Stripe](/2014/04/10/mobile-payments-what-is-a-magnetic-stripe-card.html) cards, but to be honest, that is not a correct comparison. Today, we are trying to disrupt the payment industry through innovation and modern technology. In the process we should strive to achieve unprecedented levels of revolutionary security, not just an evolutionary next step.


[ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html) and [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html) are both focussed on achieving that. Both of them deal with security at all levels within the payment lifecycle without compromising convenience to the consumers. Today, let’s talk about some similarities and differences in their security strategy when it comes to Lost and Stolen devices.


Traditionally, when we lose our physical wallet, our immediate next step is to identify all the credit cards, debit cards and stored-value cards we had in that wallet, call the respective bank’s customer service phone numbers one by one and report it as lost or stolen. It is a tedious and very involved job that no one ever likes. Between the time we realize that our wallet was stolen and the time we report it to the [Issuers](/2014/02/05/mobile-payments-who-is-an-issuer.html), we can only hope that it has not been misused for fraud. Even after the card has been reported stolen, there is still a chance of misuse based on offline transactions that is common is some places. Liability clauses aside, it is the duty of the consumer to report any suspicious activity in their account and that is another painful task. Even if we assume that the consumer is fully protected, the fraud in general has taken place and someone in the payment ecosystem is bound to lose, not the fraudster.


Now, let’s consider the scenario where you have lost your [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html) equipped Android phone or an [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html) equipped iPhone with multiple payment accounts stored inside it.


Unlike our physical wallet, which does not come with a lock and key, [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html) is protected by a PIN that only you know. In [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html), the wallet is protected using Touch ID (biometric fingerprint authentication), which only you have. A low-tech thief will not be able to breach even this `first level` of security. They will not be able to use any of the cards stored inside our wallet even though they have the wallet in their hands. I guess, they will just have to be happy with their new and shiny smartphone.


Once you realize that you have lost your phone, you don’t have to panic trying to remember all the cards you had inside it and trying to find their customer service numbers and so on. Of course, you have all the rights to be unhappy that you lost your expensive phone, but that is a different discussion. You can easily go to [Google Wallet website](https://www.google.com/wallet/) and mark your wallet as lost or stolen with just a couple of clicks. Similarly, you can go to [Apple’s iCloud website](https://www.apple.com/icloud/) and put your phone in Lost mode. In both cases, if and when your phone comes online, it will immediately be placed in Lost mode.


For a moment let’s assume that the fraudster is not as low-tech as we thought and somehow circumvents the `first level` of security (PIN or Touch ID). Now that we have put the phone in lost mode, we have enabled the `second level` of security. In case of [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html), the phone will refuse to make any payment transaction even if they hacked the PIN. In case of [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html), the tokens stored inside the embedded [Secure Element](/2014/09/01/mobile-payments-what-is-a-secure-element.html) will be erased thereby making it impossible to perform a payment transaction even if they have hacked the Touch ID. This `second level` of security makes the wallets doubly secure.


Once you have completed the above simple and straight-forward step, you are pretty much safe. You don’t even have to call your card issuer banks at all. In fact, you can continue to use your payment cards as usual without waiting for a new card to be posted via snail mail. This is pretty cool. But, just in case you want to be triply sure, you can always call your card Issuers in your leisure time and report them lost or stolen. If you do that, your physical cards will be blocked and you may have to wait for your new cards to be issued before making any new payment transaction. It is not necessary to perform this step, but it is always there if you need it.


**Earlier, while discussing the lost mode for these mobile wallets, we blissfully ignored one important scenario. The lost mode can be communicated to your mobile wallet only if your phone is online.** If your phone does not come online, neither Apple nor Google will be able to propagate the lost mode to their respective wallets. What if our high-tech thief makes sure that your phone does not go online after stealing it? Technically, this compromises the `second level` of security. If (a big If) they were also able to hack the `first level` of security (PIN or Touch ID), then it may seem that they are all set to steal our money. Let’s analyze this scenario in the context of [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html) and [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html).


In the case of [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html), the assumption is that, biometric fingerprint authentication is strong enough and cannot be broken. That is the reason why ApplePay does not allow for PIN based authentication of payment transactions because they consider it as technically less secure. In the rarest of scenarios where the fraudster is able to successfully crack the fingerprint auth and also successfully makes sure that the phone cannot be put into lost mode, then there is an open loop hole that can be exploited (unless I am missing something). In this scenario, we always have our last resort (`third level` of security) of locking our physical cards though.


In the case of [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html), we cannot assume the PIN to be as strong as biometric fingerprint authentication. Moreover, it is also possible to configure Google Wallet such that it does not prompt for PIN for a certain time-period. This leaves a hole in security if your device is lost during that time-period. But, Google has one more trick up its sleeve. Unlike ApplePay, where a payment transaction never enters Apple’s servers, Google wallet’s cloud server does come into picture when a payment transaction is conducted. Google has to authorize a transaction in transit. So, technically, even if the fraudster does not allow the phone to go to lost mode and successfully cracks the PIN as well, at the end of the day, the transaction has to pass through Google wallet’s cloud servers. Since we have already placed the wallet in lost mode in the server (although it is not yet propagated to the physical phone), the transaction will be rejected by Google at the server side. The fraudster can do nothing but be shocked after all the hard work he has done trying to steal our money.


In conclusion, for lost/stolen device scenario both [ApplePay](/2014/10/20/mobile-payments-what-is-apple-pay.html) and [Google Wallet](/2014/10/17/mobile-payments-what-is-google-wallet.html) offer multiple layers of security. Some may consider ApplePay’s biometric auth to be more secure, while others will think that Google Wallet’s server side auth is a better strategy. Technically both are sound and revolutionary. We will just have to wait and see which one stands the test of time in the real-world.



<div class="related-reading">
<p class="related-reading-title">Related Reading</p>
<ul>
    <li><a href="http://www.gmarwaha.com/blog/apple-pay-vs-google-wallet/">Apple Pay vs Google Wallet – Article Series</a></li>
    <li><a href="/2014/10/02/apple-pay-vs-google-wallet-the-secure-element.html">Apple Pay vs Google Wallet – Secure Element</a></li>
    <li><a href="http://www.gmarwaha.com/blog/mobile-payments-faq/">Mobile Payments FAQ</a></li>
    <li><a href="/2014/09/24/apple-pay-an-attempt-to-demystify.html">Apple Pay – An attempt to demystify</a></li>
    <li><a href="/2014/10/17/mobile-payments-what-is-google-wallet.html">What is Google Wallet?</a></li>
    <li><a href="/2014/10/20/mobile-payments-what-is-apple-pay.html">What is Apple Pay?</a></li>
</ul>
</div>

