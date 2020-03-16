Squeue status codes
===================

If you were to run the command `squeue` from the command line, a table similar to the one below would be printed to your screen.

| JOBID | PARTITION | NAME      | USER     | ST | TIME       | NODES | NODELIST(REASON) |
|-------|-----------|-----------|----------|----|------------|-------|------------------|
| 1     | compute   | jobname_1 | username | R  | 5:42       | 1     | compute001       |
| 2     | compute   | jobname_2 | username | PD | 0:00       | 1     | compute001       |
| 3     | bigmem    | jobname_3 | username | CG | 1-12:18:03 | 1     | bigmem002        |

The status codes are found in the "ST" (status) column. Although the three above are the ones that you are likely to see the most often, there are others (please see [this document](https://curc.readthedocs.io/en/latest/running-jobs/squeue-status-codes.html) for more details).

Description of each code:
*************************

Job 1.	: `R`

	The job is running.

Job 2.	: `PD`

	The job is waiting on sufficient resources to run. "Sufficient resources" are determined by the user at the submission of the job. If the user does not make any specifications at job submission, the default resource settings are used.

Job 3.	: `CG`

	The job is in the process of finishing. The status should change to `R` shortly.
