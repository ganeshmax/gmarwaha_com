---
layout: post
title: "Hibernate never stops surprising me"
date: 2010-02-28 12:00:00 +0000
tags: [Hibernate]
original_url: "/2010/02/28/hibernate-never-stops-surprising-me.html"
---

I have a simple form in my web application where a user can fill in his personal details and address details. *User* specific fields include firstName, middleName and lastName while *Address* specific fields include street, city and zip. On the server side, I have POJOs for *User* and *Address*. Finally I use [Hibernate](http://www.hibernate.org) to map these POJOs to the database.  Since, the *Address* will not be used outside the context of the *User*, I decided to map it as a Component of the *User* class. 


The *User* class and its corresponding mapping is given below:


```

@Entity @Table(name = "user")
public class User {

     @Column(name = "first_name")
     private String firstName;
     
     @Column(name = "middle_name")
     private String middleName;
     
     @Column(name = "last_name")
     private String lastName;
    
     @Embedded
     private Address homeAddress;

     ... Getters and Setters
}

```


The *Address* class is mapped to *User* as a component. You can see the specifics of the mapping below.


```

@Embeddable
public class Address {
     @Column(name = "address_street")
     private String street;
     
     @Column(name = "address_city")
     private String city;
     
     @Column(name = "address_state")
     private String state;

     ... Getters and Setters
}

```


As you may already know, mapping components using hibernate is a very useful feature. This feature and support for nested components and components referring to other entities are the primary source of support for rich and fine grained domain model in hibernate. But while i was using *Component* mapping, I recently stepped on an interesting Feature (or it could be an Issue) and I was happily surprised by it.


Want to know the surprise? Keep reading… 


In this case you map an *Address* as a value type using *@Embedded* annotation in the “homeAddress” field of the *User* class. The *Address* class itself is declared to be *@Emeddable*. This is the standard Hibernate/JPA way to map value types. The Address class has street, city and zip and it gets stored into the same table as the User class’s table. Now, when you insert an instance of *User* into the database, while specifying all null values for *Address*‘s fields maybe because the user didn’t give his address, then what would you expect in return at some point in time when you retrieve this *User* back from the database. 


I for one expected user.getAddress() will return an Address instance. Then address.getStreet() will return null. But that is not what happened. user.getAddress() returned null by itself. That was interesting and even helped me in my case because, if the user hasn’t given any details for his home address, then it probably means that his address itself is not there in the system. So, returning null for getAddress() is semantically the right thing to do. I was surprised and when i checked the hibernate documentation it was even mentioned there that if all properties of a component are null, then the component itself is considered null. 


In another situation this could have been bad, I don’t know, but for my purpose I was happily surprised with this nice touch from hibernate. These kind of small things is what differentiates a great product from a good product. Ain’t it?