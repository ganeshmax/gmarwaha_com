---
layout: post
title: "Heroku – Trouble with Windows and SSH Keys"
date: 2011-05-18 12:00:00 +0000
tags: [Heroku]
original_url: "/2011/05/18/heroku-trouble-with-windows-and-ssh-keys.html"
---

[Heroku](http://www.heroku.com/), one of my favorite cloud platforms, is a hosted platform built specifically for deploying Rails and other Ruby based web applications. Heroku makes deploying Rails applications to cloud ridiculously easy – as long as your source code is under version control with Git. 


The general process of installing and using Heroku on Windows is fairly simple. You should already have Ruby, Rails and Git for Windows ([msysgit](http://code.google.com/p/msysgit/)) installed. Once you have them, go to [Heroku.com](http://www.heroku.com/) and sign up for an account. After signing up, install the Heroku gem with the following command.


```

$ gem install heroku

```


Typically, as in [GitHub ](https://github.com/)you will need to create SSH keys if you haven’t already, and then tell Heroku about your public key so that you can use Git to push your application repository up to their servers. Detailed information for setting up Git and creating ssh keys on Windows can be found [here](http://help.github.com/win-set-up-git/).


```

# Create new keys
$ ssh-keygen -t rsa -C "your_email@yourdomain.com"

# Tell heroku about your public key
$ heroku keys:add

```


Remember? Your source code should be under version control with git. So, from within the root of your application folder, use typical git gimmicks to create a local git repository and commit your application source to the local repository.


```

$ cd my_app
$ git init
$ git add .
$ git commit -m "initial version"

```


Finally, from within the root of your application folder, use the heroku command to create a place on the Heroku servers for the application to live. Then, you can deploy your application to the cloud by pushing your local git repo to heroku…


```

# Create an application space on the server
$ heroku create

# Deploy your application to the cloud
$ git push heroku master

```


If until now everything went well **except for the last step** and instead of getting your application deployed if you got the following error, then it was worth your time to have read this post until this point…


```

Permission denied (publickey).
fatal: The remote end hung up unexpectedly

```


It was a frustrating experience trying to figure out the problem. The keys were created fine and they got added to heroku just fine as well. In fact i could verify it with the following command and my keys were right there.


```

heroku keys:list

```


Whatever I do, I kept getting the same error. Finally after a lot of googling, experimenting and hair plucking the problem got resolved. Here goes the solution…


**Solution:**

Typically once you create the keys as mentioned above, two files  – “id_rsa” and “id_rsa.pub” – are stored in the “.ssh” folder within the user’s home folder. If you are working with linux that seems to be good enough. But for the windows version of git that doesn’t seem to cut it. It wants the keys to be stored inside the “.ssh” folder within the “msysgit” installation folder as well. If you don’t find a “.ssh” folder inside the “msysgit” installation folder, feel free to create one. Once you drop these two key files there and repeat the entire process, everything went as smooth and my application got deployed in the heroku cloud and the world is again a better place to live in.


I am sure many people will hit the same road block. At least I am sure I will come across it again and wouldn’t remember how I solved it in the first place. Happens, doesn’t it? So, I thought i will document it here for future reference. 


If there is any other solution, or if this solution is incorrect, feel free to leave a comment.