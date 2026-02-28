---
layout: post
title: "Mobile Payments: What is EMV?"
date: 2014-06-25 12:00:00 +0000
tags: [Mobile Payments]
original_url: "/2014/06/25/mobile-payments-what-is-emv.html"
---
#### What is a EMV?


EMV is defined by [EMVCo](http://www.emvco.com/) as, “a global standard for credit and debit payment cards based on [chip card](/2014/04/21/mobile-payments-what-is-a-contact-chip-card.html) technology”. It was named after its original developers – Europay, MasterCard and Visa. EMVCo is the organization that manages, maintains and enhances the EMV specifications.  Today, EMVCo is owned by American Express, Discover, JCB, MasterCard, UnionPay, and Visa. Other organizations from the payments industry also participate as technical and business associates from time to time.


EMV chip cards contain embedded microprocessors that provide strong authentication, security and cryptography features not possible with traditional [magnetic stripe](/2014/04/10/mobile-payments-what-is-a-magnetic-stripe-card.html) cards. In addition to storing payment information in a secure chip rather than a magnetic stripe, using EMV improves the security of a payment transaction by adding 3 important features:


#### Card Authentication:


Card authentication protects the payment system against counterfeit cards. Card authentication methods are defined in the EMV specifications and the associated payment network chip specifications. Card authentication can take place online, offline or both.


#### Cardholder Verification:


Cardholder verification authenticates the cardholder. Use of a PIN is a common cardholder verification method (CVM) that authenticates the cardholder and protects against the use of lost or stolen card. EMV supports Online PIN, Offline PIN, Signature and No CVM as part of its specifications. As mobile payments grow new CVMs, in the form of finger-print, voice and device PIN may also get added to the list


#### Transaction Authorization:


For an online transaction authorization, EMV supports the notion of a dynamic transaction `cryptogram`. The presence of the dynamic component completely eliminates replay style attacks. EMV supports both online authorization and offline authorization based on rules and risk-parameters set by the Issuer


The [Contact chip cards](/2014/04/21/mobile-payments-what-is-a-contact-chip-card.html) and [Contactless chip cards](/2014/05/11/mobile-payments-what-is-a-contactless-chip-card.html) that we discussed in earlier posts can comply to the EMV specification and reap its security advantages. In fact, all of the contact and contactless chip cards in Europe are created using the EMV specification. At present, contact chip cards are in very limited use in US, but the good news is that they are migrating towards it and they are using EMV as the underlying specification.


In contrast, many US banks did offer contactless chip cards over the last few years. These cards did not follow the EMV specification. They instead used a complementary Contactless MSD specification which is an equivalent to regular magenetic stripe data, but a bit more secure. They chose to use MSD because US does not have the EMV infrastructure setup yet. As and when the migration towards EMV matures, these existing contactless MSD cards will also be migrated to Contactless EMV cards or that is what I think.

<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
Welcome to the <a href="/2014/01/24/mobile-payments-faq-and-not-so-faq.html">Mobile payments FAQ and not so FAQ</a> series and you are on FAQ #9. The idea behind this series is to share and learn as much as possible about the field of mobile payments. If you like, you can read all of the FAQs on the <a href="{{ site.baseurl }}/tags/mobile-payments/">Mobile Payments</a> category or by visiting the <a href="/articles/mobile-payments-faq/">Table of contents</a> page.</div>
