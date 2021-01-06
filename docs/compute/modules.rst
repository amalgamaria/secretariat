Software modularization
=======================

Software on Secretariat are accessed via a module system. Most of the software is not accessible unless loaded; To access the software, this must be done for each user's environment.

To see what modules are available, run ``module avail`` from the command line. This command returns a list of loadable software in the form [``software_name``]/[``version_number``].

Load / unload
-------------

To load software, run the following from the command line:

.. code-block:: bash

   module load [software_name]/[version_number]

Including the [``version_number``] portion ensures that you are loading the exact software that you would like. This is especially important if there is more than one version of the software available.

To unload software, run the following from the command line:

.. code-block:: bash

   module unload [software_name]/[version_number]

.. attention:: Do not include the brackets (“[” and “]”) when substituting your ``software_name`` and ``version_number``.

To see which software are currently loaded, run ``module list`` from the command line. This command returns a list of software that are currently loaded in the user's environment.

Within scripts
--------------

.. attention:: Software must be loaded within scripts, regardless of whether the software is currently loaded in a user's environment.

Consider these lines from the example script from the `Batch jobs`_ page:
               
.. code-block:: bash
   :lineno-start: 13

   # Load software
   module load fastp/0.21.0

If the lines above were not included in the script and the user had run the following commands, the job would not have completed successfully:

.. code-block:: bash

   module load fastp/0.21.0
   sbatch fastp_ex.sh

.. _Batch jobs: https://secretariat.readthedocs.io/en/latest/running-jobs/batch-jobs.html#example
