---
layout: page
permalink: /publications/
title: Publications
description: <b>This is only a test of jekyll-scholar, not are my publications.<b>
years: [1967, 1956, 1950, 1935, 1905, 2022]
thesis: [Thesis]
nav: true
nav_order: 1
---

<div class="publications">

{%- for y in page.thesis %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f others %} 
{% endfor %}

</div>

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
