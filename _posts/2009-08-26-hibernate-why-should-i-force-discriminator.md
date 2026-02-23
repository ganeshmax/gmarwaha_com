---
layout: post
title: "Hibernate: Why should I Force Discriminator?"
date: 2009-08-26 12:00:00 +0000
tags: [Hibernate]
original_url: "/2009/08/26/hibernate-why-should-i-force-discriminator.html"
---

Hibernate is an ambitious project that aims to be a complete solution to the problem of managing persistent data in java. Even with such an arduous task before them, the hibernate team tries very hard to expose a simple API for developers like us. Still, the complexity behind the API shows its ugly face time and again and I believe it is unavoidable as long as the mismatch between Object and Relational world exists.


That said, although I have worked with hibernate for many years and have been its advocate in all my organizations, I keep facing newer issues and keep finding newer ways to work with it efficiently and effectively. Recently, when I was working for [nboomi.com](http://www.nboomi.com), I faced an issue when mapping a *OneToMany* relationship to the sub-classes of *“Single Table Inheritance”* strategy. After a frustrating couple of hours of debugging I finally landed on the correct solution. So, I thought other developers who will travel this path could get benefited and started writing this blog post.


Let me explain the issue I faced with an example. Assume you have a normal *User* Entity with the typical *id*, *version* and *loginId* properties. Assume this *User* can have many *AboutUs* sections and many *Service* sections. You don’t need to be an architect to model them as *OneToMany* relationships from *User*. So, I modelled *UserAboutSection* and *UserServiceSection* entities and created a *OneToMany* relationship between *User* and these entities. Looking at the commonality between these two, I decided to factor out the common fields into a superclass called *UserSection*. Now, both *UserAboutSection* and *UserServiceSection* extends *UserSection*. I chose to map this Inheritance hierarchy using “Single Table Inheritance” strategy to keep it simple and since most of the fields were common and only a few were specific. 


The *User* entity is given below. Notice the *List<UserAboutSection>* and a *List<UserServiceSection>* mapped using *OneToMany* relationship.


The getters, setters, adders, imports and static imports are omitted for brevity.


```

@Entity @Table(name = "user")
public class User extends BaseEntity {

    @Column(name = "login_id")
    private String loginId;

    @Column(name = "password")
    private String password;

    ...

    @OneToMany(cascade = {CascadeType.ALL})
    @JoinColumn(name = "user_id", nullable = false)
    @IndexColumn(name = "user_section_position")
    List<UserAboutSection> aboutUs;

    @OneToMany(cascade = {CascadeType.ALL})
    @JoinColumn(name = "user_id", nullable = false)
    @IndexColumn(name = "user_section_position")
    List<UserServiceSection> services;

    ... Getters, Setters and Adders
}

```


Here goes the *UserSection* entity that acts as the base class in this “Single Table Inheritance” strategy. Hibernate uses the @DiscriminatorColumn annotation to distinguish between sub-classes. 


```

@Entity @Table(name = "user_section")
@Inheritance(strategy= InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name="user_section_type", discriminatorType = STRING) 
public class UserSection extends BaseEntity {
    
    @Column(name = "title")         
    protected String title;

    @Column(name = "description")   
    protected String description;

    ... Getters and Setters
}

```


Here goes the *UserAboutSection* entity that derives from the *UserSection* entity. Hibernate uses the @DiscriminatorValue annotation to decide if a row in the database belongs to an instance of this class.


```

@Entity @DiscriminatorValue("ABOUT")
public class UserAboutSection extends UserSection {
    @ManyToOne 
    @JoinColumn(name="user_id",updatable=false,insertable=false,nullable=false)
    protected User user;

    ... Other Properties specific to UserAboutSection
}

```


Here goes the *UserServiceSection* entity that derives from the *UserSection* entity. Hibernate uses the @DiscriminatorValue annotation to decide if a row in the database belongs to an instance of this class.


```

@Entity @DiscriminatorValue("SERVICE")
public class UserServiceSection extends UserSection {
    @ManyToOne 
    @JoinColumn(name="user_id",updatable=false,insertable=false,nullable=false)
    protected User user;

    ... Other Properties specific to UserServiceSection
}

```


Pretty straightforward… huh! When you try to retrieve an instance of *User* along with its *aboutUs* and *services* collections eagerly (or lazily – doesn’t matter), what do you expect? 


I expected an instance of *User* with the *aboutUs* collection filled with only *UserAboutSection* instances and the *services* collection filled with only *UserServiceSection* instances corresponding to only the rows they represent in the database. And I believe this expectation is valid, because that is what the mapping looks like and hibernate also has all the information it needs to make this work. 


But I got something different. Both the *aboutUs* and *services* collections had all the *UserSection* rows that belong to this *User*. I mean, *aboutUs* collection had all the *UserSection* instances including U*serAboutSection* and *UserServiceSection* instances. This was surprising because hibernate has all the information it needs to populate the right instances. 


After quite a bit of debugging, googling and RTFM-ing I landed upon *@ForceDiscriminator* annotation. This annotation has to be applied to the base class in the Inheritance hierarchy for “Single Table Inheritance” strategy. In my case, I had to apply it to *UserSection* entity. The *UserSection* entity after applying this annotation is given below… 


```

@Entity @Table(name = "user_section")
@Inheritance(strategy= InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name="user_section_type", discriminatorType = STRING) 
@ForceDiscriminator
public class UserSection extends BaseEntity {
    
    @Column(name = "title")         
    protected String title;

    @Column(name = "description")   
    protected String description;

    ... Getters and Setters
}

```


Once I ask hibernate to Force Discriminiator, it is happy and populates the aboutUs and services collections with its respective instances. 


Ok, Problem Solved! But why did I have to tell hibernate to Force Discriminator. Shouldn’t that be the default behaviour. Is it a bug in hibernate or is it a feature? Am I missing something? If any one of you hibernate fans have walked this path and know the answer, please feel free to drop in a comment. I sincerely hope this post will be a valuable time-saver for other hibernate developers who step on this Bug/Feature.