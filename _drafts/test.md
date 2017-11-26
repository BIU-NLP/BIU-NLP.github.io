---
layout: paper
id: ppdb-reranking
figures: 
      -
         img: figures/ppdb-reranking/figure1.jpg
         label: Figure 1
         caption: PPDB 2.0 includes an improved scoring model for ranking paraphrases. Shown are the top 10 ranked para- phrases for the word berries according to PPDB 1.0 (left) and PPDB 2.0 (right). PPDB 2.0 also contains an entailment relation for every pair. These relations capture asymmetries in the paraphrases, such as the fact that strawberries entails berries, while fruits is entailed by berries.
      -
         img: figures/ppdb-reranking/figure2.jpg
         label: Figure 2
         caption: Scatterplots of automatic paraphrase scores versus human scores for four ways of automatically ranking the paraphrases&colon; p(e2 given e1) (far left), PPDB 1.0's heuristic ranking method (middle left), word2vec similarity (middle right), and our supervised model for PPDB 2.0 (far right).  Our rankings achieve the highest correlation with human judgments.
      -
         img: figures/ppdb-reranking/figure3.jpg
         label: Figure 3
         caption: Averaged precision of paraphrases lists for 100 phrases  randomly drawn from Wikipedia. Curves show precision @k for varying values of k, up to 100. Here, ``good'' paraphrases are defined as having received an average human rating >= 3.
      -
         img: figures/ppdb-reranking/table1.jpg
         label: Table 1
         caption: Quality of rankings using for the improved PPDB 2.0 score versus the current heuristic score. Both metrics (AP and MRR) range from 0 to 1 and higher is better. >=t means that the statistics are computed by considering a paraphrase to be “good” if its human judgments averaged >=t. 
      -
         img: figures/ppdb-reranking/table2.jpg
         label: Table 2
         caption: Some paraphrases of *the end*, ranked from most complex to most simple according to the style scores included in PPDB 2.0.
author:
- |
    Ellie Pavlick, Pushpendre Rastogi, Juri Ganitkevitch, Benjamin Van Durme, Chris Callison-Burch
title: |
    PPDB 2.0: Better paraphrase ranking, fine-grained entailment relations,
    word embeddings, and style classification
bibliography:
- 'rerank.bib'
references:
- id: geffet2004feature
  type: paper-conference
  author:
  - family: Geffet
    given: Maayan
  - family: Dagan
    given: Ido
  issued:
  - year: 2004
  title: Feature vector quality and distributional similarity
  container-title: Proceedings of the 20th international conference on computational
    linguistics
  publisher: Association for Computational Linguistics
  page: 247

- id: Ganitkevitch-Callison-Burch-2014:LREC
  type: paper-conference
  author:
  - family: Ganitkevitch
    given: Juri
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2014
    month: May
  title: The multilingual paraphrase database
  container-title: The 9th edition of the language resources and evaluation conference
  publisher: European Language Resources Association
  publisher-place: Reykjavik, Iceland
  URL: http://cis.upenn.edu/~ccb/publications/ppdb-multilingual.pdf

- id: bannard2005paraphrasing
  type: paper-conference
  author:
  - family: Bannard
    given: Colin
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2005
  title: Paraphrasing with bilingual parallel corpora
  container-title: ACL
  page: 597-604

- id: callison2008syntactic
  type: paper-conference
  author:
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2008
  title: Syntactic constraints on paraphrases extracted from parallel corpora
  container-title: EMNLP
  page: 196-205

- id: ganitkevitch2013ppdb
  type: paper-conference
  author:
  - family: Ganitkevitch
    given: Juri
  - family: Van Durme
    given: Benjamin
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2013
    month: June
  title: 'PPDB: The paraphrase database'
  title-short: PPDB
  container-title: NAACL-HLT
  publisher-place: Atlanta, Georgia
  page: 758-764

- id: sultan2014back
  type: article-journal
  author:
  - family: Sultan
    given: Md Arafat
  - family: Bethard
    given: Steven
  - family: Sumner
    given: Tamara
  issued:
  - year: 2014
  title: 'Back to basics for monolingual alignment: Exploiting word similarity and
    contextual evidence'
  title-short: Back to basics for monolingual alignment
  container-title: TACL
  page: 219-230
  volume: 2

- id: yao2013semi
  type: paper-conference
  author:
  - family: Yao
    given: Xuchen
  - family: Van Durme
    given: Benjamin
  - family: Callison-Burch
    given: Chris
  - family: Clark
    given: Peter
  issued:
  - year: 2013
  title: Semi-markov phrase-based monolingual alignment
  container-title: EMNLP
  page: 590-600

- id: rastogi2015multiview
  type: no-type
  author:
  - family: Rastogi
    given: Pushpendre
  - family: Van Durme
    given: Benjamin
  - family: Arora
    given: Raman
  issued:
  - year: 2015
  title: 'Multiview LSA: Representation learning via generalized CCA'
  title-short: Multiview LSA

- id: yatskar2010sake
  type: paper-conference
  author:
  - family: Yatskar
    given: Mark
  - family: Pang
    given: Bo
  - family: Danescu-Niculescu-Mizil
    given: Cristian
  - family: Lee
    given: Lillian
  issued:
  - year: 2010
  title: 'For the sake of simplicity: Unsupervised extraction of lexical simplifications
    from wikipedia'
  title-short: For the sake of simplicity
  container-title: 'Human language technologies: The 2010 annual conference of the
    north american chapter of the association for computational linguistics'
  publisher: Association for Computational Linguistics
  page: 365-368

- id: inui2003text
  type: paper-conference
  author:
  - family: Inui
    given: Kentaro
  - family: Fujita
    given: Atsushi
  - family: Takahashi
    given: Tetsuro
  - family: Iida
    given: Ryu
  - family: Iwakura
    given: Tomoya
  issued:
  - year: 2003
  title: 'Text simplification for reading assistance: A project note'
  title-short: Text simplification for reading assistance
  container-title: Proceedings of the second international workshop on paraphrasing-volume
    16
  publisher: Association for Computational Linguistics
  page: 9-16

- id: napoles2011paraphrastic
  type: paper-conference
  author:
  - family: Napoles
    given: Courtney
  - family: Callison-Burch
    given: Chris
  - family: Ganitkevitch
    given: Juri
  - family: Van Durme
    given: Benjamin
  issued:
  - year: 2011
  title: 'Paraphrastic sentence compression with a character-based metric: Tightening
    without deletion'
  title-short: Paraphrastic sentence compression with a character-based metric
  container-title: Proceedings of the workshop on monolingual text-to-text generation
  publisher: Association for Computational Linguistics
  page: 84-90

- id: ganitkevitch2011learning
  type: paper-conference
  author:
  - family: Ganitkevitch
    given: Juri
  - family: Callison-Burch
    given: Chris
  - family: Napoles
    given: Courtney
  - family: Van Durme
    given: Benjamin
  issued:
  - year: 2011
  title: Learning sentential paraphrases from bilingual parallel corpora for text-to-text
    generation
  container-title: EMNLP
  page: 1168-1179

- id: bosma2007paraphrase
  type: chapter
  author:
  - family: Bosma
    given: Wauter
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2007
  title: Paraphrase substitution for recognizing textual entailment
  container-title: Evaluation of multilingual and multi-modal information retrieval
  publisher: Springer
  page: 502-509

- id: androutsopoulos2010survey
  type: article-journal
  author:
  - family: Androutsopoulos
    given: Ion
  - family: Malakasiotis
    given: Prodromos
  issued:
  - year: 2010
  title: A survey of paraphrasing and textual entailment methods
  container-title: Journal of Artificial Intelligence Research
  page: 135-187

- id: berant2014semantic
  type: paper-conference
  author:
  - family: Berant
    given: Jonathan
  - family: Liang
    given: Percy
  issued:
  - year: 2014
  title: Semantic parsing via paraphrasing
  container-title: Proceedings of aCL
  collection-number: 1
  page: 92
  volume: 7

- id: xu2013gathering
  type: paper-conference
  author:
  - family: Xu
    given: Wei
  - family: Ritter
    given: Alan
  - family: Grishman
    given: Ralph
  issued:
  - year: 2013
  title: Gathering and generating paraphrases from twitter with application to normalization
  container-title: Proceedings of the sixth workshop on building and using comparable
    corpora
  publisher: Citeseer
  page: 121-12⒏

- id: ling2013paraphrasing
  type: paper-conference
  author:
  - family: Ling
    given: Wang
  - family: Dyer
    given: Chris
  - family: Black
    given: Alan W
  - family: Trancoso
    given: Isabel
  issued:
  - year: 2013
  title: Paraphrasing 4 microblog normalization.
  container-title: EMNLP
  page: 73-84

- id: mckeown1979paraphrasing
  type: paper-conference
  author:
  - family: McKeown
    given: Kathleen R
  issued:
  - year: 1979
  title: Paraphrasing using given and new information in a question-answer system
  container-title: Proceedings of the 17th annual meeting on association for computational
    linguistics
  publisher: Association for Computational Linguistics
  page: 67-72

- id: ravichandran2002learning
  type: paper-conference
  author:
  - family: Ravichandran
    given: Deepak
  - family: Hovy
    given: Eduard
  issued:
  - year: 2002
  title: Learning surface text patterns for a question answering system
  container-title: Proceedings of the 40th annual meeting on association for computational
    linguistics
  publisher: Association for Computational Linguistics
  page: 41-47

- id: riezler2007statistical
  type: paper-conference
  author:
  - family: Riezler
    given: Stefan
  - family: Vasserman
    given: Alexander
  - family: Tsochantaridis
    given: Ioannis
  - family: Mittal
    given: Vibhu
  - family: Liu
    given: Yi
  issued:
  - year: 2007
  title: Statistical machine translation for query expansion in answer retrieval
  container-title: Annual meeting-association for computational linguistics
  collection-number: 1
  page: 464
  volume: 45

- id: barzilay1999information
  type: paper-conference
  author:
  - family: Barzilay
    given: Regina
  - family: McKeown
    given: Kathleen R
  - family: Elhadad
    given: Michael
  issued:
  - year: 1999
  title: Information fusion in the context of multi-document summarization
  container-title: Proceedings of the 37th annual meeting of the association for computational
    linguistics on computational linguistics
  publisher: Association for Computational Linguistics
  page: 550-557

- id: zhou2006paraeval
  type: paper-conference
  author:
  - family: Zhou
    given: Liang
  - family: Lin
    given: Chin-Yew
  - family: Munteanu
    given: Dragos Stefan
  - family: Hovy
    given: Eduard
  issued:
  - year: 2006
  title: 'Paraeval: Using paraphrases to evaluate summaries automatically'
  title-short: Paraeval
  container-title: Proceedings of the main conference on human language technology
    conference of the north american chapter of the association of computational linguistics
  publisher: Association for Computational Linguistics
  page: 447-454

- id: madnani2007using
  type: paper-conference
  author:
  - family: Madnani
    given: Nitin
  - family: Ayan
    given: Necip Fazil
  - family: Resnik
    given: Philip
  - family: Dorr
    given: Bonnie J
  issued:
  - year: 2007
  title: Using paraphrases for parameter tuning in statistical machine translation
  container-title: Proceedings of the second workshop on statistical machine translation
  publisher: Association for Computational Linguistics
  page: 120-127

- id: snover2009ter
  type: article-journal
  author:
  - family: Snover
    given: Matthew G
  - family: Madnani
    given: Nitin
  - family: Dorr
    given: Bonnie
  - family: Schwartz
    given: Richard
  issued:
  - year: 2009
  title: 'TER-plus: Paraphrase, semantic, and alignment enhancements to translation
    edit rate'
  title-short: TER-plus
  container-title: Machine Translation
  publisher: Springer
  page: 117-127
  volume: 23
  issue: 2-3

- id: pavlick2015inducing
  type: paper-conference
  author:
  - family: Pavlick
    given: Ellie
  - family: Nenkova
    given: Ani
  issued:
  - year: 2015
  title: Inducing lexical style properties for paraphrase and genre differentiation
  container-title: NAACL

- id: malakasiotis2011generate
  type: paper-conference
  author:
  - family: Malakasiotis
    given: Prodromos
  - family: Androutsopoulos
    given: Ion
  issued:
  - year: 2011
  title: A generate and rank approach to sentence paraphrasing
  container-title: EMNLP
  page: 96-106

- id: feng:2013:ACL2013
  type: paper-conference
  author:
  - family: Feng
    given: Song
  - family: Kang
    given: Jun Sak
  - family: Kuznetsova
    given: Polina
  - family: Choi
    given: Yejin
  issued:
  - year: 2013
    month: Angust
  title: 'Connotation lexicon: A dash of sentiment beneath the surface meaning'
  title-short: Connotation lexicon
  container-title: 'Proceedings of the 51th annual meeting of the association for
    computational linguistics (volume 2: Short papers)'
  publisher: Association for Computational Linguistics
  publisher-place: Sofia, Bulgaria

- id: mitchell-lapata:2008:ACLMain
  type: paper-conference
  author:
  - family: Mitchell
    given: Jeff
  - family: Lapata
    given: Mirella
  issued:
  - year: 2008
    month: June
  title: Vector-based models of semantic composition
  container-title: 'Proceedings of aCL-08: HLT'
  URL: http://www.aclweb.org/anthology/P/P08/P08-1028

- id: hill2014simlex
  type: article-journal
  author:
  - family: Hill
    given: Felix
  - family: Reichart
    given: Roi
  - family: Korhonen
    given: Anna
  issued:
  - year: 2014
  title: 'Simlex-999: Evaluating semantic models with (genuine) similarity estimation'
  title-short: Simlex-999
  container-title: arXiv preprint arXiv:1408.3456

- id: ludeep
  type: article-journal
  author:
  - family: Lu
    given: Ang
  - family: Wang
    given: Weiran
  - family: Bansal
    given: Mohit
  - family: Gimpel
    given: Kevin
  - family: Livescu
    given: Karen
  issued:
  - year: 2015
  title: Deep multilingual correlation for improved word embeddings

- id: lazaridou2015combining
  type: article-journal
  author:
  - family: Lazaridou
    given: Angeliki
  - family: Pham
    given: Nghia The
  - family: Baroni
    given: Marco
  issued:
  - year: 2015
  title: Combining language and vision with a multimodal skip-gram model
  container-title: arXiv preprint arXiv:1501.02598

- id: grefenstette2015concrete
  type: article-journal
  author:
  - family: Grefenstette
    given: Edward
  - family: Sadrzadeh
    given: Mehrnoosh
  issued:
  - year: 2015
  title: Concrete models and empirical evaluations for the categorical compositional
    distributional model of meaning
  container-title: Computational Linguistics
  publisher: MIT Press

- id: xu2015problems
  type: article-journal
  author:
  - family: Anonymous
  issued:
  - year: 2015
  title: 'Problems in current text simplification research: New data can help'
  title-short: Problems in current text simplification research
  container-title: TACL (in review)

- id: chan2011reranking
  type: paper-conference
  author:
  - family: Chan
    given: Tsz Ping
  - family: Callison-Burch
    given: Chris
  - family: Van Durme
    given: Benjamin
  issued:
  - year: 2011
  title: Reranking bilingually extracted paraphrases using monolingual distributional
    similarity
  container-title: GEMS
  page: 33-42

- id: malakasiotis2009paraphrase
  type: paper-conference
  author:
  - family: Malakasiotis
    given: Prodromos
  issued:
  - year: 2009
  title: Paraphrase recognition using machine learning to combine similarity measures
  container-title: Proceedings of the aCL-iJCNLP 2009 student research workshop
  publisher: Association for Computational Linguistics
  page: 27-35

- id: kotlerman2010directional
  type: article-journal
  author:
  - family: Kotlerman
    given: Lili
  - family: Dagan
    given: Ido
  - family: Szpektor
    given: Idan
  - family: Zhitomirsky-Geffet
    given: Maayan
  issued:
  - year: 2010
  title: Directional distributional similarity for lexical inference
  container-title: Natural Language Engineering
  publisher: Cambridge Univ Press
  page: 359-389
  volume: 16
  issue: 04

- id: bhagat2007ledir
  type: paper-conference
  author:
  - family: Bhagat
    given: Rahul
  - family: Pantel
    given: Patrick
  - family: Hovy
    given: Eduard H
  - family: Rey
    given: Marina
  issued:
  - year: 2007
  title: 'LEDIR: An unsupervised algorithm for learning directionality of inference
    rules.'
  title-short: LEDIR
  container-title: EMNLP-coNLL
  page: 161-170

- id: socher2012semantic
  type: paper-conference
  author:
  - family: Socher
    given: Richard
  - family: Huval
    given: Brody
  - family: Manning
    given: Christopher D
  - family: Ng
    given: Andrew Y
  issued:
  - year: 2012
  title: Semantic compositionality through recursive matrix-vector spaces
  container-title: Proceedings of the joint conference of eMNLP and coNLL
  page: 1201-1211

- id: grefenstette2011experimental
  type: paper-conference
  author:
  - family: Grefenstette
    given: Edward
  - family: Sadrzadeh
    given: Mehrnoosh
  issued:
  - year: 2011
  title: Experimental support for a categorical compositional distributional model
    of meaning
  container-title: EMNLP

- id: pennington2014glove
  type: article-journal
  author:
  - family: Pennington
    given: Jeffrey
  - family: Socher
    given: Richard
  - family: Manning
    given: Christopher D
  issued:
  - year: 2014
  title: 'Glove: Global vectors for word representation'
  title-short: Glove
  container-title: Proceedings of the Empiricial Methods in Natural Language Processing
    (EMNLP 2014)
  volume: 12

- id: jimenez2014unal
  type: article-journal
  author:
  - family: Jimenez
    given: Sergio
  - family: Duenas
    given: George
  - family: Baquero
    given: Julia
  - family: Gelbukh
    given: Alexander
  - family: Bátiz
    given: Av Juan Dios
  - family: Mendizábal
    given: Av
  issued:
  - year: 2014
  title: 'UNAL-nLP: Combining soft cardinality features for semantic textual similarity,
    relatedness and entailment'
  title-short: UNAL-nLP
  container-title: SemEval 2014
  page: 732

- id: vo2014fbk
  type: article-journal
  author:
  - family: Vo
    given: Ngoc Phuoc An
  - family: Popescu
    given: Octavian
  - family: Caselli
    given: Tommaso
  issued:
  - year: 2014
  title: 'FBK-tR: SVM for semantic relatedness and corpus patterns for rTE'
  title-short: FBK-tR
  container-title: SemEval 2014
  page: 289

- id: maccartney:thesis
  type: thesis
  author:
  - family: MacCartney
    given: Bill
  issued:
  - year: 2009
  title: Natural language inference
  publisher: Citeseer
  genre: PhD thesis

- id: han2013umbc
  type: paper-conference
  author:
  - family: Han
    given: Lushan
  - family: Kashyap
    given: Abhay
  - family: Finin
    given: Tim
  - family: Mayfield
    given: James
  - family: Weese
    given: Jonathan
  issued:
  - year: 2013
  title: 'UMBC eBIQUITY-cORE: Semantic textual similarity systems'
  title-short: UMBC eBIQUITY-cORE
  container-title: Proceedings of the second joint conference on lexical and computational
    semantics
  page: 44-52
  volume: 1

- id: yu2014improving
  type: paper-conference
  author:
  - family: Yu
    given: Mo
  - family: Dredze
    given: Mark
  issued:
  - year: 2014
  title: Improving lexical embeddings with semantic knowledge
  container-title: ACL
  page: 545-550
  volume: 2

- id: ji2013discriminative
  type: paper-conference
  author:
  - family: Ji
    given: Yangfeng
  - family: Eisenstein
    given: Jacob
  issued:
  - year: 2013
  title: Discriminative improvements to distributional sentence similarity.
  container-title: EMNLP
  page: 891-896

- id: beltagy2014utexas
  type: paper-conference
  author:
  - family: Beltagy
    given: Islam
  - family: Roller
    given: Stephen
  - family: Boleda
    given: Gemma
  - family: Erk
    given: Katrin
  - family: Mooney
    given: Raymond J
  issued:
  - year: 2014
  title: 'UTexas: Natural language semantics using distributional semantics and
    probabilistic logic'
  title-short: UTexas
  container-title: SemEval

- id: bjerva2014meaning
  type: paper-conference
  author:
  - family: Bjerva
    given: Johannes
  - family: Bos
    given: Johan
  - family: Goot
    given: Rob
    dropping-particle: van der
  - family: Nissim
    given: Malvina
  issued:
  - year: 2014
  title: 'The meaning factory: Formal semantics for recognizing textual entailment
    and determining semantic similarity'
  title-short: The meaning factory
  container-title: SemEval

- id: faruqui2015retrofitting
  type: paper-conference
  author:
  - family: Faruqui
    given: Manaal
  - family: Dodge
    given: Jesse
  - family: Jauhar
    given: Sujay K
  - family: Dyer
    given: Chris
  - family: Hovy
    given: Eduard
  - family: Smith
    given: Noah A
  issued:
  - year: 2015
  title: Retrofitting word vectors to semantic lexicons
  container-title: NAACL

- id: sultan-bethard-sumner:2014:SemEval
  type: paper-conference
  author:
  - family: Sultan
    given: Md Arafat
  - family: Bethard
    given: Steven
  - family: Sumner
    given: Tamara
  issued:
  - year: 2014
  title: 'DLS$@$CU: Sentence similarity from word alignment'
  title-short: DLS$@$CU
  container-title: SemEval
  URL: http://www.aclweb.org/anthology/S14-2039

- id: sultan-etal:2014:TACL
  type: article-journal
  author:
  - family: Sultan
    given: Md. Arafat
  - family: Bethard
    given: Steven
  - family: Sumner
    given: Tamara
  issued:
  - year: 2014
    month: 1
    day: 1
  title: 'Back to basics for monolingual alignment: Exploiting word similarity and
    contextual evidence'
  title-short: Back to basics for monolingual alignment
  container-title: Transactions of the Association for Computational Linguistics
  page: 219-230
  volume: 2
  keyword: text similarity
  URL: https://tacl2013.cs.columbia.edu/ojs/index.php/tacl/article/view/292

- id: pavlick2015adding
  type: paper-conference
  author:
  - family: Pavlick
    given: Ellie
  - family: Bos
    given: Johan
  - family: Nissim
    given: Malvina
  - family: Beller
    given: Charley
  - family: Van Durme
    given: Benjamin
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2015
  title: Adding semantics to data-driven paraphrasing
  container-title: ACL

- id: xu-EtAl:2012
  type: paper-conference
  author:
  - family: Xu
    given: Wei
  - family: Ritter
    given: Alan
  - family: Dolan
    given: Bill
  - family: Grishman
    given: Ralph
  - family: Cherry
    given: Colin
  issued:
  - year: 2012
  title: Paraphrasing for style
  container-title: COLING
  URL: http://www.aclweb.org/anthology/C12-1177

- id: mikolov-yih-zweig:2013:NAACL-HLT
  type: paper-conference
  author:
  - family: Mikolov
    given: Tomas
  - family: Yih
    given: Wen-tau
  - family: Zweig
    given: Geoffrey
  issued:
  - year: 2013
  title: Linguistic regularities in continuous space word representations
  container-title: 'NAAC:'
  URL: http://www.aclweb.org/anthology/N13-1090

- id: mikolov2013efficient
  type: paper-conference
  author:
  - family: Mikolov
    given: Tomas
  - family: Chen
    given: Kai
  - family: Corrado
    given: Greg
  - family: Dean
    given: Jeffrey
  issued:
  - year: 2013
  title: Efficient estimation of word representations in vector space
  container-title: Workshop at iCLR

- id: Dhillon2011NIPS
  type: paper-conference
  author:
  - family: Dhillon
    given: Paramveer S.
  - family: Foster
    given: Dean
  - family: Ungar
    given: Lyle
  issued:
  - year: 2011
  title: Multi-view learning of word embeddings via CCA
  container-title: NIPS

- id: Zhao2008b
  type: paper-conference
  author:
  - family: Zhao
    given: Shiqi
  - family: Niu
    given: Cheng
  - family: Zhou
    given: Ming
  - family: Liu
    given: Ting
  - family: Li
    given: Sheng
  issued:
  - year: 2008
  title: Combining multiple resources to improve SMT-based paraphrasing model
  container-title: ACL
  URL: http://www.aclweb.org/anthology/P/P08/P08-1116

- id: berant-dagan-goldberger:2011:ACL-HLT2011
  type: paper-conference
  author:
  - family: Berant
    given: Jonathan
  - family: Dagan
    given: Ido
  - family: Goldberger
    given: Jacob
  issued:
  - year: 2011
  title: Global learning of typed entailment rules
  container-title: ACL
  URL: http://www.aclweb.org/anthology/P11-1062

- id: snow2004learning
  type: paper-conference
  author:
  - family: Snow
    given: Rion
  - family: Jurafsky
    given: Daniel
  - family: Ng
    given: Andrew Y
  issued:
  - year: 2004
  title: Learning syntactic patterns for automatic hypernym discovery
  container-title: NIPS

- id: chiang2007hierarchical
  type: article-journal
  author:
  - family: Chiang
    given: David
  issued:
  - year: 2007
  title: Hierarchical phrase-based translation
  container-title: computational linguistics
  publisher: MIT Press
  page: 201-228
  volume: 33
  issue: 2

- id: post2013joshua
  type: paper-conference
  author:
  - family: Post
    given: Matt
  - family: Ganitkevitch
    given: Juri
  - family: Orland
    given: Luke
  - family: Weese
    given: Jonathan
  - family: Cao
    given: Yuan
  - family: Callison-Burch
    given: Chris
  issued:
  - year: 2013
  title: 'Joshua 5.0: Sparser, better, faster, server'
  title-short: Joshua 5.0
  container-title: Proceedings of the eighth workshop on statistical machine translation
  page: 206-212

- id: koehn2003statistical
  type: paper-conference
  author:
  - family: Koehn
    given: Philipp
  - family: Och
    given: Franz Josef
  - family: Marcu
    given: Daniel
  issued:
  - year: 2003
  title: Statistical phrase-based translation
  container-title: Proceedings of the 2003 conference of the north american chapter
    of the association for computational linguistics on human language technology-volume
    1
  publisher: Association for Computational Linguistics
  page: 48-54

- id: napoles2012annotated
  type: paper-conference
  author:
  - family: Napoles
    given: Courtney
  - family: Gormley
    given: Matthew
  - family: Van Durme
    given: Benjamin
  issued:
  - year: 2012
  title: Annotated gigaword
  container-title: Proceedings of the joint workshop on automatic knowledge base construction
    and web-scale knowledge extraction
  publisher: Association for Computational Linguistics
  page: 95-100

- id: brants2006google
  type: article-journal
  author:
  - family: Brants
    given: Thorsten
  - family: Franz
    given: Alex
  issued:
  - year: 2006
  title: The google web 1T 5-gram corpus version 1.1
  container-title: LDC2006T13
---



We present a new release of the Paraphrase Database. PPDB 2.0 includes a
discriminatively re-ranked set of paraphrases that achieve a higher
correlation with human judgments than PPDB 1.0’s heuristic rankings.
Each paraphrase pair in the database now also includes fine-grained
entailment relations, word embedding similarities, and style
annotations.

Introduction
============

The Paraphrase Database (PPDB) is a collection of over 100 million
paraphrases that was automatically constructed by . Although it is
relatively new, it has been adopted by a large number of researchers,
who have demonstrated that it is useful for a variety of natural
language processing tasks. It has been used for recognizing textual
entailment @beltagy2014utexas [@bjerva2014meaning], measuring the
semantic similarity of texts @han2013umbc
[@ji2013discriminative; @sultan-bethard-sumner:2014:SemEval],
monolingual alignment @yao2013semi [@sultan-etal:2014:TACL], natural
language generation @ganitkevitch2011learning, and improved lexical
embeddings @yu2014improving
[@rastogi2015multiview; @faruqui2015retrofitting].

<!--
|ranked paraphrases of *berries*|
| **PPDB 1.0**	| **PPDB 2.0**	| |
| 1. embayments |  1. strawberries |  $$\sqsubset$$ | 
| 2. strawberries |  2. raspberries |  $$\sqsubset$$ | 
| 3. racks |  3. blueberries |  $$\sqsubset$$ | 
| 4. grains |  4. blackberries |  $$\sqsubset$$ | 
| 5. raspberries |  5. fruits |  $$\sqsupset$$ | 
| 6. blueberries |  6. fruit |  $$\sqsupset$$ | 
| 7. fruits |  7. beans |  $$\#$$ | 
| 8. fruit |  8. grains |  $$\sim$$ | 
| 9. blackberries |  9. seeds |  $$\#$$ | 
| 10. beans |  10. kernels |  $$\#$$ | 
-->




For any given input phrase to PPDB, there are often dozens or hundreds
of possible paraphrases. There are several interesting research
questions that arise because of the number and variety of paraphrases in
PPDB. How can we distinguish between correct and incorrect paraphrases?
Within the paraphrase sets, are all of the paraphrases truly
substitutable or do they sometimes exhibit other types of relationships
(like directional entailment)? When the paraphrases share the same
meaning, are there stylistic reasons why we should choose one versus
another (e.g., is one paraphrase a less formal version of another)?



In this paper we describe several improvements to PPDB that address
these questions. We release PPDB version 2.0, incorporating the
following improvements:

-   A completely re-ranked set of paraphrases that uses a regression
    model to fit the paraphrase scores to human judgments of
    paraphrase quality. <a data-toggle="modal" data-target="#{{page.id}}-figures" data-slide-to="Figure 1">Figure 1</a>
    paraphrases for the word <span>*berries*</span>.

-   Each paraphrase pair is automatically labeled with an explicit
    entailment relationship. Instead of assuming all paraphrases are
    perfectly equivalent, we label some as one directional entailments
    (or other entailment types).

-   Each paraphrase rule now has new features that indicate when its
    application is expected to result in a change in style.

-   Each paraphrase entry in the database now has an associated word
    embedding learned using Multiview Latent Semantic Analysis.

Upon publication of this paper, we will release PPDB 2.0 along with a
set of 26K phrase pairs annotated with human similarity judgments.

Improved rankings of paraphrases {#model}
================================

The notion of ranking paraphrases goes back to the original method that
PPDB is based on. introduced the bilingual pivoting method, which
extracts <span>*incarcerated*</span> as a potential paraphrase of
<span>*put in prison*</span> since they are both aligned to
<span>*festgenommen*</span> in different sentence pairs in an
English-German bitext. Since <span>*incarcerated*</span> aligns to many
foreign words (in many languages) the list of potential paraphrases is
long. Paraphrases vary in quality since the alignments are automatically
produced and noisy. In order to rank the paraphrases, define a
paraphrase probability in terms of the translation model probabilities
$$p(f | e)$$ and 
$$p(e | f)$$: 

$$\begin{aligned}
  p(e_2|e_1) &\approx& \sum_f p(e_2|f) p(f|e_1) .
\label{paraphrase_prob_eqn}\end{aligned}$$

#### Heuristic scoring in PPDB 1.0

Instead of ranking the paraphrases with a single score, expanded the set
of scores in PPDB. Each paraphrase rule in PPDB consists of four
components: a phrase ($$e_1$$), a paraphrase ($$e_2$$), a syntactic category
($$LHS$$[^1]), and a feature vector. This feature vector contains 33
scores of paraphrase quality, which are described in full in the
supplementary material to this paper. The rules in PPDB 1.0 were scored
using an ad-hoc weighting of seven of these features, given by the
following equation:

$$\begin{aligned}
& &1.0 & \times &-log \ p(e_1|e_2) \\
&+&1.0 & \times & -log \ p(e_2|e_1)\\
&+&1.0 & \times&  -log \ p(e_1|e_2,LHS) \\
&+&1.0 & \times&   -log \ p(e_2|e_1,LHS) \\
&+&0.3 & \times &-log \ p(LHS|e_1) \\
&+&0.3 & \times &-log \ p(LHS|e_2)\\
&+&100 & \times & RarityPenalty \
\end{aligned}$$

where $$-log \ p(e_2|e_1) $$ is the paraphrase probability computed
according to Equation \[paraphrase~p~rob~e~qn\] and $$RarityPenalty$$ is a
real-valued feature that indicates how frequently the paraphrase was
observed in the training data.

This heuristic linear combination of scores was used to divide PPDB into
six increasingly large sizes– S, M, L, XL, XXL, and XXXL. PPDB-XXXL
contains all of the paraphrase rules and has the highest recall, but the
lowest average precision. The smaller sizes contain better average
scores but offer lower coverage. performed a small-scale analysis of how
their heuristic score correlated with human judgments by collecting
$$<$$2,000 judgments for PPDB paraphrases of verbs that occurred in
Propbank.

#### Supervised scoring model

For this paper, we rank the paraphrases using a supervised scoring
model. To train the model, we collected human judgements for 26,455
paraphrase pairs sampled from PPDB. Each paraphrase pair was judged by 5
people who each assigned a score on a 5-point Likert scale, as described
in . These 5 scores were averaged.

We used these human judgments to fit a regression to the 33 features
available in the PPDB 1.0 feature vector, plus an additional 176 new
features that we developed. Our features included the cosine similarity
of the word embeddings that we generated for each PPDB phrase (described
in Section \[multiviewLSA\]), as well as lexical overlap features,
features derived from WordNet, and distributional similarity features.
We weighted the contribution of these features using ridge regression
with its regularization parameter tuned using cross validation on the
training data.

See the supplemental materials for a complete description of the
features used in our model and our data collection methodology including
inter-annotator agreement.

Evaluating the rankings
-----------------------

We evaluate the new rankings in two ways:

-   We calculate the correlation of the different ways of automatically
    ranking the paraphrases against the 26k human judgments that
    we collected.

-   We compute the goodness (in terms of mean reciprocal rank and
    averaged precision) of the ranked paraphrase lists for 100 phrases
    drawn randomly from Wikipedia.

#### Correlation

Figure \[correlation\] plots the different automatic paraphrase scores
against the 5-point human judgments for four different ways of ranking
the paraphrases: 1) the original paraphrase probability defined by , 2)
the heuristic ranking that defined for PPDB 1.0, 3) the cosine
similarity of word2vec[^2] embeddings[^3], and 4) the new score
predicted by our discriminative model. The paraphrase probability has a
Spearman correlation of 0.41. The heuristic PPDB 1.0 ranking has a
similar correlation of $$\rho=0.41$$. The word2vec similarity improves
correlation slightly to 0.46. To test our supervised method, we use
cross validation: in each fold, we hold out 200 phrases along with all
of their associated paraphrases for testing. Our rankings for PPDB 2.0
dramatically improve correlation with human judgments to $$\rho=0.71$$.

#### Goodness of the top-ranked paraphrases

In addition to calculating the correlation over the sample of
paraphrases (where the human judgments were taken evenly over the range
of $$p(e_2|e_1)$$ values), we also evaluated the full list of paraphrases
as it is likely to be used by researchers who use PPDB. We took a sample
of 100 unique phrase types from Wikipedia (constraining to types which
appear in PPDB), and collected human judgments for their full list of
paraphrases.






We compare the ranking produced by the proposed PPDB 2.0 model against
the heuristic PPDB 1.0 ranking in terms of each one’s ability to put
good paraphrases at the top of its list. Figure \[prcurve\] shows
precision curves for the ranked paraphrases in PPDB 1.0 compared to PPDB
2.0. PPDB 2.0 achieves consistently higher precision, improving P@1 by
17 points and P@5 by 9 points.

We also analyzed the different rankings when we varied the criterion
that we used for what constitutes a good paraphrase. Table \[results\]
shows how the averaged precision (AP) and the mean reciprocal rank (MRR)
change as we vary the human score for good paraphrases from $$\geq$$3 to
$$\geq$$4.5. Depending on the threshold, our PPDB 2.0 ranking achieves a
9-12 point improvement in MRR over the PPDB 1.0 rankings. Similarly, it
improves AP by 7-9 points.

Other Additions
===============

In addition to dramatically improving the rankings of the paraphrases
(novel to this publication), our PPDB 2.0 release adds several automatic
annotations created in other research. Every paraphrase pair now has an
entailment relation from , style classifications from , and associated
vector embedding from . These are described briefly below.

Entailment relations
--------------------

Although we typically think of paraphrases as equivalent or as
bidirectionally entailing, a substantial fraction of the phrase pairs in
PPDB exhibit different entailment relations. Figure \[berries\] gives an
example of how these relations capture the range or entailment present
in the paraphrases of *berries*. We automatically annotate each
paraphrase rule in PPDB with an explicit entailment relation based on
*natural logic* @maccartney:thesis. These relations include forward
entailment/hyponym ($$\sqsubset$$), reverse entailment/hypernym
($$\sqsupset$$), non-entailing topical relatedness ($$\sim$$), unrelatedness
($$\#$$), and even exclusion/contradiction ($$\neg$$). For a complete
evaluation of the entailment classifications, and the prevalence of each
type in PPDB, see .

Style scores
------------

Some of the variation within paraphrase sets can be attributed to
stylistic variations of language. We automatically induce style
information on each rule in PPDB for two dimensions– complexity and
formality. Table \[style\] shows some paraphrases of *the end*, sorted
from most complex to most simple using these scores. These
classifications could be useful for natural language generation tasks
like text simplification @xu2015problems. A complete evaluation of these
scores is given in .

<!--
  ---------------------- --------------------- -------------------------
  1\. the finalization   6\. the latter part   11\. the final analysis
  2\. the expiration     7\. termination       12\. the last
  3\. the demise         8\. goal              13\. the finish
  4\. the completion     9\. the close         14\. the final part
  5\. the closing        10\. late             15\. the last part
  ---------------------- --------------------- -------------------------

  : Some paraphrases of *the end*, ranked from most complex to most
  simple according to the style scores included in PPDB 2.0.
-->




Multiview LSA vector embeddings {#multiviewLSA}
-------------------------------

Recently there has been tremendous interest in representing words via
vector embeddings @Dhillon2011NIPS
[@mikolov2013efficient; @pennington2014glove]. Such representations can
be used to measure word and phrase similarity, possibly to improve
paraphrasing. Multiview Latent Semantic Analysis (MVLSA) is a
state-of-the-art method for modeling word similarities. MVLSA can
incorporate an arbitrary number of data views, such as monolingual
signals, bilingual signals, and even signals from other embeddings. PPDB
2.0 contains new similarity features based on MVLSA embeddings for all
phrases. A complete discussion is given in .



Related Work {#relatedwork}
============

The most closely related work to our supervised re-ranking of PPDB is
work by and . improved ’s paraphrase probability by converting it into
log-linear model inspired by machine translation, allowing them to
incorporate a variety of features. developed a similar model trained on
human judgements. Both efforts apply their model to natural language
generation by paraphrasing full sentences. We apply our model to the
sub-sentential paraphrases directly, in order to improve the quality of
the Paraphrase Database.

Also related is work by which reranked bilingually-extracted paraphrases
using monolingual distributional similarities, but did not use a
supervised model. Work that is relevant to our classification of
semantic entailment types to each paraphrase, includes learning
directionality of inference rules @bhagat2007ledir
[@berant-dagan-goldberger:2011:ACL-HLT2011] and learning hypernyms
rather than paraphrases @snow2004learning. Our style annotations are
related to ’s efforts at learning stylistic paraphrases. Our word
embeddings additions to the paraphrase database are related to many
current projects on that topic, including projects that attempt to
customize embeddings to lexical resources @faruqui2015retrofitting.
However, the embeddings included here were shown to be state-of-the art
in predicting human judgements.

Conclusion
==========

We release PPDB 2.0 (<http://paraphrase.org/#/download>). The resource
includes dramatically improved paraphrase rankings, explicit entailment
relations, style information, and state-of-the-art distributional
similarity measures for each paraphrase rule. The 2.0 release contains
100m+ paraphrases, and 26k manually rated phrase pairs, which will
facilitate further research in modeling semantic similarity.

Acknowledgements 
================

This research was supported by the Allen Institute for Artificial
Intelligence (AI2), the Human Language Technology Center of Excellence
(HLTCOE), and by gifts from the Alfred P. Sloan Foundation, Google, and
Facebook. This material is based in part on research sponsored by the
NSF under grant IIS-1249516 and DARPA under agreement number
FA8750-13-2-0017 (the DEFT program). The U.S. Government is authorized
to reproduce and distribute reprints for Governmental purposes. The
views and conclusions contained in this publication are those of the
authors and should not be interpreted as representing official policies
or endorsements of DARPA or the U.S. Government.

We would like to thank the anonymous reviewers for their thoughtful
comments.

[^1]: The name LHS is due to the fact that the syntactic category comes
    from the lefthand side of the synchronous CFG rule used to produce
    the paraphrase.

[^2]: <https://code.google.com/p/word2vec/>

[^3]: For phrases, we use the vector of the rarest word as an
    approximation of the vector for the phrase.
