---
layout: page
title: Exhibitions
permalink: /exhibitions/
---

<style>
.exhibitions-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-top: 2rem;
}

@media (min-width: 768px) {
  .exhibitions-grid {
    grid-template-columns: 1fr 1fr;
  }
}

.exhibition-item {
  margin-bottom: 0;
}

.exhibition-item .image-container {
  position: relative;
  display: inline-block;
  width: 100%;
}

.exhibition-item img {
  width: 100%;
  height: auto;
  display: block;
}

.exhibition-item p {
  position: absolute;
  bottom: 1rem;
  left: 0;
  right: 0;
  margin: 0;
  padding: 1rem;
  font-size: 0.75rem;
  font-weight: normal;
  text-transform: uppercase;
  text-align: center;
  background: transparent;
  color: var(--pico-text-color);
}

.exhibition-item a {
  color: var(--pico-text-color) !important;
  text-decoration: none !important;
}

.exhibition-item a:hover {
  color: var(--pico-text-color) !important;
}
</style>

<section class="exhibitions-grid">
  {% for post in site.posts %}
    {% if post.category == "exhibitions" %}
    <div class="exhibition-item">
      <a href="{{ post.url | relative_url }}">
        <div class="image-container">
          <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" />
          <p>{{ post.title }}</p>
        </div>
      </a>
    </div>
    {% endif %}
  {% endfor %}
</section>