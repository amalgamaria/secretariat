Software modularization
=======================

Software on Secretariat are accessed via a module system. Most of the software are not accessible unless loaded; To access the software, this must be done for each user's environment.

To see what modules are available, run ``module avail`` from the command line. This command returns a list of loadable software in the form [*software_name*]/[*version_number*].

Load / unload
-------------

To load software, run the following from the command line:

.. code-block:: bash

   module load [software_name]/[version_number]

Including the [*version_number*] portion ensures that you are loading the exact software that you would like. This is especially important if there is more than one version of the software available.

To unload software, run the following from the command line:

.. code-block:: bash

   module unload [software_name]/[version_number]

.. attention:: Do not include the brackets (“[” and “]”) when substituting your *software_name* and *version_number*.

To see which software are currently loaded, run ``module list`` from the command line. This command returns a list of software that are currently loaded in the user's environment.

For more information about additional sub-commands, run ``module help`` from the command line. This will return a help message with detailed information about more use-cases of *module*. To learn more about this module system, read the `Lmod documentation`_.

Within scripts
--------------

.. attention:: Software must be loaded within scripts, regardless of whether the software is currently loaded in a user's environment.

Consider these lines from the example script from the `Batch jobs`_ page:
               
.. code-block:: bash
   :lineno-start: 13

   # Load software
   module load fastp/0.21.0

The pertinent software must be loaded in this manner before it / they can be used. A good place to do this is immediately after the *#SBATCH* header. Please refer to the full `example` to see software loading in context.

.. _Lmod documentation: http://lmod.readthedocs.org
.. _Batch jobs: https://secretariat.readthedocs.io/en/latest/running-jobs/batch-jobs.html#example
.. _example: https://secretariat.readthedocs.io/en/latest/running-jobs/batch-jobs.html#example
