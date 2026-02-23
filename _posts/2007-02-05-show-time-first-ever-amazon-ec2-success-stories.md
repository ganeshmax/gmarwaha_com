---
layout: post
title: "Show time! – First ever Amazon EC2 Success Stories"
date: 2007-02-05 12:00:00 +0000
tags: [General]
original_url: "/2007/02/05/show-time-%e2%80%93-first-ever-amazon-ec2-success-stories.html"
---

Amazon, always an innovator, recently unfolded yet another masterpiece to the world in the form of EC2 web-service. [Gumiyo.com](http://www.gumiyo.com), an online mobile-commerce provider and Abaca.com, a spam-blocker solution, are now celebrated as the pioneers to launch a production site using [Amazon EC2](http://www.amazon.com/b/ref=sc_fe_l_2/102-1757361-1220931?ie=UTF8&node=201590011&no=3435361&me=A36L942TSJ2AJA) Service. You can relish the full versions of their [success stories](http://www.amazon.com/Success-Stories-AWS-home-page/b/ref=sc_fe_l_1/102-1757361-1220931?ie=UTF8&amp;amp;amp;node=182241011&no=3435361&me=A36L942TSJ2AJA) [here](http://www.amazon.com/gp/browse.html?node=325814011) and [here](http://www.amazon.com/gp/browse.html?node=325813011).


[EC2 (Elastic compute cloud)](http://www.amazon.com/b/ref=sc_fe_l_2/102-1757361-1220931?ie=UTF8&node=201590011&no=3435361&me=A36L942TSJ2AJA) – the name doesn’t tell much, or does it? For those who are not familiar, EC2 is a dynamically scalable data-center kind of service. It is not a REST/SOAP style web-service that we have come to conventionally recognize. We do not fire a call, and expect a response. Instead, we get access to virtual servers equivalent of Intel Xeon 1.7 GHz, 1.75 GB of RAM, 250 MB/S of network bandwidth and 160 GB of local hard drive space. Any number of such servers are at our disposal in just a matter of minutes, and that my friends, is not just innovative, but a killer idea in the data-center services arena. At 10 cents per hour of instance up-time, this service is something any start-up, if not individuals, should seriously consider. An EC2 account implicitly comes with a S3 account. Of course you can sign-up for S3 separately as well. In case you are wondering what S3 is, keep reading…


[S3 (Simple Storage Service)](http://www.amazon.com/S3-AWS-home-page-Money/b/ref=sc_fe_l_2/102-1757361-1220931?ie=UTF8&node=16427261&no=3435361&me=A36L942TSJ2AJA) is, well, a simple storage service that can be used to store and retrieve huge volumes of data over the internet. This  offering has a similar accent to traditional web-services. The infamous REST and SOAP interfaces are provided for campers at both ends of the web-services campground. The value-add I see in this service is Simplicity, Cost effectiveness and more importantly, the trust that we already have over Amazon’s infrastructure. After all, they are one of the very few survivors of the DotCom boom. At 15 cents for a GB of storage per month and 20 cents for a GB of data transfer, S3 is something that i would use for all my back-up needs. Being a java programmer, I use the [JetS3T](https://jets3t.dev.java.net/) library from Java.net and see how easy it gets…


```

// Sample code that uploads a file to S3. 
String access = "YOUR_AWS_ACCESS_KEY"; 
String secret = "YOUR_AWS_SECRET_KEY";
AWSCredentials cred = new AWSCredentials(access, secret);

// I used Rest, you could use Soap
S3Service s3 = new RestS3Service(cred);

// Buckets are like folders, but globally unique
S3Bucket bucket = s3.createBucket(access + ".Test");

// File that you want to upload
File file = new File("SomeFile.txt");

// Upload your file
S3Object s3Object = new S3Object(fileData);
object = s3.putObject(bucket, file);
```


Start-ups, small businesses and web 2.0 companies should regard these services as “God-Sent”. Well, I guess, I am not wrong. Two startups have already considered it serious enough to launch their production environment on EC2. And I’m sure there are more to come. Lets see what they are up to.


[Gumiyo.com](http://www.gumiyo.com) is the first end-to-end mobile commerce platform, connecting live buyers and live sellers through mobile phones and through the Web. Using any mobile phone with a built-in camera and a basic data plan you can create ads in 3 easy steps


1. Capture images or video of an item

2. Attach them to a multimedia message with a short description

3. Send it to post [AT] gumiyo [DOT] com


Gumiyo will create an online ad for you and then send you a reply link asking you to review and edit your ad before it is posted. You don’t need to use a mobile phone though. You can login and place your ad any time on the Web. You can even send them your ad as an email with photo or video attachments. Could it get any easier? Check it out for yourself.


Abaca.com is a spam-blocker appliance that you can purchase for under $2000. This email protection gateway offers 99% guaranteed filtration with zero management. At present, I don’t have a need for such an appliance as an individual. So, I didn’t try it out myself.


Will more and more businesses build around these services? Will traditional data-center providers offer EC2 as an option with GUI based configuration? Will amazon create more like these? What do you think?