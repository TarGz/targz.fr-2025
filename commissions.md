---
layout: base
title: Commissions - Custom Pen Plotting Art | Targz
description: Browse commissioned pen plotted artworks. Custom algorithmic art pieces created for clients, showcasing personalized Op Art and generative designs.
keywords: pen plotting commissions, custom algorithmic art, commissioned generative art, bespoke op art, personalized pen plotting
permalink: /commissions/
image: /assets/images/targz.png
---
<br/>
<hgroup style="text-align: center">
  <h2>Commissions</h2>
  <p><small>A selection of my last pen plotter commissions</small></p>
</hgroup>
<br/>
<br/>
<br/>

<section class="home-grid commissions-grid">
    {% for post in site.posts %} {% if post.category == "commissions" %}
    <article class="home-item">
        <a href="{{ post.url | relative_url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
            <p>{{ post.title }}</p>
        </a>
    </article>
    {% endif %} {% endfor %}
</section>