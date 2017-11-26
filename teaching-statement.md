---
title: Teaching Statement - Chris Callison-Burch
layout: default
active_tab: main_page 
keep_sidebar: false
publications:
- teaching-machine-translation
---

# Chris Callison-Burch: Teaching Statement
<p class="text-muted">
(Last updated {{ site.time | date: "%B %d, %Y" }})<br/>
</p>

I teach three courses at Penn.  Two are courses related to my research, and one is an introductory undergraduate course.  My teaching philosophy is that students are best engaged through hands-on work.  This idea is borne out in the project-based design of my classes, and in my mentorship of undergraduates and master's students through research projects.  Here, I'll describe my courses, my work with undergraduates and master's students, and my personal efforts at increasing the number of women in computer science.

 

## [Machine Translation (CIS 526)](http://mt-class.org/penn/)

I have been working in the field of machine translation since 2000, when statistical data-driven approaches became the dominant paradigm.  Statistical machine translation emerged as the clear winner of more than a decade's worth of DARPA bakeoffs, and it underlies commercial translation services like Google's online translation platform and Skype's speech-to-speech translation.  I co-designed a course at Johns Hopkins University with my colleagues Adam Lopez and Matt Post to teach the fundamental techniques that underlie statistical machine translation to graduate students and advanced undergrads.  In addition to a set of 20+ full lectures, we created an innovative set of hands-on projects.  We published a journal article about the course projects
[(Lopez et al, 2013)](#teaching-machine-translation).  Here is the abstract of the article: 


> Machine translation (MT) draws from several different disciplines, making it a complex subject to teach. There are excellent pedagogical texts, but problems in MT and current algorithms for solving them are best learned by doing. As a centerpiece of our MT course, we devised a series of open-ended challenges for students in which the goal was to improve performance on carefully constrained instances of four key MT tasks: alignment, decoding, evaluation, and reranking. Students brought a diverse set of techniques to the problems, including some novel solutions which performed remarkably well. A surprising and exciting outcome was that student solutions or their combinations fared competitively on some tasks, demonstrating that even newcomers to the field can help improve the state-of-the-art on hard NLP problems while simultaneously learning a great deal. The problems, baseline code, and results are freely available.


All of the projects represent contemporary research topics within the field of machine translation.  Unlike problem sets, in that they are open-ended assignments, and none of them has a "correct" solution.  However, they all have objective measures of how good the students' solutions are.  We are able to automatically score their solutions and we maintain a public leaderboard that shows which of the students have the current best solution.  This encourages friendly competition among the students, and sometimes drives the students to create novel solutions that approach the state-of-the-art. Our course materials and lectures are all freely available, and they have been used to teach courses at several other universities (Carnegie Mellon University, Johns Hopkins University, University of Illinois at Urbana-Champaign, Simon Frasier University, and the University of Edinburgh).  Professors at these universities have contributed improvements to the class.  We advertise our courses collectively at [http://mt-class.org/](http://mt-class.org/).


## [Crowdsourcing and Human Computation (NETS 213)](http://crowdsourcing-class.org/)

I helped to popularize the use of crowdsourcing within the field of natural language processing (NLP).  Through my grants, I have spent approximately \$250,000 to create new data sets for NLP that would have cost millions using previous techniques.    Crowdsourcing has transformed the way that I approach my research.  Instead of taking an existing data set and thinking "How can I build a model that performs better on this problem?", I now think "What problems do I actually want to solve, and what sort of data do I need to solve them?"  This opens new horizons in research, and allows creative solutions to new problems.

My interest in crowdsourcing has expanded beyond NLP.  I created a new course on Crowdsourcing and Human Computation.  Here is the course description: 

> Crowdsourcing and human computation are emerging fields that sit squarely at the intersection of economics and computer science. They examine how people can be used to solve complex tasks that are currently beyond the capabilities of artificial intelligence algorithms. Online marketplaces like Mechanical Turk and CrowdFlower provide an infrastructure that allows micropayments to be given to people in return for completing human intelligence tasks. This opens up previously unthinkable possibilities like people being used as function calls in software. We will investigate how crowdsourcing can be used for computer science applications like machine learning, next-generation interfaces, and data mining. Beyond these computer science aspects, we will also delve into topics like prediction markets, the sharing economy,  how businesses capitalize on collective intelligence, and the fundamental principles that underlie democracy and other group decision-making processes.

I designed the course to appeal to students in Penn's interdisciplinary major Networks and Social Systems Engineering ("NETS" for short).  NETS students bring computer science fundamentals to bear on a variety of problems in other disciplines. Among other things, my course shows how computer science can be used to do things like empower epidemiologists and enable data-driven public policy. 

In the homework assignments, we build [a structured database about all reported incidents of gun violence in the United States](http://gun-violence.org).   This idea came through a collaboration with Doug Weibe, a professor in Department of Biostatistics and Epidemiology in Penn's School of Medicine, who studies gun violence from a public heath perspective.  Congress has blocked the CDC and NIH from conducting research on this topic.  The homework assignments in NETS 213 combine together to create exactly the sort of gun violence database that partisan congressional action has sought to block. First, [students use machine learning](http://crowdsourcing-class.org/assignment4.html) to train a text classifier to predict whether an article describes an incident of gun violence or not.  They apply it to more than 2 million web pages harvested from over 2,000 local newspapers around the country. Next, they have [crowd workers validate the predictions of the classifier](http://crowdsourcing-class.org/assignment5.html).  The students learn how to use Mechanical Turk and how to perform [quality control on contributions from anonymous crowd workers](http://crowdsourcing-class.org/assignment7.html).  They then build an [interface that allows crowd workers to extract structured information](http://crowdsourcing-class.org/assignment8.html) from the gun violence articles (including things like the location of the shooting, demographic information of the shooter and the victim, and details about the circumstances like whether alcohol was involved, or if it was an incident of domestic violence).  Finally they [create visualizations to analyze the data](http://crowdsourcing-class.org/assignment9.html) that they created.  

My goal is to engage students by showing them how research can have social impact.  So far the strategy has been working.  The course enrollment doubled from 25 students in the first year, to 50 in the second.  More than 100 students have signed up to take it when I teach it again this Spring.
 
## [Data Structures and Algorithms (CIS 121)](http://www.seas.upenn.edu/~cis121/current/)

This year I have started teaching CIS 121, which is Penn's introduction to data structures and algorithms.  This is the third or fourth course that undergraduates take in their computer science major, depending on whether they have had programming experience in high school or not.  It's an incredibly fun course to teach for a lot of reasons.  This is the course where the *science* part of computer science really comes into focus through the analysis of algorithms.  Students become much better programmers because they implement and analyze the algorithms and data structures that are the fundamental building blocks of more sophisticated programs.  Also, this course is probably the most valuable course that students take to prepare for computer science job interviews. 

The course has an enrollment of more than 200 students.   I work with a staff of 26 incredible undergraduate TAs.  In many ways the TAs have a larger influence on the students' experience in the course.   They run the recitations and give the majority of the office hours in the course.   Over the years the TAs have designed the programming assignments as well.  In addition to lecturing and writing exams and written homework assignments, my role is really organizational and logistical. 

When I teach the course in the future, I hope to help turn it into a conduit for recruiting more students into the major, and to encourage more students from outside of Engineering to a minor in computer science.  I would like to make the course accessible to all students by showing the practical value of the course material.  I have made efforts to recruit more women to be part of the teaching staff.  In my first year teaching the course, only 3 out of 19 of the staff were women.  Now 10 of the [26 TAs](http://www.seas.upenn.edu/~cis121/current/) are women, and the 3 head TAs are all women.


## Mentorship of Undergraduates and Master's Students

I am currently working with 21 undergraduate and master's students.  I supervise these students through independent students, or paid research assistantships, and through team project work.  My own career was profoundly influenced by working with a professor when I was an undergraduate at Stanford University.  It was that experience of doing research that made me decide that grad school was in my future, which in turn lead to my career in academia.  I have a policy that I will start a research project with any student who is interested in working with me.  I formulate a reasonably circumscribed project that should be doable in 1-2 months.  At the end of that time, the student and I evaluate whether we should continue, with the idea that either of us can back out without causing offense.  The student gets to assess whether NLP research actually fits their interests.  I assess whether it is worth it for me to set aside time to work with the student, which I typically do if the student is enthusiastic and productive.  I have weekly one-on-one meetings with each of the students, plus a weekly group meeting where the students get to practice presenting their research in a way that is understandable to others and where the students get advice from one another.

## Women in Computer Science

I am proud of my track record of trying to promote women in computer science.   At Johns Hopkins University, I was the chair of the diversity committee for the CS department.  I helped to start a Women in Computer Science (WiCS) group.  The goals of WiCS were to foster a sense of community and to improve retention of women in our undergraduate program. We offered undergraduates mentorship from female graduate students and from faculty (like myself), introduced the students to research opportunities,  offered them advice on applying for graduate programs and jobs post-graduation, and wrote letters of recommendation for NSF Fellowships and grad school. I mentored 6 undergraduates at JHU through WiCS.  One of them, Ellie Pavlick, went on to apply to the PhD program at Penn.  She has become one of my strongest PhD students.

Of the [PhD students postdocs, and visiting scholars who I am currently advising](students.html#phds) at JHU and Penn, 6 of 9 are women.  At Penn, 5 of 6 of them are women. Of [the undergraduates and master's students who I am now mentoring](students.html#RAs),  13 of 21  are women.  I hope to continue improving the gender diversity of the computer science department here, and I feel that the best way of doing so it to engage women in research. 


## Bibliography 

  
<table class="table"> 
  <tbody>

{% for year in (2000..2015) reversed %}
 {% for id in page.publications %}
  {% for publication in site.data.publications %}
   {% if publication.id == id %} 
    {% if publication.year == year %}
    <tr id="{{ publication.id }}">
      <td>
	{% if publication.url %}
		<a href="{{ publication.url }}">{{ publication.title }}.</a>
        {% else %}
		{{ publication.title }}.
	{% endif %}
	{{ publication.authors }}.
	{{ publication.venue }}-{{ publication.year }}.

	{% if publication.abstract %}
	<!-- abstract button -->
	<a data-toggle="modal" href="#{{publication.id}}-abstract" class="label label-success">Abstract</a>
	<!-- /.abstract button -->
	<!-- abstract content -->
	<div id="{{publication.id}}-abstract" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{publication.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{publication.id}}">{{publication.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
        {{publication.abstract}}
        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.abstract-content -->
	{% endif %}


	{% if publication.figures %}
	<!-- figures button -->
	<a data-toggle="modal" href="#{{publication.id}}-figures" class="label label-primary">Figures</a>
	<!-- /.figures button -->
	<!-- figures content -->
	<div id="{{publication.id}}-figures" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{publication.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{publication.id}}">{{publication.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
	 <!-- Carousel -->
	<div id="{{publication.id}}-figures-carousel" class="carousel slide" data-interval="false">

	  <!-- Carousel items -->
	  <div class="carousel-inner" role="listbox">
                {% assign isFirstFigure = 1 %}
	  	{% for figure in publication.figures %}
		  	{% if isFirstFigure == 1 %}
			  	<div class="item active">
			        <b>Abstract:</b> {{publication.abstract}}
				</div>
			  	<div class="item">
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
		<a class="left carousel-control" href="#{{publication.id}}-figures-carousel" role="button" data-slide="prev">
		<span class="glyphicon glyphicon-chevron-left" aria-hidden="true" style="color:gray"></span>
		<span class="sr-only">Previous</span>
		</a>
		<a class="right carousel-control" href="#{{publication.id}}-figures-carousel" role="button" data-slide="next">
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


	{% if publication.bibtex %}
	<!-- bibtex button -->
	<a data-toggle="modal" href="#{{publication.id}}-bibtex" class="label label-default">BibTex</a>
	<!-- /.bibtex button -->
	<!-- bibtex content -->
	<div id="{{publication.id}}-bibtex" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="{{publication.id}}">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="{{publication.id}}">{{publication.title}}</h4>
        </div><!-- /.modal-header -->
        <div class="modal-body">
 	   <pre>{{publication.bibtex}}
           </pre>
        </div><!-- /.modal-body -->
	</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
	</div><!-- /.bibtex-content -->
	{% endif %}
	</td>
    <tr>
    {% endif %}
   {% endif %}
  {% endfor %}
 {% endfor %}
{% endfor %}
