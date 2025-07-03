---
layout: page
title: Work in progress 👷‍♂
permalink: /projects/
description: This section is under construction. It will be ready soon.
thesis: [Bachelor]
nav: false
nav_order: 2
---

<!-- Header 
display_categories: [Condensed Matter Physics, Computational Physics, Education and Science Outreach]
horizontal: false

-->

<p>You will be redirected to the main page within 3 seconds. If not redirected, please click <a href="{{ site.baseurl }}/">here</a>.</p>


<!-- pages/projects.md -->
<!-- <div class="projects"> 
{%- if site.enable_project_categories and page.display_categories %}-->
  <!-- Display categorized projects (Cooment)-->
<!--  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %} -->
  <!-- Generate cards for each project  (Comment)-->
<!--  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}-->

<!-- {%- else -%}-->
<!-- Display projects without categories (Comment) -->
<!--  {%- assign sorted_projects = site.projects | sort: "importance" -%} -->
  <!-- Generate cards for each project (Comment)-->
<!--  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div> -->

## My thesis projects

<div class="publications">

{%- for y in page.thesis %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f others %} 
{% endfor %}

</div>
