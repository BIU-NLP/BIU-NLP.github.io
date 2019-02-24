---
title: People
layout: default
active_tab: students
---
<head>
  <link rel="stylesheet" href="people.css">
</head>

<h3 id="faculty">Faculty</h3>

<div class="container-fluid">
  <div class="row">
  {% for prof in site.data.faculty %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px, text-align: center">
        <a href="{{ prof.homepage }}">
			<img src="assets/img/faculty/{{prof.pic}}"  class="img-circle"/>
		</a>
		<br/>
		<paragraph style="display: inline-block">
        	<b><a href="{{ prof.homepage }}">{{ prof.name }}</a></b>
			<br/>
			{{ prof.degree }}
			<br/>
		</paragraph>
      </div>
	{% endfor %}
	</div>
	<br/>
</div>


<h3 id="students">PhD Students</h3>

<div class="container-fluid">
  <div class="row">
  {% for student in site.data.phd_students %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if student.homepage %}
        <a href="{{ student.homepage }}"><img src="assets/img/students/{{student.pic}}"  class="img-circle"></a>
		<br/>
        <b><a href="{{ student.homepage }}">{{ student.name }}</a></b><br/>
        {% else %}
		<img src="assets/img/students/{{student.pic}}"  class="img-circle"><br/>
        <b>{{ student.name }}</b><br/>
        {% endif %}
		{% if student.advisors %}
			Advisor: {{student.advisors}}<br/>
		{% endif %}
		<!--
        {{ student.degree }}<br />
        {{ student.institution }}<br /> 
		-->
      </div>
  {% endfor %}
  </div>
</div>



<h3 id="RAs">MSc Students</h3>

<div class="container-fluid">
  <div class="row">
  {% for student in site.data.master_students %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if student.homepage %}
        <a href="{{ student.homepage }}"><img src="assets/img/students/{{student.pic}}"  class="img-circle"/></a><br />
         <b><a href="{{ student.homepage }}">{{ student.name }}</a></b><br />
        {% else %}
		<img src="assets/img/students/{{student.pic}}"  class="img-circle"/><br />
        <b>{{ student.name }}</b><br />    
        {% endif %}
        
		{% if student.advisors %}
			Advisor: {{student.advisors}}<br />
		{% endif %}
		<!-- 
		{{ student.degree }}<br />
	{% if student.project %}
		Project: {{ student.project }} 
	{% endif %}
	 -->
      </div>
  {% endfor %}
  </div>
</div>


<h3>Alumni</h3>

<div class="container-fluid">
  <div class="row">
  {% for student in site.data.students_graduated %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
	  	{% if student.homepage %}
        <a href="{{ student.homepage }}"><img src="assets/img/students/{{student.pic}}"  class="img-circle"/></a><br />
         <b><a href="{{ student.homepage }}">{{ student.name }}</a></b><br />
        {% else %}
		<img src="assets/img/students/{{student.pic}}"  class="img-circle"/><br />
         <b>{{ student.name }}</b><br />    
        {% endif %}
		{{ student.degree }}<br />
		{% if student.advisors %}
			Advisor: {{student.advisors}}<br />
		{% endif %}
		{% if student.current_position and student.current_employer %}
			Current position: {{ student.current_position }} at {{ student.current_employer }}
		{% endif %}
<!--
	{% if student.thesis_link %}
        Thesis: <a href="publications/{{ student.thesis_link}}">{{ student.thesis_title }}</a><br /> 
 	{% else %}
        Thesis: {{ student.thesis_title }}<br />

	{% endif %}
-->
      </div>
  {% endfor %}
  </div>
</div>

<!--

<h3>Past Postdocs</h3>

<div class="container-fluid">
  <div class="row">
  {% for postdoc in site.data.past_postdocs %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px">
        {% if postdoc.homepage %}
        <a href="{{ postdoc.homepage }}"><img src="assets/img/students/{{postdoc.pic}}"  class="img-circle"/></a><br />
         <b><a href="{{ postdoc.homepage }}">{{ postdoc.name }}</a></b><br />
        {% else %}
	<img src="assets/img/students/{{student.pic}}"  class="img-circle"/><br />
         <b>{{ postdoc.name }}</b><br />         
        {% endif %}
	{% if postdoc.current_position and postdoc.current_employer %}
		Current position: {{ postdoc.current_position }} at {{ postdoc.current_employer }}
	{% endif %}
      </div>
  {% endfor %}
  </div>
</div>
-->


