CHG-BSL worshops
################

You will find information about currently-offered CHG Bioinformatics and Statistics Laboratory (BSL) workshops below.

HPCC Basics Workshop
--------------------

**Frequency**: Fall (~September) and Spring (~February).

**Location**: CHG, Greenwood, SC (remote option possible).

**Pre-course**: Note that attendees must have a Secretariat account to attend the HPCC Basics Workshop. This workshop does not give an introduction to Linux: Before attending, it is preferred that users know some command line basics and feel comfortable navigating around a virtual computing environment using commands (e.g. `those mentioned in this tutorial`_). 

The HPCC Basics Workshop is divided into 3 parts, so participants must attend all 3 sessions! It is recommended that all Secretariat users attend this workshop. The goal of this workshop is for users to understand how to use Secretariat, the CHG HPC, effectively. Topics will include many of the items discussed in the `Secretariat Documentation`_ as well as some others, described below.

**Topics**:

- **Day 1**
   
   - **Cluster resources**: Users will learn about Secretariat's architecture (partitions, nodes, cores, RAM) so that they can request appropriate resources for their analyses.
   
   - **Login**: Instructors will ensure that users can log into the cluster from the command line.
   
   - **Workspace navigation**: Users will learn how to gather user-specific information from the command line prompt and how to use basic Unix commands to navigate around the directory structure. Instructors will advise users on where to store / access different types of data.
   
   - **Permissions**: Users will learn about the significance of file / directory permissions (read, write, execute) and how to be intentional about setting permissions for different purposes.

- **Day 2**
   
   - **Data transfer**: Users will practice transferring data between local (laptop) and remote (Secretariat) machines using command line and graphical user interface methods. Instructors will emphasize the importance of maintaining a data backup plan.
   
   - **Software accession**: Instructors will explain how to access software via a module system, how to list currently available modularized software, and when it is necessary to load software.
   
   - **Software installation**: Users will learn how to install software when it is not already installed on the cluster through a variety of methods and how to create a module file from software installed from source.

- **Day 3**
   
   - **Job submission**: Instructors will give recommendations on how to organize a project directory before beginning an analysis. Instructors will explain how Slurm handles job submissions, walk users through the general layout of an SBATCH script, and demonstrate several Slurm commands (squeue, sbatch, srun, sinfo, scontrol, scancel).
   
   - **Cluster etiquette**: Users will learn how to create interactive sessions and instructors will demonstrate how to estimate cluster resources needed for a job by scaling down the analysis, and monitoring it in real time and / or afterwards, and looking at stats that Slurm collects.
   
   - **Resources**: Instructors will demonstrate how to connect to Secretariat via Open OnDemand (https://secretariat-master) and give a tour of the interface.

Git & GitHub Workshop
---------------------

**Frequency**: Fall (~October) and Spring (~March).

**Location**: CHG, Greenwood, SC (remote option possible).

**Pre-course**: Note that the CHG-BSL HPCC Basics Workshop is currently treated as a pre-requisite for the Git & GitHub Workshop. Before the workshop, users will need to install and test the Git software client, create a GitHub account, and set up SSH keys for authentication. Instructors will provide instructions for these tasks to attendees.

The Git & GitHub Workshop is divided into 2 parts, so participants must attend all 2 sessions! The Git & GitHub Workshop gives explanation of version control and motivates the many ways Git and GitHub are useful tools for bioinformaticians and users of bioinformatic tools and pipelines in general.

**Topics**:

- **Day 1**
   
   - **Basic Worflow**: Users will configure Git and learn the basic steps for local version control. This section covers required and common configuration options and the routine commands to add, manipulate, retrieve, and monitor the status of a local Git repository.
   
   - **GitHub**: Instructors will explain the relationship between GitHub and Git, how to link local and remote repos, and the role of collaboration and backup. This section gives an overview of the features provided by the GitHub web portal for open source projects as well as approaches to starting new projects and version controlling existing projects.
   
   - **History**: Instructors will demonstrate how Git can be used to search an annotated history of the project to identify what changes were made and retrieve previous versions of code exactly as they were saved.

- **Day2**
   
   - **Branching**: Instructors will discuss the rationale for branches as well as how to create them, switch between them, and incorporate changes from one into another (merging). This section emphasizes the power of branching during development and demystifies how Git works.
   
   - **Merging and Merge Conflicts**: Users will learn how to incorporate changes and how to handle this process when intervention is necessary.
   
   - **Fixing Errors**: Instructors will go over the concept of "re-writing history" and emphasize when this is appropriate and when it should be avoided to prevent common "broken repo" scenarios. Uses will practice several methods to remove errors.
   
   - **Best Practices**: Users will learn ways to make their Git and GitHub experience as simple as possible by avoiding the problems which often frustrate new users, especially when actively collaborating.
   
   - **Resources**: Instructors will provide a condensed list of curated resources particularly suited to new users covering basic, intermediate, and advanced topics. The goal is to provide a clear, concise, and easy to navigate set of references and tutorials to assist users easily expand their Git skills as their needs and experience grow.

RNA-Seq Retreat
---------------

**Frequency**: Summer (July).

**Location**: Clemson University Roy Muldrow Cooper Library, Clemson, SC.

**Pre-course**: Basic Unix/Linux command line skills are recommended. Access to Secretariat (CHG HPC) is currently required. Future iterations could be modified use Palmetto, so access to either HPC environment will be a pre-requisite.

The RNA-Seq Retreat is divided into 3 parts, so participants must attend all 3 sessions! Although focused on the analysis portion, this retreat gives a comprehensive overview of transcriptomic studies, beginning with experimental design.

**Topics**:

- **Day 1**

   - **Background**: Attendees will be introduced to some basic concepts such as the definition and constituents of a transcriptome, its basic properties, diversity and expression potential, and ribosomal RNA removal strategies.
   
   - **Experimental Design**: Hypothesis testing using transcriptome data will be addressed from a factorial design perspective. Strategies to handle variable confoundedness and block effects will also be discussed. Data-driven gold standards for replication and sequencing depth requirements will be presented and discussed.
   
   - **Quality Control**: Attendees will be presented with currently-recommended strategies for quality control of whole transcriptome data. They will also practice basic quality control steps such as adapter removal, length filtering, per-based quality filtering, and rRNA filtering using pre-designed pipelines and tools.
   
   - **Alignment and Processing**: The means of identifying and acquiring reference genome resources, basic concepts of sequencing data alignment to reference genome and the properties of the alignment intermediary files and methods to visualized feature alignments and assess quality issues will be presented and explored.
   
   - **Feature Quantification**: Attendees will be introduced to strategies for quantification based on transcriptome features such as gene, transcript isoform, exon and transposon. Acquisition, construction, and manipulation of gene models (GTF) will also be discussed.
   
- **Day 2**

   - *De Novo* **Transcriptomics**: Alternative strategies to a reference-based transcriptome analysis will be presented and discussed. Attendees will also practice the *de novo* pipeline steps which includeassembly, clustering, annotation, and assessment.
   
   - **Normalization**: Means to correct for technical variation in feature quantification as well as commonly utilized strategies will be discussed and explored. The consequences and affinities of different normalization methods will also be introduced and explained.
   
   - **Statistical Modeling**: The concept of differential expression will be described from a statistical modeling perspective. Critical ideas such as conditional means, distribution properties and centrality, dispersion, model parametrization, mean-variance relationships, and statistical tests will be discussed.

- **Day 3**
   
   - **Gene Set Analyses**: Methods to infer functional significance and consequences from a set of genes will be covered in detail. Popular techniques such as over-representation analysis, gene set enrichment and pathway analyses will be discussed. The differences between these methods will also be explained. Attendees will be provided with the necessary tools and datasets to perform their own analyses in the HPC environment.
   
   - **Network Analyses**: Attendees will participate in the critical discussion of the different methods commonly used to represent the relationship between genes based on expression and known interactions. The performance of popular methods such as Weighted Gene Co-expression Network Analysis and Inference-based Interaction Network Analyses will be assessed by the attendees using the test dataset. Network visualization and sub-clustering will also be discussed and demonstrated.

.. _Secretariat Documentation: https://secretariat.readthedocs.io/en/latest
.. _those mentioned in this tutorial: https://www.chm.bris.ac.uk/unix/unix1.html
