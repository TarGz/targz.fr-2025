---
layout: base
title: Exhibitions
permalink: /exhibitions/
---



<section class="home-grid exhibitions-grid">
    {% for post in site.posts %} {% if post.category == "exhibitions" %}
    <article class="home-item">
        <a href="{{ post.url | relative_url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
            <p>{{ post.title }}</p>
        </a>
    </article>
    {% endif %} {% endfor %}
</section>