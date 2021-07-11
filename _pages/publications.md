---
layout: archive
title: "Cursos"
permalink: /publications/
author_profile: true
---

En esta sección presentaré algunos cursos que llevaré acabo. Por el momento solo se mostrará el texto predeterminado. 

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


