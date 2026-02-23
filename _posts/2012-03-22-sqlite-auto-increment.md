---
layout: post
title: "SQLite Auto Increment"
date: 2012-03-22 12:00:00 +0000
tags: [SQLite]
original_url: "/2012/03/22/sqlite-auto-increment.html"
---

In SQLite, the primary key column get auto-incremented by default. So, my thought was that there was no necessity to set the `autoincrement` flag explicitly in the `create table` DDL. Then I discovered a hard truth. When I don’t set the `autoincrement` flag explicitly, it does auto-increment, but there is a minor issue. It so happens that SQLite has two algorithms to perform auto-increment in primary keys – a default one where you don’t explicitly set the flag and an other one where you explicitly set the flag.


To understand the glitch, let’s consider an example. Assume that you have a table with 5 rows with `IDs` 1, 2, 3, 4 and 5. The default algorithm increments the highest value in the `ID` column by 1. If you add a new row to this table, it automatically gets an `ID` of 6. Now, let’s delete the row with `ID #6`. You are left in the same state you started – 5 rows with `IDs` 1, 2, 3, 4 and 5. Let’s add a new row once again. **This new row again gets an ID of 6**.


This may have disastrous consequences or no consequences at all depending on your scenario. Generally, the autoincrement behavior that is expected out of a database is not this. I would expect the last row to get an ID of 7 instead since the PK column will not be reused. That brings us to the other algorithm. If I explicitly set the `autoincrement` flag in the `create table` DDL, the row that was added last correctly gets an ID of 7 instead of 6. This behavior is consistent with other databases. Not a big issue at all depending on your scenario. But, just be warned.