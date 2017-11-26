---
title: Chris Callison-Burch 
layout: default
active_tab: CV
---
<h1>Chris Callison-Burch</h1>
<p class="text-muted">
(Last updated {{ site.time | date: "%B %d, %Y" }})<br/>
</p>


<h2>Grants</h2>

{% assign grant_status = "current,pending,past" | split: "," %}
{% for status in grant_status %}

<!-- print the grant status -->
{%if status == "current" %}
<h3>Current grants</h3>
{% elsif status == "pending" %}
<h3>Pending grants</h3>
{% elsif status == "past" %}
<h3>Past grants</h3>
{% else %}
<h3>Other</h3>
{% endif %}


<table class="table"> 
  <tbody>
     <tr>
       <th>Grant Title</th>
       <th>Awarding Body</th>
       <th>Amount</th>
       <th>Dates</th>
       <th>PI Info</th>
     </tr>
  {% for grant in site.data.grants %}
    {% if grant.status == status %}
     <tr>
       <td>{{grant.title}}</td>
       <td>{{grant.awarding_body}}</td>
       <td>{{grant.amount}}</td>
       <td>{{grant.start_date}}{% if grant.end_date %}-{{grant.end_date}}{% endif %}</td>
       <td>{% if grant.PI_info %}{{grant.PI_info}}{% endif %}</td>
     </tr>
     {% endif %}
  {% endfor %}
  </tbody>
</table>

{% endfor %}
