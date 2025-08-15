---
layout: base
title: Exhibitions - Pen Plotting Art Shows | Targz
description: Browse exhibitions featuring algorithmic pen plotted artworks. From solo shows to group exhibitions showcasing Op Art and generative art pieces.
keywords: pen plotting exhibitions, op art gallery, generative art shows, algorithmic art exhibition, mathematical art display
permalink: /exhibitions/
image: /assets/images/targz.png
---

<br>
<hgroup style="text-align: center">
  <h2>Exhibitions</h2>
  <p>Some of my last Exhibitions</p>
</hgroup>
<br>
<br>
<br>

<section class="home-grid exhibitions-grid">
    {% for post in site.posts %} {% if post.category == "exhibitions" %}
    <article class="home-item">
        <a href="{{ post.url | relative_url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
            <p>{{ post.title }}{% if post.location %} • {{ post.location }}{% endif %}</p>
        </a>
    </article>
    {% endif %} {% endfor %}
</section>