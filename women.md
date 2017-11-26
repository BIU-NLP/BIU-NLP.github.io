---
title: I am with you
layout: default
active_tab: students
---



<div class="container-fluid">
  <div class="row">


  {% for student in site.data.students %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
         <b>{{ student.degree }}</b><br />
      </div>
	{% endif %}
  {% endfor %}

  {% for student in site.data.students_graduated %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
         <b>Graduated PhD</b><br />
      </div>
	{% endif %}
  {% endfor %}

  {% for student in site.data.past_postdocs %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
         <b>Past Postdoc</b><br />
      </div>
	{% endif %}
  {% endfor %}
  </div>
</div>


<div class="container-fluid">
  <div class="row">
  {% for student in site.data.TAs.cis121_fall_2016 %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/TAs/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
{% if student.extra_title %}
         <b>{{ student.extra_title }}</b><br /> 
{% else %}
         <b>TA</b><br />
{% endif %}
      </div>
	{% endif %}
  {% endfor %}

  {% for student in site.data.research_assistants %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
         <b>{{ student.role }}</b><br />
      </div>
	{% endif %}
  {% endfor %}


  {% for project in site.data.past_team_projects %}
    {% for student in project.students %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
         <b>{{ student.role }}</b><br />
      </div>
	{% endif %}
  {% endfor %}
  {% endfor %}



  {% for semester in site.data.past_research_assistants %}
    {% for student in semester.students %}
	{% if student.gender == "female" %}
      <div align="center" class="col-lg-3 col-md-6 col-xs-12" style="margin-bottom: 20px">
	<img src="assets/img/students/{{student.pic}}"  class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
         <b>{{ student.name }}</b><br />
         <b>{{ student.role }} - {{ semester.semester }}</b><br />
      </div>
	{% endif %}
  {% endfor %}
  {% endfor %}

  </div>
</div>
