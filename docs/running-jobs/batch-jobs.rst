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

  - _minutes_

  - _minutes:seconds_

  - _hours:minutes:seconds_

  - _days-hours_

  - _days-hours:minutes_

  - _days-hours:minutes:seconds_

- [``mem``]: maximum amount of memory (integer) to allocate to each node
  
  - kilobyes: _K_

  - megabyes: _M_

  - gigabytes: _G_

  - terabytes: _T_

- [``/path/to/``][``jobname``]: parent directory and filename of which to print standard error and output

- [``mailtype``]: events for which to send notifications via email
  
   - _NONE_

   - _BEGIN_

   - _END_

   - _FAIL_

   - _REQUEUE_

   - _ALL_ (BEGIN, END, FAIL, REQUEUE, STAGE_OUT)

   - _STAGE_OUT_

   - _TIME_LIMIT_

   - _TIME_LIMIT_90_

   - _TIME_LIMIT_80_

   - _TIME_LIMIT_50_

   - *ARRAY_TASKS*

- [``username``]: email address before the "@" to send the notifications specified in [``mailtype``]

Example
-------


.. Slurm documentation: https://slurm.schedmd.com/sbatch.html
