CHG-BSL worshops
################

You will find information about currently-offered CHG Bioinformatics and Statistics Laboratory (BSL) workshops below.

HPCC Basics Workshop
--------------------

**Frequency**: Fall (~September) and Spring (~February).

**Location**: CHG, Greenwood, SC (remote option possible).

**Pre-course**: Note that attendees must have a Secretariat account to attend the HPCC Basics Workshop. This workshop does not give an introduction to Linux: Before attending, it is preferred that users know some command line basics and feel comfortable navigating around a virtual computing environment using commands (e.g. `those mentioned in this tutorial`_). 

The HPCC Basics Workshop is divided into 3 parts, so participants must attend all 3 sessions! It is recommended that all Secretariat users attend this workshop. The goal of this workshop is for users to understand how to use Secretariat, the CHG HPC, effectively. Topics will include many of the items discussed in the Secretariat Documentation as well as some others, described below.

**Day 1**: Users will learn about Secretariat's architecture (partitions, nodes, cores, RAM) so that they can request appropriate resources for their analyses. Instructors will ensure that users can log into the cluster from the command line. Users will learn how to gather user-specific information from the command line prompt and how to use basic Unix commands to navigate around the directory structure. Instructors will advise users on where to store / access different types of data. Users will learn about the significance of file / directory permissions (read, write, execute) and how to be intentional about setting permissions for different purposes.

**Day 2**: Users will practice transferring data between local (laptop) and remote (Secretariat) machines using command line and graphical user interface methods. Instructors will emphasize the importance of maintaining a data backup plan. Instructors will explain how to access software via a module system, how to list currently available modularized software, and when it is necessary to load software. Users will also learn how to install software when it is not already installed on the cluster through a variety of methods and how to create a module file from software installed from source.

**Day 3**: Instructors will give recommendations on how to organize a project directory before beginning an analysis. Instructors will explain how Slurm handles job submissions, walk users through the general layout of an SBATCH script, and demonstrate several Slurm commands (squeue, sbatch, srun, sinfo, scontrol, scancel). Users will learn how to create interactive sessions and instructors will demonstrate how to estimate cluster resources needed for a job by scaling down the analysis, and monitoring it in real time and / or afterwards, and looking at stats that Slurm collects. Instructors will demonstrate how to connect to Secretariat via Open OnDemand (https://secretariat-master) and give a tour of the interface.

**Tags**: Cluster resources, Login, Workspace navigation, Permissions, Data transfer, Software accession, Software installation, Job submission, Cluster etiquette

Git & GitHub Workshop
---------------------

**Frequency**: Fall (~October) and Spring (~March).

**Location**: CHG, Greenwood, SC (remote option possible).

**Pre-course**: Note that the CHG-BSL HPCC Basics Workshop is currently treated as a pre-requisite for the Git & GitHub Workshop. Before the workshop, users will need to install and test the Git software client, create a GitHub account, and set up SSH keys for authentication. Instructors will provide instructions for these tasks to attendees.

The Git & GitHub Workshop is divided into 2 parts, so participants must attend all 2 sessions! The Git & GitHub Workshop gives explanation of version control and motivates the many ways Git and GitHub are useful tools for bioinformaticians and users of bioinformatic tools and pipelines in general!

**Topics**:

**Basic Worflow**: Users will configure Git and learn the basic steps for local version control. This section covers required and common configuration options and the routine commands to add, manipulate, retrieve, and monitor the status of a local Git repository.

**GitHub**: Instructors will explain the relationship between GitHub and Git, how to link local and remote repos, and the role of collaboration and backup. This section gives an overview of the features provided by the GitHub web portal for open source projects as well as approaches to starting new projects and version controlling existing projects.

**History**: Instructors will demonstrate how Git can be used to search an annotated history of the project to identify what changes were made and retrieve previous versions of code exactly as they were saved.

**Branching**: Instructors will discuss the rationale for branches as well as how to create them, switch between them, and incorporate changes from one into another (merging). This section emphasizes the power of branching during development and demystifies how Git works.

**Merging and Merge Conflicts**: Users will learn how to incorporate changes and how to handle this process when intervention is necessary.

**Fixing Errors**: Instructors will go over the concept of "re-writing history" and emphasize when this is appropriate and when it should be avoided to prevent common "broken repo" scenarios. Uses will practice several methods to remove errors.

**Best Practices**: Users will learn ways to make their Git and GitHub experience as simple as possible by avoiding the problems which often frustrate new users, especially when actively collaborating.

**Resources**: Instructors will provide a condensed list of curated resources particularly suited to new users covering basic, intermediate, and advanced topics. The goal is to provide a clear, concise, and easy to navigate set of references and tutorials to assist users easily expand their Git skills as their needs and experience grow.

RNA-Seq Retreat
---------------

< TBA >

.. _those mentioned in this tutorial: https://www.chm.bris.ac.uk/unix/unix1.html
