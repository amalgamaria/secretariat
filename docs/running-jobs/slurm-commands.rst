Slurm commands
==============

.. attention:: For a full list of commands, see the `Slurm documentation`_.

sbatch
------

Consider the example script from the `Batch jobs`_ page:

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
   # Note: This example is for single-end data
   for f in *.fq.gz
   do
      prefix=$(echo ${f} | cut -f1-3 -d'_')

      fastp \
         -i ${dir_in}/${f} \
         -o ${dir_out}/${prefix}.out
   done

   # Unload software
   module unload fastp/0.21.0

Say that we saved this code to a file named ``fastp_ex.sh``. We would then submit the script by running the following commands from the command line:

.. code-block:: bash

   cd /path/to/fastp_ex.sh
   sbatch fastp_ex.sh

The ``sbatch`` command submits the script to Slurm, which allocates the appropriate resources (specified in the ``sbatch`` header of the script) from Secretariat to complete the job. Once successfully submitted, the job is assigned a job ID.

The following message should print to the terminal window:

.. code-block:: bash

   Submitted batch job [job_id_number]

where [``job_id_number``] is a number greater than or equal to 1.

squeue
------

To review all of the currently submitted jobs, their IDs, and other information, run the ``squeue`` command from the command line. This command will output a table with the following header:

+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+
| **JOBID** | **PARTITION** | **NAME**  | **USER** | **ST** | **TIME**   | **NODES** | **NODELIST(REASON)** |
+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+

where

	- ``JOBID``: ID number assigned to job
	- ``PARTITION``: partition to which job has been assigned
	- ``NAME``: name of job specified in ``sbatch`` header with ``--job-name``
	- ``USER``: username of the user who submitted the job
	- ``ST``: status of job (for more information, see the `Squeue status codes`_ page)
	- ``TIME``: amount of time the job has been running
	- ``NODES``: number of unique nodes that the job is assigned to
	- ``NODELIST(REASON)``: node(s) the job is assigned to

scancel
-------

If you need to terminate a specific job before it has completed, run the following from the command line:

.. code-block:: bash

   scancel [job_id_number]

If you need to terminate all of your currently submitted jobs, run the following from the command line:

.. code-block:: bash

   scancel -u [username]

where [``username``] is your username.

.. attention:: Do not include the brackets ("[" and "]") when substituting your ``job_id_number`` and ``username``.

.. _Slurm documentation: https://slurm.schedmd.com/man_index.html
.. _Batch jobs: https://secretariat.readthedocs.io/en/latest/running-jobs/batch-jobs.html#example
.. _Squeue status codes: https://secretariat.readthedocs.io/en/latest/running-jobs/squeue-status-codes.html#squeue-status-codes
