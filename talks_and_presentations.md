---
title: Talks and Presentations
layout: default
active_tab: talks_and_presentations
---


<table class="table"> 
<tbody>
  {% for year in (2000..2017) reversed %}
    <tr><td>
	<a name="{{year}}"></a><h1>{{year}}</h1>
    </td><td></td></tr>
    {% for presentation in site.data.presentations %}
    {%if presentation.year == year%}
    <tr>
      <td>
	{% if presentation.url %}
		<a href="{{ presentation.url }}">{{ presentation.title }}.</a>
        {% else %}
		{{ presentation.title }}.
	{% endif %}
	{% if presentation.award %}
		<b>{{ presentation.award }}.</b>
	{% endif %}
	{{ presentation.authors }}.
        {% if presentation.page_count < 8 and (presentation.venue == "ACL" or presentation.venue == "NAACL" or presentation.venue == "EMNLP" or presentation.venue == "EACL")   %}
		{{ presentation.venue }} {{ presentation.year }} short papers.
	{% else %}
		{{ presentation.venue }}  {{ presentation.year }}.
	{% endif %}

	{% if presentation.abstract %}
	<!-- abstract button -->
	<a data-toggle="modal" href="#{{presentation.id}}-abstract" class="label label-success">Abstract</a>
	<!-- /.abstract button -->
	<!-- abstract content -->
	<div id="{{presentation.id}}-abstract" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{presentation.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{presentation.id}}">{{presentation.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
        {{presentation.abstract}}
        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.abstract-content -->
	{% endif %}


<!-- ccb - turning off figures for now, until I can figure out how to load them in a lazy fashion, so that the user doesn't get bombarded with so much data -->
	{% if presentation.figures_TURN_OFF_FOR_NOW %}
	<!-- figures button -->
	<a data-toggle="modal" href="#{{presentation.id}}-figures" class="label label-primary">Figures</a>
	<!-- /.figures button -->
	<!-- figures content -->
	<div id="{{presentation.id}}-figures" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{presentation.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{presentation.id}}">{{presentation.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
	 <!-- Carousel -->
	<div id="{{presentation.id}}-figures-carousel" class="carousel slide" data-interval="false">

	  <!-- Carousel items -->
	  <div class="carousel-inner" role="listbox">
                {% assign isFirstFigure = 1 %}
	  	{% for figure in presentation.figures %}
		  	{% if isFirstFigure == 1 %}
			  	<div class="item active">
				<!-- ccb testing adding abstract as first time on carousel -->
			        <b>Abstract:</b> {{presentation.abstract}}
				</div>
			  	<div class="item">
				<!-- /ccb end testing adding abstract as first time on carousel -->
                		{% assign isFirstFigure = 0 %}
		  	{% else %}
			  	<div class="item">
                	{% endif %}
					<p><b>{{figure.label}}:</b> {{figure.caption}}</p>
<img src="{{figure.img}}" alt="" width="100%">
				</div>
		{% endfor %}
	  </div>
	  <!-- /.Carousel items -->
	  <!-- Controls -->
		<a class="left carousel-control" href="#{{presentation.id}}-figures-carousel" role="button" data-slide="prev">
		<span class="glyphicon glyphicon-chevron-left" aria-hidden="true" style="color:gray"></span>
		<span class="sr-only">Previous</span>
		</a>
		<a class="right carousel-control" href="#{{presentation.id}}-figures-carousel" role="button" data-slide="next">
		<span class="glyphicon glyphicon-chevron-right" aria-hidden="true" style="color:gray"></span>
		<span class="sr-only">Next</span>
		</a>
	  <!-- /.Controls -->
	</div>
	<!-- /.Carousel -->

        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.figures-content -->
	{% endif %}


	{% if presentation.bibtex %}
	<!-- bibtex button -->
	<a data-toggle="modal" href="#{{presentation.id}}-bibtex" class="label label-default">BibTex</a>
	<!-- /.bibtex button -->
	<!-- bibtex content -->
	<div id="{{presentation.id}}-bibtex" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{presentation.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{presentation.id}}">{{presentation.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
 	   <pre>{{presentation.bibtex}}
           </pre>
        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.bibtex-content -->
	{% endif %}
	</td>
    <tr>
    {% endif %}
    {% endfor %}
  {% endfor %}
<!-- ccb - debugging by removing </tbody> -->
<!-- ccb - debugging by removing</table> -->
