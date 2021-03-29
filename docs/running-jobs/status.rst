Squeue status codes
===================

If you were to run the command ``squeue`` from the command line, a table similar to the one below would be printed to your screen.

+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+
| **JOBID** | **PARTITION** | **NAME**  | **USER** | **ST** | **TIME**   | **NODES** | **NODELIST(REASON)** |
+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+
| 1         | compute       | jobname_1 | username | R      | 5:42       | 1         | compute001           |
+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+
| 2         | compute       | jobname_2 | username | PD     | 0:00       | 1         | compute001           |
+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+
| 3         | bigmem        | jobname_3 | username | CG     | 1-12:18:03 | 1         | bigmem002            |
+-----------+---------------+-----------+----------+--------+------------+-----------+----------------------+

The status codes are found in the "ST" (status) column. Although the three above are the ones that you are likely to see the most often, there are others (please see `this document`_ for more details).

**Description of each code:**

Job 1.	: *R*

	The job is **R**\ unning.

Job 2.	: *PD*

	The job is **P**\ en\ **D**\ ing. This means that it is waiting on sufficient resources to run. "Sufficient resources" are determined by the user at the submission of the job. If the user does not make any specifications at job submission, the default resource settings are used. Once sufficient resources are available, the status will change to *R*.

Job 3.	: *CG*

	The job is **C**\ ompletin\ **G**. The job should finish shortly and disappear from the ``squeue`` table.


.. _this document: https://curc.readthedocs.io/en/latest/running-jobs/squeue-status-codes.html
