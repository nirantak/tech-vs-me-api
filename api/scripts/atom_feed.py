from typing import Dict, List

import feedparser

from api.models import Authors, Posts


def get_feed(FEED_URL: str) -> int:
    """Parse Atom Feed to get all posts"""
    data = []

    r = feedparser.parse(FEED_URL)
    for article in r.entries:
        a = {}
        a["title"] = article.title
        a["url"] = article.link
        a["author"] = article.author
        a["category"] = ", ".join([i.term for i in article.tags])
        a["summary"] = article.content[1].value
        a["published"] = article.published
        a["updated"] = article.updated
        data.append(a)

    count = update(data)
    return count


def update(data: List[Dict]) -> int:
    """Update database with new posts from feed"""
    posts = Posts.objects.all()
    count = 0

    for article in data:
        if article["url"] not in [i.url for i in posts]:
            post = Posts(
                title=article["title"],
                url=article["url"],
                author=article["author"],
                category=article["category"],
                summary=article["summary"],
                published=article["published"],
                updated=article["updated"],
            )
            post.save()
            count += 1

            author = Authors.objects.filter(name=article["author"])
            if author:
                author = author[0]
                author.posts = f"{author.posts}, {post.id}"
                author.save()
            else:
                author = Authors(
                    username=".".join(article["author"].split()).lower(),
                    name=article["author"],
                    social=f"https://twitter.com/{article['author'].replace(' ','')}",
                    posts=post.id,
                )
                author.save()

    return count
