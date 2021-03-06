Batch jobs
==========

A common way of running an analysis on Secretariat is to run your command(s) / script(s) from within an "*sbatch* script." This method allows the user to request specific resources from within the script rather than typing them out on the command line. Since Secretariat's resources are managed by `Slurm`_, resource requests must be denoted in what is called an *sbatch* header.

.. attention:: It is important to be careful when requesting resources on Secretariat. If you request more than what you actually need, this could stall other users waiting for resources to become available. If you are unsure about how much you should allocate for your job, please consult with `Vijay`_ or `Maria`_.

Template
--------

Here is a template of how to declare Slurm parameters in the header of an *sbatch* script. This information should be placed at the top of the script that you will be submitting to Secretariat. After creating this script, save it as *[jobname].sh*.

*Note*: Please see the `FAQ`_ page for information on creating / editing files on Secretariat.

.. code-block:: bash
   :linenos:

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

.. attention:: At the least, please set the parameters for lines 1-7. The only line that is absolutely required is the first: ``#!/bin/bash``.  Lines 8-11 may be helpful for organizational purposes, but are optional. Please see the `Slurm documentation`_ for a full list of possible *sbatch* header options.

**Explanation**:

- [``jobname``]: name that will be assigned to a job within Secretariat

- [``cpus``]: number (positive `integer`_) of CPUs to allocate to a job

- [``partition``]: name of partition to which job will be submitted

- [``time``]: maximum amount of time to allocate to a job

   - *minutes*
   - *minutes:seconds*
   - *hours:minutes:seconds*
   - *days-hours*
   - *days-hours:minutes*
   - *days-hours:minutes:seconds*

- [``mem``]: maximum amount of memory (positive `integer`_) to allocate to each node

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

Here is an example of an *sbatch* header for a script to run `fastp`_.

.. code-block:: bash
   :linenos:

   #!/bin/bash
   #
   #SBATCH --job-name=fastp_ex
   #SBATCH --cpus-per-task=1
   #SBATCH --partition=compute
   #SBATCH --time=00:30:00
   #SBATCH --mem=2G
   #SBATCH --output=/opt/ohpc/pub/workshop/toyout/logs/fastp_ex.%j.out
   #SBATCH --error=/opt/ohpc/pub/workshop/toyout/logs/fastp_ex.%j.err
   #SBATCH --mail-type=all
   #SBATCH --mail-user=madonay@clemson.edu

   # Load software   
   module load fastp/0.21.0
   
   # Save directories as variables
   export dir_in="/opt/ohpc/pub/workshop/toysets/fastq/dnaseq"
   export dir_out="/opt/ohpc/pub/workshop/toyout/fastp"

   # Prepare directories
   mkdir -p ${dir_out}
   cd ${dir_in}
   
   # Execute function for each fastq file
   # Note: This example is for paired-end data
   for r1 in *_R1_001.fastq.gz
   do
      r2="$(echo ${r1} | sed -e 's/R1/R2/')"
      prefix="$(echo ${r1} | cut -f1-3 -d'_')"

      fastp \
         -in1 ${dir_in}/${r1} \
         -in2 ${dir_in}/${r2} \
       	 -out1 ${dir_out}/${prefix}_R1.out \
       	 -out2 ${dir_out}/${prefix}_R2.out \
       	 --json ${dir_out}/${prefix}.json \
       	 --html ${dir_out}/${prefix}.html
   done
   
   # Unload software
   module unload fastp/0.21.0

**Explanation**:

This script sets up a job named **fastp_ex** to execute the function **fastp**. This script allocates **1 CPU** on a **compute** node (compute[001-004]) with up to **2 GB of memory** and no more than **30 minutes of runtime** to complete this job. Standard error and output will be outputted to separate files in **/opt/ohpc/pub/workshop/tmp/logs** and the email address **madonay@clemson.edu** will receive notifications when the job **begins** and if it **ends**, **fails**, **requeues**, or **stages out**.

.. attention:: To actually submit this script to Secretariat, please refer to the `Slurm commands`_ tab.

Jobs and nodes and tasks, oh my! 
--------------------------------

When allocating resources to jobs, particularly with respect to nodes and CPUs, there may be more than one way to accomplish the same result. This is due to the relationship between ``--nodes``, ``--ntasks-per-node``, ``--cpus-per-task``, and ``--ntasks``.

- ``--nodes``: number of nodes to be allocated to a job

- ``--ntasks-per-node``: number of tasks to be allocated per node

- ``--cpus-per-task``: number of CPUs to allocate per task

- ``--ntasks``: maximum number of tasks to allocate to a job

.. attention:: All of these values must be positive `integers`_.

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

.. attention:: Know your software! Make sure that the software within your script supports multiple CPU usage before requesting resources that allow for multithreading.


.. _Vijay: https://scienceweb.clemson.edu/chg/dr-vijay-shankar-2/
.. _Maria: https://scienceweb.clemson.edu/chg/maria-adonay/
.. _FAQ: https://secretariat.readthedocs.io/en/latest/faq.html#how-do-i-create-edit-files-on-secretariat
.. _Slurm: https://slurm.schedmd.com/documentation.html
.. _Slurm documentation: https://slurm.schedmd.com/sbatch.html
.. _integer: https://en.wikipedia.org/wiki/Integer
.. _fastp: https://github.com/OpenGene/fastp
.. _Slurm commands: https://secretariat.readthedocs.io/en/latest/running-jobs/slurm-commands.html
.. _integers: https://en.wikipedia.org/wiki/Integer
.. _Slurm FAQ: https://support.ceci-hpc.be/doc/_contents/SubmittingJobs/SlurmFAQ.html
