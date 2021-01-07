================
Interactive jobs
================

.. attention:: When testing code on Secretariat, it is important that you **not** run your commands on the head node (``secretariat-master``).

When you follow the instructions on the `Logging in`_ page, you are connecting to the head node. To make sure that you are testing your code appropriately, please use one of the following options.

srun
----

To create an ``interactive session`` on Secretariat, run ``srun`` from the command line. 

Consider the ``sbatch`` header in the example script from the `Batch jobs`_ page:

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
   
When initiating your session, you must specify your resource requests in your command. Make sure that you specify parameters for the options in lines 4-7, at least:

.. code-block:: bash

   srun --cpus-per-task=1 --partition=compute --time=00:30:00 --mem=2G --pty bash

where

	- ``--pty``: instructs ``srun`` to run in "pseudo terminal mode"
	- ``bash``: creates an "interactive bash shell"\

Every option that you could include in your ``sbatch`` header should be possible to include in an ``srun`` command. Please see the `Slurm documentation`_ for more details.

sbatch
------

Say that you have written all of your commands inside a script named ``fastp_ex.sh``. When you submit the script via the command ``sbatch fastp_ex.sh``, you are submitting the script to a particular partition of Secretariat (either ``bigmem`` or ``compute``), given by the ``--partition`` option in the ``sbatch`` header of your script.

.. attention:: If you choose this method, make sure to specify all of the necessary parameters in your ``sbatch`` header. For more information, see the `Batch jobs`_ page.

.. _Logging in: https://secretariat.readthedocs.io/en/latest/access/logging-in.html#logging-in
.. _Slurm documentation: https://slurm.schedmd.com/sbatch.html
.. _Batch jobs: https://secretariat.readthedocs.io/en/latest/running-jobs/batch-jobs.html#batch-jobs
