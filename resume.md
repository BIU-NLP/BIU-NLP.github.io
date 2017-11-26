---
title: Chris Callison-Burch 
layout: default
active_tab: CV
---
<h1>Chris Callison-Burch: CV</h1>
<p class="text-muted">
(Last updated {{ site.time | date: "%B %d, %Y" }})<br/>
</p>

<h2>Employment</h2>

<table class="table"> 
  <tbody>
  {% for job in site.data.employment %}
     <tr>
       <td><b>{{job.position}}</b><br /> {{job.employer}}, {{job.location}}</td>
       <td>{{job.start_date}}-{{job.end_date}}</td>
     </tr>
<!--
     {% if job.description %}
     <tr>
        <td colspan="2">{{job.description}}</td>
     </tr>
     {% endif %}
-->
  {% endfor %}
  </tbody>
</table>

<h2>Education</h2>
<table class="table"> 
  <tbody>
  {% for degree in site.data.education %}
     <tr>
       <td><b>{{degree.degree}}</b><br /> 
		{{degree.institution}}, {{degree.location}}
		{% if degree.thesis %}<br /> 
		<i>Thesis:</i>{{degree.thesis}}.<br /> 
		<i>Advisors:</i>{{degree.advisor}}. 
     		{% endif %}
	</td>
       <td>{{degree.end_date}}</td>
     </tr>
  {% endfor %}
  </tbody>
</table>


<h2>Teaching</h2>

<table class="table"> 
  <tbody>
  {% for course in site.data.teaching %}
     <tr>
       <td>
	{% if course.url %}
		<a href="{{course.url}}"><b>{{course.title}}</b></a>
	{% else %}
		<b>{{course.title}}</b>
	{% endif %}
		({{course.number}})
	{% if course.coinstructors %}
		<i>co-taught with {{course.coinstructors}}</i>
	{% endif %}
		<br /> 
		{{course.institution}}
	</td>
       <td>{{course.term}} {{course.year}}</td>
     </tr>
     {% if course.description %}
     <tr>
        <td colspan="2">{{course.description}}</td>
     </tr>
     {% endif %}
  {% endfor %}

  </tbody>
</table>


<h2>Teaching Reviews at Penn</h2>
Quality scale (0-4): 0=Poor, 1=Fair, 2=Good, 3=Very Good, 4=Excellent
<table class="table"> 
  <tbody>
     <tr>
       <th>Term</th>
       <th>Course Title (Number)</th>
       <th>Students Enrolled</th>
       <th>Course Quality</th>
       <th>Instructor Quality</th>
     </tr>
  {% for course in site.data.teaching %}
      {% if course.institution == "University of Pennsylvania" %}
     <tr>
       <td>{{course.term}} {{course.year}}</td>
       <td>{{course.title}} ({{course.number}})</td>
       <td>{{course.enrollment}}</td>
       <td>{{course.course_rating | round: 1}}</td>
       <td>{{course.instructor_rating | round: 1}}</td>
     </tr>
      {% endif %}
  {% endfor %}
  </tbody>
</table>


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


<h2>Publications</h2>

<!-- iterate over the different publication types -->
{% assign publication_types = "conference,journal,chapter,workshop,thesis" | split: "," %}
{% for publication_type in publication_types %}

<!-- print the publication type -->
{%if publication_type == "conference" %}
<h3>Refereed conference papers (most have <a href="https://www.aclweb.org/aclwiki/index.php?title=Conference_acceptance_rates">acceptance rates</a> ≈ 25%)</h3>
{% elsif publication_type == "journal" %}
<h3>Journal articles</h3>
{% elsif publication_type == "chapter" %}
<h3>Book chapters</h3>
{% elsif publication_type == "workshop" %}
<h3>Refereed workshop papers</h3>
{% elsif publication_type == "thesis" %}
<h3>Theses</h3>
{% endif %}


<ol>
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
  {% for year in (2000..this_year) reversed %}
    {% for publication in site.data.publications %}
    {%if publication.year == year and publication.type == publication_type%}

        {% if publication.url %}
<li><a href="http://cis.upenn.edu/~ccb/{{ publication.url }}">
	{{ publication.authors }} ({{publication.year}}).
	{{ publication.title }}.
        {% if publication.page_count < 8 and (publication.venue == "ACL" or publication.venue == "NAACL" or publication.venue == "EMNLP" or publication.venue == "EACL")   %}
		{{ publication.venue }} short papers.
	{% else %}
		{{ publication.venue }}.
	{% endif %}

        {% if publication.award %}
	<b> {{ publication.award }}.</b>
	{% endif %}
</a>
        {% if publication.page_count %}
		{{publication.page_count}} pages.
	{% endif %}
</li>
        {% else %}
<li>{{ publication.authors }} ({{publication.year}}).{{ publication.title }}.</li>
	{% endif %}
    {% endif %}
    {% endfor %}
  {% endfor %}
</ol>
{% endfor %}




<h2>Invited Talks</h2>

<ol>
    {% for talk in site.data.talks %}
<li> {{ talk.venue }}. {{talk.title}}. {{talk.date}} </li>
  {% endfor %}
</ol>


<h2>Academic Service</h2>

<ul>
    {% for item in site.data.service %}
<li>
	{{item.description}}
</li>
  {% endfor %}
</ul>



<h2>Current PhD Students and Postdocs</h2>

<ol>
    {% for student in site.data.students %}
<li> {{ student.name }},  {{ student.degree }}, {{ student.institution }}.
    {% if student.expected_graduation_date %}
    Expected graduation date: {{ student.expected_graduation_date }}
    {% endif %}
</li>

  {% endfor %}
</ol>

<h2>PhDs Graduated</h2>

<ol>
    {% for student in site.data.students_graduated %}
<li>
	{{ student.name }}, {{ student.institution }} 
	{% if student.advisors contains ' and ' %}
		(advisors: {{student.advisors}}),
	{% else %}
		(advisor: {{student.advisors}}),
	{% endif %}
	{% if student.thesis_link %}
        	"<a href="publications/{{ student.thesis_link}}">{{ student.thesis_title }}</a>", {{ student.graduation_date }}.
	{% else %}
        	"{{ student.thesis_title }}", {{ student.graduation_date }}.
	{% endif %}


</li>
  {% endfor %}
</ol>


<h2>Thesis Committees</h2>

<ol>
    {% for student in site.data.thesis_committees %}
<li>
	{{ student.name }}, {{ student.institution }} 
	{% if student.advisors contains ' and ' %}
		(advisors: {{student.advisors}}),
	{% else %}
		(advisor: {{student.advisors}}),
	{% endif %}
	"{{ student.thesis_title }}", {{ student.graduation_date }}.
</li>
  {% endfor %}
</ol>

