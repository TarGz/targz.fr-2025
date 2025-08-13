---
layout: page
title: Pen Plotting
permalink: /pen-plotting/
---

<section class="portfolio-grid">
{% for post in site.posts %}
  {% if post.category == "portfolio" %}
    <article class="portfolio-item">
      {% if post.image %}
        <a href="{{ post.url | relative_url }}">
          <img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
        </a>
      {% endif %}
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <time>{{ post.date | date: "%B %d, %Y" }}</time>
      <p>{{ post.content | strip_html | truncatewords: 20 }}</p>
    </article>
  {% endif %}
{% endfor %}
</section>