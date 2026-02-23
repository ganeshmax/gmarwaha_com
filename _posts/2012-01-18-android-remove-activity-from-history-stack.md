---
layout: post
title: "Android: Remove activity from history stack"
date: 2012-01-18 12:00:00 +0000
tags: [Android]
original_url: "/2012/01/18/android-remove-activity-from-history-stack.html"
---

In most Android REST-Client applications, the first screen a user sees is either a Login or Registration screen. Once the user logs in, the user is generally taken to a Dashboard screen or to some other Home screen. Now, What do you think will happen if the user presses the back button? Won’t they be taken back to the Login Screen? That is not good design, Is it? The issue is no different even when we show a Blank/Splash screen while automatically logging the user in based on their saved credentials. In fact in the second case it is worse. The user gets to see a Blank screen when they press the back button.


To avoid this behavior, we have to tell android to remove the Login screen from the display/history stack once its job is complete. There are a variety of ways to do this. The easiest way is to give the LoginActivity a “android:noHistory = true” attribute in the manifest file. That instructs Android to remove the given activity from the history stack thereby avoiding the aforementioned behavior altogether.


```

<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.example.activity"
          android:versionCode="1"
          android:versionName="1.0">

  <application android:name="MyApp" android:label="My Application">

    <activity android:name=".LoginActivity" android:noHistory="true">
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>

  </application>
</manifest>

```


In other similar circumstances, we may want a similar but dynamic behavior where we would like to choose at runtime, if an activity should be removed from the history stack or not. In those cases we can use Intent.FLAG_ACTIVITY_NO_HISTORY intent flag to achieve the same feature dynamically.


There is a cornucopia of other Intent flags [available and documented here](http://developer.android.com/reference/android/content/Intent.html) for our usage pleasure. They may render themselves useful under other circumstances. Have fun learning them all…