---
title: People
layout: default
active_tab: students
---

<h3 id="faculty">Faculty</h3>

<div class="container-fluid">
  <div class="row">
  {% for prof in site.data.faculty %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if prof.homepage %}
        <a href="{{ prof.homepage }}"><img src="assets/img/students/{{prof.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/></a><br />
         <b><a href="{{ prof.homepage }}">{{ prof.name }}</a></b><br />
        {% else %}
	<img src="assets/img/students/{{prof.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/><br />
         <b>{{ prof.name }}</b><br />
        {% endif %}
        {{ prof.degree }}<br />
        {{ prof.institution }}<br /> 
      </div>
  {% endfor %}
  </div>
</div>


<h3 id="students">PhD Students</h3>

<div class="container-fluid">
  <div class="row">
  {% for student in site.data.students %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if student.homepage %}
        <a href="{{ student.homepage }}"><img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/></a><br />
         <b><a href="{{ student.homepage }}">{{ student.name }}</a></b><br />
        {% else %}
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/><br />
         <b>{{ student.name }}</b><br />
        {% endif %}
        {{ student.degree }}<br />
        {{ student.institution }}<br /> 
      </div>
  {% endfor %}
  </div>
</div>



<h3 id="RAs">MSc Students</h3>

<div class="container-fluid">
  <div class="row">
  {% for student in site.data.research_assistants %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if student.homepage %}
        <a href="{{ student.homepage }}"><img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/></a><br />
         <b><a href="{{ student.homepage }}">{{ student.name }}</a></b><br />
        {% else %}
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/><br />
         <b>{{ student.name }}</b><br />    
        {% endif %}     
        {{ student.degree }}<br />
	{% if student.project %}
		Project: {{ student.project }} 
	{% endif %}
      </div>
  {% endfor %}
  </div>
</div>

<h3>Past PhD Students</h3>

<div class="container-fluid">
  <div class="row">
  {% for student in site.data.students_graduated %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
	  	{% if student.homepage %}
        <a href="{{ student.homepage }}"><img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/></a><br />
         <b><a href="{{ student.homepage }}">{{ student.name }}</a></b><br />
        {% else %}
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/><br />
         <b>{{ student.name }}</b><br />    
        {% endif %}
        Graduated from {{ student.institution }},  {{ student.graduation_date }}<br /> 

	{% if student.thesis_link %}
        Thesis: <a href="publications/{{ student.thesis_link}}">{{ student.thesis_title }}</a><br /> 
	{% else %}
        Thesis: {{ student.thesis_title }}<br />
	{% endif %}
	{% if student.advisors contains ' and ' %}
		Advisors: {{student.advisors}}<br />
	{% else %}
		Advisor: {{student.advisors}}<br />
	{% endif %}
	{% if student.current_position and student.current_employer %}
		Current position: {{ student.current_position }} at {{ student.current_employer }}
	{% endif %}
      </div>
  {% endfor %}
  </div>
</div>


<h3>Past Postdocs</h3>

<div class="container-fluid">
  <div class="row">
  {% for postdoc in site.data.past_postdocs %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if postdoc.homepage %}
        <a href="{{ postdoc.homepage }}"><img src="assets/img/students/{{postdoc.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/></a><br />
         <b><a href="{{ postdoc.homepage }}">{{ postdoc.name }}</a></b><br />
        {% else %}
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 200px; max-width: 200px"/><br />
         <b>{{ postdoc.name }}</b><br />         
        {% endif %}
	{% if postdoc.current_position and postdoc.current_employer %}
		Current position: {{ postdoc.current_position }} at {{ postdoc.current_employer }}
	{% endif %}
      </div>
  {% endfor %}
  </div>
</div>


