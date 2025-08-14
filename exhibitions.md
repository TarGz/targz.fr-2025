---
layout: base
title: Exhibitions - Pen Plotting Art Shows | Targz
description: Browse exhibitions featuring algorithmic pen plotted artworks. From solo shows to group exhibitions showcasing Op Art and generative art pieces.
keywords: pen plotting exhibitions, op art gallery, generative art shows, algorithmic art exhibition, mathematical art display
permalink: /exhibitions/
image: /assets/images/targz.png
---

Exhibitions I’ve taken part in, across different places and mediums.

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