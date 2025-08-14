---
layout: base
title: Bits - Digital Art & Experiments | Targz
description: Explore digital artworks, experimental projects, and creative coding beyond pen plotting. A collection of diverse creative explorations.
keywords: digital art, experimental art, creative coding, generative design, typography, LEGO art
permalink: /bits/
image: /assets/images/targz.png
---


<hgroup style="text-align: center">
  <h2>Bits & Experiments</h2>
  <p><small>A selection of my other work, from Lego<br/> to digital projects and NFT series.</small></p>
</hgroup>

<section class="home-grid bits-grid">
    {% for post in site.posts %} {% if post.category == "bits" %}
    <article class="home-item">
        <a href="{{ post.url | relative_url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
            <p>{{ post.title }}</p>
        </a>
    </article>
    {% endif %} {% endfor %}
</section>