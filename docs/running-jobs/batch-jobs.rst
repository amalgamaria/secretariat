Batch jobs
==========

It is important to be careful when requesting resources on Secretariat. If you request more than what you actually need, this could stall other users waiting for resources to become available. If you are unsure about how much you should allocate for your job, please consult with `Vijay`_ or `Maria`_.

A common way of running an analysis on Secretariat is to run your command(s) / script(s) from within an "``sbatch`` script." This method allows the user to request specific resources from within the script rather than typing them out on the command line. Since Secretariat's resources are managed by `Slurm`_, resource requests must be denoted in what is called an ``sbatch`` header.

Template
--------

Here is a template of how to declare Slurm parameters in the header of an ``sbatch`` script. This information should be placed at the top of the script that you will be submitting to Secretariat. After creating this script, save it as ``[jobname].sh``.

.. code-block:: bash
   :emphasize-lines: 1,2,3,4,5,6,7

   #!/bin/bash
   #
   #SBATCH --job-name=[jobname]
   #SBATCH --cpus-per-task=[cpus]
   #SBATCH --partition=[partition]
   #SBATCH --time=[time]
   #SBATCH --mem=[mem]
   #SBATCH --output=[/path/to/][jobname].%j.out
   #SBATCH --error=[/path/to/][jobname].%j.err
   #SBATCH --mail-type=[mailtype]
   #SBATCH --mail-user=[username]@clemson.edu

*Note*: At the least, please set the parameters for the highlighted lines. The only line that is absolutely required is the first: ``#!/bin/bash``.  The unhighlighted options may be helpful for organizational purposes, but are optional. Please see the `Slurm documentation`_ for a full list of possible ``sbatch`` header options.

**Explanation**:

- [``jobname``]: name that will be assigned to a job within Secretariat

- [``cpus``]: number (integer) of CPUs to allocate to a job

- [``partition``]: name of partition to which job will be submitted

- [``time``]: maximum amount of time to allocate to a job

   - *minutes*
   - *minutes:seconds*
   - *hours:minutes:seconds*
   - *days-hours*
   - *days-hours:minutes*
   - *days-hours:minutes:seconds*

- [``mem``]: maximum amount of memory (integer) to allocate to each node

   - kilobyes: *K*
   - megabyes: *M*
   - gigabytes: *G*
   - terabytes: *T*

- [``/path/to/``][``jobname``]: parent directory and filename of which to print standard error and output

- [``mailtype``]: events for which to send notifications via email

   - *NONE*
   - *BEGIN*
   - *END*
   - *FAIL*
   - *REQUEUE*
   - *ALL* (BEGIN, END, FAIL, REQUEUE, STAGE_OUT)
   - *STAGE_OUT*
   - *TIME_LIMIT*
   - *TIME_LIMIT_90*
   - *TIME_LIMIT_80*
   - *TIME_LIMIT_50*
   - *ARRAY_TASKS*

- [``username``]: email address before the "@" to send the notifications specified in [``mailtype``]


Example
-------

Here is an example of an `sbatch` header for a script to run `AfterQC`_.

.. code-block:: bash

   #!/bin/bash
   #
   #SBATCH --job-name=afterqc_ex
   #SBATCH --cpus-per-task=1
   #SBATCH --partition=compute
   #SBATCH --time=00:30:00
   #SBATCH --mem=2G
   #SBATCH --output=/opt/ohpc/pub/workshop/toyout/logs/afterqc_ex.%j.out
   #SBATCH --error=/opt/ohpc/pub/workshop/toyout/logs/afterqc_ex.%j.err
   #SBATCH --mail-type=all
   #SBATCH --mail-user=madonay@clemson.edu
   
   module load afterqc/0.9.7
   
   mkdir -p /opt/ohpc/pub/workshop/toyout/afterqc
   cd /opt/ohpc/pub/workshop/toysets/fastq
   
   after.py \
      -g /opt/ohpc/pub/workshop/toyout/afterqc/pass \
      -b /opt/ohpc/pub/workshop/toyout/afterqc/fail \
      -r /opt/ohpc/pub/workshop/toyout/afterqc/QC

**Explanation**:

This script sets up a job named **afterqc_ex** to execute the python script **after.py**. This script allocates **2 CPUs** on one or two of the **compute** nodes with up to **2 GB of memory** and no more than **30 minutes of runtime** to complete this job. Standard error and output will be outputted to separate files in **/opt/ohpc/pub/workshop/tmp/logs** and the email address **madonay@clemson.edu** will receive notifications when the job **begins** and if it **ends**, **fails**, **requeues**, or **stages out**.

*Note*: To actually submit this script to Secretariat, please refer to the `Slurm commands`_ tab.

Jobs and nodes and tasks, oh my! 
--------------------------------

When allocating resources to jobs, particularly with respect to nodes and CPUs, there may be more than one way to accomplish the same result. This is due to the relationship between ``--nodes``, ``--ntasks-per-node``, ``--cpus-per-task``, and ``--ntasks``.

- ``--nodes``: number of nodes to be allocated to a job

- ``--ntasks-per-node``: number of tasks to be allocated per node

- ``--cpus-per-task``: number of CPUs to allocate per task

- ``--ntasks``: maximum number of tasks to allocate to a job

*Note*: All of these values must be integers.

Amended from the example on the `Slurm FAQ`_ page, suppose you need to allocate 4 CPUs to a particular job. There are a variety of ways to request 4 CPUs, and depending on the job, one method might be preferable. Here are some examples.

+-----------------------------------------------------------------------+---------------------------------------------------------------+
| Slurm paramaters							| Interpretation						|
+=======================================================================+===============================================================+
| ``--ntasks=4``							| 4 independent processes					|
+-----------------------------------------------------------------------+---------------------------------------------------------------+
| ``--ntasks=4 --ntasks-per-node=1`` **or** ``--ntasks=4 --nodes=4``	| 4 processes with 1 CPU each, spread across 4 distinct nodes	|
+-----------------------------------------------------------------------+---------------------------------------------------------------+
| ``--ntasks=4 --ntasks-per-node=2``					| 4 processes spread across 2 nodes				|
+-----------------------------------------------------------------------+---------------------------------------------------------------+
| ``--ntasks=4 --ntasks-per-node=4``					| 4 processes on the same node					|
+-----------------------------------------------------------------------+---------------------------------------------------------------+
| ``--ntasks=1 --cpus-per-task=4``					| 1 process with up to 4 CPUs for multithreading		|
+-----------------------------------------------------------------------+---------------------------------------------------------------+
| ``--ntasks=2 --cpus-per-task=2``					| 2 processes with up to 2 CPUs for multithreading		|
+-----------------------------------------------------------------------+---------------------------------------------------------------+

*Note*: Know your software! Make sure that the software within your script supports multiple CPU usage before requesting resources that allow for multithreading.

.. _Vijay: https://scienceweb.clemson.edu/chg/dr-vijay-shankar-2/
.. _Maria: https://scienceweb.clemson.edu/chg/maria-adonay/
.. _Slurm: https://slurm.schedmd.com/documentation.html
.. _Slurm documentation: https://slurm.schedmd.com/sbatch.html
.. _AfterQC: https://github.com/OpenGene/AfterQC
.. _Slurm commands: https://secretariat.readthedocs.io/en/latest/running-jobs/slurm-commands.html
.. _Slurm FAQ: https://support.ceci-hpc.be/doc/_contents/SubmittingJobs/SlurmFAQ.html
