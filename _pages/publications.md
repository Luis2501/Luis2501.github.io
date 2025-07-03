---
layout: page
permalink: /publications/
title: Publications
description: All publications listed from newest to oldest
years: [2025]
nav: false
nav_order: 1
---

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
