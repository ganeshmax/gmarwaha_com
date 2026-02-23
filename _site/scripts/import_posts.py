#!/usr/bin/env python3
"""
Import blog posts from gmarwaha.com into Jekyll _posts format.
Fetches content from the live site and saves as markdown files.
"""

import os
import re
import time
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from datetime import datetime

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')
os.makedirs(POSTS_DIR, exist_ok=True)

POST_URLS = [
    ("2015-01-03", "Apple Pay – An attempt to demystify – Take 2", "https://www.gmarwaha.com/blog/2015/01/03/apple-pay-an-attempt-to-demystify-take-2/"),
    ("2014-10-28", "Apple Pay vs Google Wallet : Lost and Stolen Scenario", "https://www.gmarwaha.com/blog/2014/10/28/apple-pay-vs-google-wallet-lost-and-stolen-scenario/"),
    ("2014-10-20", "Mobile Payments: What is Apple Pay?", "https://www.gmarwaha.com/blog/2014/10/20/mobile-payments-what-is-apple-pay/"),
    ("2014-10-17", "Mobile Payments: What is Google Wallet?", "https://www.gmarwaha.com/blog/2014/10/17/mobile-payments-what-is-google-wallet/"),
    ("2014-10-09", "jCarouselLite version 1.1 released !", "https://www.gmarwaha.com/blog/2014/10/09/jcarousellite-version-1-1-released/"),
    ("2014-10-02", "Apple Pay vs Google Wallet : The Secure Element", "https://www.gmarwaha.com/blog/2014/10/02/apple-pay-vs-google-wallet-the-secure-element/"),
    ("2014-09-24", "Apple Pay – An attempt to demystify", "https://www.gmarwaha.com/blog/2014/09/24/apple-pay-an-attempt-to-demystify/"),
    ("2014-09-20", "Mobile Payments: What is HCE?", "https://www.gmarwaha.com/blog/2014/09/20/mobile-payments-what-is-hce/"),
    ("2014-09-01", "Mobile Payments: What is a Secure Element?", "https://www.gmarwaha.com/blog/2014/09/01/mobile-payments-what-is-a-secure-element/"),
    ("2014-08-07", "Mobile Payments: What is NFC Card Emulation Mode?", "https://www.gmarwaha.com/blog/2014/08/07/mobile-payments-what-is-nfc-card-emulation-mode/"),
    ("2014-08-03", "Mobile Payments: What is NFC?", "https://www.gmarwaha.com/blog/2014/08/03/mobile-payments-what-is-nfc/"),
    ("2014-07-16", "Mobile Payments: What is a Mobile Wallet?", "https://www.gmarwaha.com/blog/2014/07/16/mobile-payments-what-is-a-mobile-wallet/"),
    ("2014-07-06", "Mobile Payments: What is Mobile Payment?", "https://www.gmarwaha.com/blog/2014/07/06/mobile-payments-what-is-mobile-payment/"),
    ("2014-06-25", "Mobile Payments: What is EMV?", "https://www.gmarwaha.com/blog/2014/06/25/mobile-payments-what-is-emv/"),
    ("2014-05-12", "Bring Your Own Wallet", "https://www.gmarwaha.com/blog/2014/05/12/bring-your-own-wallet/"),
    ("2014-05-11", "Mobile Payments: What is Tap & Pay?", "https://www.gmarwaha.com/blog/2014/05/11/mobile-payments-what-is-tap-pay/"),
    ("2014-05-11", "Mobile Payments: What is a Contactless Chip Card?", "https://www.gmarwaha.com/blog/2014/05/11/mobile-payments-what-is-a-contactless-chip-card/"),
    ("2014-04-21", "Mobile Payments: What is a Contact Chip Card?", "https://www.gmarwaha.com/blog/2014/04/21/mobile-payments-what-is-a-contact-chip-card/"),
    ("2014-04-10", "Mobile Payments: What is a Magnetic Stripe Card?", "https://www.gmarwaha.com/blog/2014/04/10/mobile-payments-what-is-a-magnetic-stripe-card/"),
    ("2014-03-21", "Mobile Payments: Who is a Payment Network?", "https://www.gmarwaha.com/blog/2014/03/21/mobile-payments-who-is-a-payment-network/"),
    ("2014-03-07", "Mobile Payments: Who is a Merchant?", "https://www.gmarwaha.com/blog/2014/03/07/mobile-payments-who-is-a-merchant/"),
    ("2014-02-12", "Mobile Payments: Who is an Acquirer?", "https://www.gmarwaha.com/blog/2014/02/12/mobile-payments-who-is-an-acquirer/"),
    ("2014-02-05", "Mobile Payments: Who is an Issuer?", "https://www.gmarwaha.com/blog/2014/02/05/mobile-payments-who-is-an-issuer/"),
    ("2014-01-24", "Mobile Payments: FAQ and not so FAQ", "https://www.gmarwaha.com/blog/2014/01/24/mobile-payments-faq-and-not-so-faq/"),
    ("2012-03-22", "SQLite Auto Increment", "https://www.gmarwaha.com/blog/2012/03/22/sqlite-auto-increment/"),
    ("2012-01-18", "Android: Remove activity from history stack", "https://www.gmarwaha.com/blog/2012/01/18/android-remove-activity-from-history-stack/"),
    ("2012-01-16", "Tomcat & IntelliJ – Deploy war files outside webapps folder", "https://www.gmarwaha.com/blog/2012/01/16/tomcat-intellij-deploy-war-files-outside-webapps-folder/"),
    ("2011-12-08", "No hadoop-env.sh in Hadoop 0.23", "https://www.gmarwaha.com/blog/2011/12/08/no-hadoop-env-sh-in-hadoop-0-23/"),
    ("2011-09-30", "jQuery UI: Calling widget methods directly", "https://www.gmarwaha.com/blog/2011/09/30/jquery-ui-calling-widget-methods-directly/"),
    ("2011-08-17", "JQuery: Wait for multiple animations to Complete – Take 2", "https://www.gmarwaha.com/blog/2011/08/17/jquery-wait-for-multiple-animations-to-complete-take-2/"),
    ("2011-07-15", "Blackberry: Code signing for Tablet and Smartphone", "https://www.gmarwaha.com/blog/2011/07/15/blackberry-code-signing-for-tablet-and-smartphone/"),
    ("2011-06-16", "Blackberry – Issue with Installing to a device using Javaloader", "https://www.gmarwaha.com/blog/2011/06/16/blackberry-issue-with-installing-to-a-device-using-javaloader/"),
    ("2011-06-03", "Install Blackberry SDK 6.0 to your existing Eclipse Helios", "https://www.gmarwaha.com/blog/2011/06/03/install-blackberry-sdk-6-0-to-your-existing-eclipse-helios/"),
    ("2011-05-18", "Heroku – Trouble with Windows and SSH Keys", "https://www.gmarwaha.com/blog/2011/05/18/heroku-trouble-with-windows-and-ssh-keys/"),
    ("2011-05-09", "GWT – Pros and Cons", "https://www.gmarwaha.com/blog/2011/05/09/gwt-pros-and-cons/"),
    ("2011-05-04", "GWT – Not enough methods, expecting 3 saw 2", "https://www.gmarwaha.com/blog/2011/05/04/gwt-not-enough-methods-expecting-3-saw-2/"),
    ("2011-04-22", "Shelfari is Down – Wants me to finish my next book", "https://www.gmarwaha.com/blog/2011/04/22/shelfari-is-down-wants-me-to-finish-my-next-book/"),
    ("2011-04-18", "Ceylon – Yet Another JVM Language (YAJL)", "https://www.gmarwaha.com/blog/2011/04/18/ceylon-yet-another-jvm-language-yajl/"),
    ("2011-04-11", "Twitter moves from Rails to Java", "https://www.gmarwaha.com/blog/2011/04/11/twitter-moves-from-rails-to-java/"),
    ("2011-03-30", "Android: List View alternating between 1px and 2px dividers", "https://www.gmarwaha.com/blog/2011/03/30/android-list-view-alternating-between-1px-and-2px-dividers/"),
    ("2011-02-28", "iPhone SDK – Initial Thoughts", "https://www.gmarwaha.com/blog/2011/02/28/iphone-sdk-initial-thoughts/"),
    ("2011-01-11", "Intellij IDEA key map for Eclipse", "https://www.gmarwaha.com/blog/2011/01/11/eclipse-use-intellij-idea-key-map/"),
    ("2010-12-25", "Android: My HTC Desire", "https://www.gmarwaha.com/blog/2010/12/25/android-my-htc-desire/"),
    ("2010-05-10", "Tomcat 5.5 and above doesn't need the JDK", "https://www.gmarwaha.com/blog/2010/05/10/tomcat-5-5-and-above-doesnt-need-the-jdk/"),
    ("2010-04-21", "Groovy: List Operations", "https://www.gmarwaha.com/blog/2010/04/21/groovy-list-operations/"),
    ("2010-03-12", "Groovy: No-arg constructor is always there", "https://www.gmarwaha.com/blog/2010/03/12/groovy-no-arg-constructor-is-always-there/"),
    ("2010-02-28", "Hibernate never stops surprising me", "https://www.gmarwaha.com/blog/2010/02/28/hibernate-never-stops-surprising-me/"),
    ("2010-01-02", "Final Modifier for method arguments. What do you think?", "https://www.gmarwaha.com/blog/2010/01/02/final-modifier-for-method-arguments-what-do-you-think/"),
    ("2009-08-26", "Hibernate: Why should I Force Discriminator?", "https://www.gmarwaha.com/blog/2009/08/26/hibernate-why-should-i-force-discriminator/"),
    ("2009-08-02", "Happy Friendship Day!", "https://www.gmarwaha.com/blog/2009/08/02/happy-friendship-day/"),
    ("2009-06-27", "Is it an AJAX Request or a Normal Request?", "https://www.gmarwaha.com/blog/2009/06/27/is-it-an-ajax-request-or-a-normal-request/"),
    ("2009-06-16", "Ctrl + Key Combination – Simple Jquery Plugin", "https://www.gmarwaha.com/blog/2009/06/16/ctrl-key-combination-simple-jquery-plugin/"),
    ("2009-06-09", "JQuery: Waiting for Multiple Animations to Complete", "https://www.gmarwaha.com/blog/2009/06/09/jquery-waiting-for-multiple-animations-to-complete/"),
    ("2009-05-30", "Where did the Brilliant Indian Minds Go?", "https://www.gmarwaha.com/blog/2009/05/30/where-did-the-brilliant-indian-minds-go/"),
    ("2009-05-23", "Toon: When Sensex plunged …", "https://www.gmarwaha.com/blog/2009/05/23/toon-when-sensex-plunged/"),
    ("2009-05-23", "Ganesh and God – Keat's Toons", "https://www.gmarwaha.com/blog/2009/05/23/ganesh-and-god-keats-toondoos/"),
    ("2009-02-02", "Groovy: Private is not private", "https://www.gmarwaha.com/blog/2009/02/02/groovy-private-is-not-private/"),
    ("2008-12-30", "Groovy – Syntax sugar for map keys", "https://www.gmarwaha.com/blog/2008/12/30/groovy-syntax-sugar-for-map-keys/"),
    ("2008-11-22", "Groovy – Add Static & Instance methods dynamically", "https://www.gmarwaha.com/blog/2008/11/22/groovy-%e2%80%93-add-static-instance-methods-dynamically/"),
    ("2008-07-04", "The Nboomi Experience", "https://www.gmarwaha.com/blog/2008/07/04/the-nboomi-experience/"),
    ("2008-01-09", "Groovy – Java keyword as a method name", "https://www.gmarwaha.com/blog/2008/01/09/groovy-%e2%80%93-java-keyword-as-a-method-name/"),
    ("2007-08-23", "LavaLamp for jQuery lovers!", "https://www.gmarwaha.com/blog/2007/08/23/lavalamp-for-jquery-lovers/"),
    ("2007-08-09", "jCarousel Lite – A jQuery plugin", "https://www.gmarwaha.com/blog/2007/08/09/jcarousel-lite-a-jquery-plugin/"),
    ("2007-02-05", "Show time! – First ever Amazon EC2 Success Stories", "https://www.gmarwaha.com/blog/2007/02/05/show-time-%e2%80%93-first-ever-amazon-ec2-success-stories/"),
    ("2007-01-16", "Hibernate – Difference between session's get() and load()", "https://www.gmarwaha.com/blog/2007/01/16/hibernate-difference-between-sessions-get-and-load/"),
    ("2006-10-05", "A journey of a thousand miles begins with one step.", "https://www.gmarwaha.com/blog/2006/10/05/a-journey-of-a-thousand-miles-begins-with-one-step-well-here-goes-my-first-step/"),
]

# Tags derived from URL paths / titles
def guess_tags(url, title):
    tags = []
    url_lower = url.lower()
    title_lower = title.lower()
    if 'jquery' in url_lower or 'jquery' in title_lower: tags.append('jQuery')
    if 'groovy' in url_lower or 'groovy' in title_lower: tags.append('Groovy')
    if 'android' in url_lower or 'android' in title_lower: tags.append('Android')
    if 'hibernate' in url_lower or 'hibernate' in title_lower: tags.append('Hibernate')
    if 'mobile-payment' in url_lower or 'mobile payment' in title_lower: tags.append('Mobile Payments')
    if 'apple-pay' in url_lower or 'apple pay' in title_lower: tags.append('Apple Pay')
    if 'google-wallet' in url_lower or 'google wallet' in title_lower: tags.append('Google Wallet')
    if 'nfc' in url_lower or 'nfc' in title_lower: tags.append('NFC')
    if 'gwt' in url_lower or 'gwt' in title_lower: tags.append('GWT')
    if 'blackberry' in url_lower or 'blackberry' in title_lower: tags.append('Blackberry')
    if 'tomcat' in url_lower or 'tomcat' in title_lower: tags.append('Tomcat')
    if 'jcarousel' in url_lower or 'jcarousel' in title_lower: tags.append('jCarouselLite')
    if 'lavalamp' in url_lower or 'lavalamp' in title_lower: tags.append('jQuery')
    if 'sqlite' in url_lower: tags.append('SQLite')
    if 'hadoop' in url_lower: tags.append('Hadoop')
    if 'heroku' in url_lower: tags.append('Heroku')
    if 'iphone' in url_lower or 'iphone' in title_lower: tags.append('iPhone')
    if not tags:
        tags.append('General')
    return tags

def slugify(title):
    # Create a URL-safe slug from the title
    s = title.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s[:60]  # keep it reasonable length

def fetch_post_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


# Simple but functional HTML-to-text converter preserving code blocks
class ContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_entry_content = False
        self.depth = 0
        self.target_depth = 0
        self.content_parts = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
        self.skip_depth = 0
        self.current_tag = None
        self.in_code = False
        self.in_pre = False
        self.in_heading = None
        self.in_link = False
        self.link_href = ''
        self.in_skip = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '')
        
        if tag in self.skip_tags:
            self.skip_depth += 1
            return

        if self.skip_depth > 0:
            return

        # Detect entry content div
        if tag == 'div' and any(c in classes for c in ['entry-content', 'post-content', 'entry', 'post-entry']):
            self.in_entry_content = True
            self.depth = 1

        if self.in_entry_content:
            if tag == 'div':
                self.depth += 1
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                self.in_heading = tag
            if tag == 'pre':
                self.in_pre = True
                self.content_parts.append('\n```\n')
            if tag == 'code' and not self.in_pre:
                self.in_code = True
                self.content_parts.append('`')
            if tag == 'a' and 'href' in attrs_dict:
                self.in_link = True
                self.link_href = attrs_dict['href']
                self.content_parts.append('[')
            if tag == 'p':
                self.content_parts.append('\n\n')
            if tag == 'br':
                self.content_parts.append('\n')
            if tag == 'li':
                self.content_parts.append('\n- ')
            if tag in ('ul', 'ol'):
                self.content_parts.append('\n')
            if tag == 'blockquote':
                self.content_parts.append('\n> ')
            if tag == 'strong' or tag == 'b':
                self.content_parts.append('**')
            if tag == 'em' or tag == 'i':
                self.content_parts.append('*')
            if tag == 'img':
                src = attrs_dict.get('src', '')
                alt = attrs_dict.get('alt', 'image')
                if src:
                    self.content_parts.append(f'\n![{alt}]({src})\n')

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth > 0:
            return

        if self.in_entry_content:
            if tag == 'div':
                self.depth -= 1
                if self.depth <= 0:
                    self.in_entry_content = False
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                self.in_heading = None
                self.content_parts.append('\n\n')
            if tag == 'pre':
                self.in_pre = False
                self.content_parts.append('\n```\n')
            if tag == 'code' and not self.in_pre:
                self.in_code = False
                self.content_parts.append('`')
            if tag == 'a' and self.in_link:
                self.in_link = False
                self.content_parts.append(f']({self.link_href})')
                self.link_href = ''
            if tag == 'p':
                self.content_parts.append('\n')
            if tag in ('strong', 'b'):
                self.content_parts.append('**')
            if tag in ('em', 'i'):
                self.content_parts.append('*')

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        if not self.in_entry_content:
            return
        text = data
        if self.in_heading:
            level = int(self.in_heading[1])
            prefix = '#' * level + ' '
            self.content_parts.append(f'\n{prefix}{text.strip()}')
        else:
            self.content_parts.append(text)

    def get_content(self):
        raw = ''.join(self.content_parts)
        # Clean up excessive blank lines
        raw = re.sub(r'\n{4,}', '\n\n\n', raw)
        return raw.strip()


def html_to_content(html):
    parser = ContentExtractor()
    parser.feed(html)
    content = parser.get_content()
    if not content:
        # Fallback: if no entry-content found, just strip all HTML
        content = re.sub(r'<[^>]+>', ' ', html)
        content = re.sub(r'\s+', ' ', content).strip()
        content = content[:2000] + '...' if len(content) > 2000 else content
    return content


def title_to_safe(title):
    """Make title safe for YAML front matter (escape quotes)."""
    return title.replace('"', '\\"').replace("'", "''")


def main():
    failed = []
    succeeded = []

    for i, (date, title, url) in enumerate(POST_URLS):
        slug = slugify(title)
        filename = f"{date}-{slug}.md"
        filepath = os.path.join(POSTS_DIR, filename)

        # Skip if already exists
        if os.path.exists(filepath):
            print(f"[{i+1}/{len(POST_URLS)}] SKIP (exists): {filename}")
            succeeded.append((date, title, filename))
            continue

        print(f"[{i+1}/{len(POST_URLS)}] Fetching: {url}")
        html = fetch_post_html(url)

        if not html:
            failed.append((date, title, url))
            # Write stub post
            html = ''

        content = html_to_content(html) if html else f"*Content could not be fetched. [View original post]({url})*"

        tags = guess_tags(url, title)
        tags_yaml = ', '.join(tags)
        safe_title = title_to_safe(title)

        front_matter = f"""---
layout: post
title: "{safe_title}"
date: {date} 12:00:00 +0000
tags: [{tags_yaml}]
original_url: "{url}"
---
"""
        full_content = front_matter + '\n' + content

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"  -> Saved: {filename} ({len(content)} chars)")
        succeeded.append((date, title, filename))

        # Be polite — small delay between requests
        time.sleep(0.5)

    print(f"\n=== DONE ===")
    print(f"Saved: {len(succeeded)} posts")
    print(f"Failed: {len(failed)} posts")
    if failed:
        print("Failed posts:")
        for d, t, u in failed:
            print(f"  {d} - {t}: {u}")


if __name__ == '__main__':
    main()
