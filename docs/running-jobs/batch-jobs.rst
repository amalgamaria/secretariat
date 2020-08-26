Batch jobs
==========

Template
--------

Here is a template of how to declare Slurm parameters in the header of an ``sbatch`` script. This information should be placed at the top of the script that you will be submitting to Secretariat. Please see the `Slurm documentation`_ for a full list of possible `sbatch` header options.

.. code-block:: bash

   #!/bin/bash
   #
   #SBATCH --job-name=[jobname]
   #SBATCH --ntasks=[cpus]
   #SBATCH --nodelist=[node]
   #SBATCH --time=[time]
   #SBATCH --mem=[mem]
   #SBATCH --output=[/path/to/][jobname].%j.out
   #SBATCH --error=[/path/to/][jobname].%j.err
   #SBATCH --mail-type=[mailtype]
   #SBATCH --mail-user=[username]@clemson.edu

Explanation:

- [``jobname``]: name that will be assigned to your job within Secretariat

- [``cpus``]: maximum number (integer) of cores / CPUs to allocate to the job

- [``node``]: name of node to which you will submit your job

- [``time``]: maximum amount of time to allocate to the job

  - minutes
  - minutes:seconds
  - hours:minutes:seconds
  - days-hours
  - days-hours:minutes
  - days-hours:minutes:seconds

- [``mem``]: maximum amount of memory (integer) to allocate to each node
  
  - kilobyes: K
  - megabyes: M
  - gigabytes: G
  - terabytes: T

- [``/path/to/``][``jobname``]: parent directory and filename of which to print standard error and output

- [``mailtype``]: events for which to send notifications via email
  
   - NONE
   - BEGIN
   - END
   - FAIL
   - REQUEUE
   - ALL (BEGIN, END, FAIL, REQUEUE, STAGE_OUT)
   - STAGE_OUT
   - TIME_LIMIT
   - TIME_LIMIT_90
   - TIME_LIMIT_80
   - TIME_LIMIT_50
   - ARRAY_TASKS

- [``username``]: email address before the "@" to send the notifications specified in [``mailtype``]

Example
-------


.. Slurm documentation: https://slurm.schedmd.com/sbatch.html
