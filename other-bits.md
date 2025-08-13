---
layout: page
title: Other Bits
permalink: /other-bits/
---

<style>
.other-bits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}
.other-bits-item img {
  width: 100%;
  height: auto;
  display: block;
}
.other-bits-item h2 {
  margin: 1rem 0 0.5rem;
  font-size: 1.2rem;
}
.other-bits-item time {
  color: #666;
  font-size: 0.9em;
}
</style>

<div class="other-bits-grid">
{% for post in site.posts %}
  {% if post.category == "other" %}
    <article class="other-bits-item">
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
</div>