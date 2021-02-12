Palmetto cluster
================

Clemson University has a high-performance computing resource called Palmetto. For more general information / specs, please see the Clemson University Palmetto Cluster's `website`_.

As a Clemson student, faculty, or staff member, you are eligible to `request an account`_ on the Palmetto cluster.

Hyperion
--------

All members of the Center for Human Genetics (CHG) may request to use our CHG-designated node on Palmetto.

+---------------+-----------------------+---------------+
| Cluster	| Compute cores (CPUs)  | RAM           |
+===============+=======================+===============+
| Palmetto      | 80                    | 1.54 TB       |
+---------------+-----------------------+---------------+

If you would like to use this resource, you need to `request an account`_. After this, please contact `Vijay`_ or `Maria`_ via the `Ticket Request Form`_ about becoming a part of our user group on Palmetto.

TORQUE vs Slurm
---------------

.. attention:: Palmetto is managed by `TORQUE`_, which means that you must submit job scripts in the *#PBS* format. This is different than Secretariat, which is managed by `Slurm`_ and processes job scripts written in the *#SBATCH* format.

To see some equivalencies between *#PBS* and *#SBATCH* script formatting, see `this documentation`_ from the `University of Michigan Information and Technology Services`_.


.. _website: https://www.palmetto.clemson.edu/palmetto/`
.. _instructions: https://www.palmetto.clemson.edu/palmetto/basic/new/
.. _request an account: https://www.palmetto.clemson.edu/palmetto/basic/new/
.. _Vijay: https://scienceweb.clemson.edu/chg/dr-vijay-shankar-2/
.. _Maria: https://scienceweb.clemson.edu/chg/maria-adonay/
.. _Ticket Request Form: https://secretariat.readthedocs.io/en/latest/tickets.html#ticket-requests
.. _TORQUE: https://adaptivecomputing.com/cherry-services/torque-resource-manager/
.. _Slurm: https://slurm.schedmd.com/overview.html
.. _this documentation: https://arc-ts.umich.edu/migrating-from-torque-to-slurm/
.. _University of Michigan Information and Technology Services: https://its.umich.edu/
