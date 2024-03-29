Computational nodes
===================

You may submit jobs to a variety of partitions and nodes on Secretariat.

.. attention:: bigmem[003-009] and compute[005-012] are under two different queues / partitions. One set of queues (Lab only) have priority over the other (all user general queues). These nodes were purchased by CHG Principal Investigators and their group members get priority over the general queues for their respective nodes’ usage. Please be aware that when placing jobs on the “gen-” queues they may get terminated with the message below when node-owner group members place their jobs on their priority queues.

The following tables include CPU and RAM information. This is with respect to each node.

General purpose
---------------

+------------------+-----------------------+------------+---------+--------------+
| Partition        | Node                  | CPUs       | GPUs    | RAM          |
+==================+=======================+============+=========+==============+
| compute          | compute[001-004]      | 40         | 0       | 188 G        |
+------------------+-----------------------+------------+---------+--------------+
| gen-mk-compute-1 | compute[005-008]      | 40         | 0       | 248 G        |
+------------------+-----------------------+------------+---------+--------------+
| gen-kw-compute-1 | compute[009-012]	   | 48         | 0	  | 1 T          |
+------------------+-----------------------+------------+---------+--------------+
| bigmem           | bigmem[001-002]       | 40         | 0       | 1.5 T        |
+------------------+-----------------------+------------+---------+--------------+
| gen-fm-bigmem-1  | bigmem[003-004]       | 56         | 0       | 1.5 T        |
+------------------+-----------------------+------------+---------+--------------+
| gen-fm-bigmem-2  | bigmem[006-007]       | 56         | 0       | 2 T          |
+------------------+-----------------------+------------+---------+--------------+
| gen-fm-bigmem-3  | bigmem[005]           | 80         | 0       | 2 T (optane) |
+------------------+-----------------------+------------+---------+--------------+
| gen-fm-bigmem-4  | bigmem[008-009]       | 128        | 0	  | 4 T          |
+------------------+-----------------------+------------+---------+--------------+
| interactive      | interactive[001-005]  | 56 or 72   | 0       | 118 or 244 G |
+------------------+-----------------------+------------+---------+--------------+
| dgx              | northern-dancer       | 256        | 8       | 2 T          |
+------------------+-----------------------+------------+---------+--------------+

PacBio sequencer
----------------

+------------------+-----------------------+-------+---------------+
| Partition        | Node                  | CPUs  | RAM           |
+==================+=======================+=======+===============+
| PBC              | compute[003-004]      | 40    | 188 G         |
+------------------+-----------------------+-------+---------------+

.. attention:: compute[003-004] also belong to another partition called PBC (do not submit jobs to this partition). Periodic, automatic data transfers from the PacBio Sequencer will be given priority and will use resources on these two compute nodes, only. Secretariat may assign jobs to these nodes when resources are requested of the compute partition, but this will only occur when they are not being used to transfer data. Likewise, you may request resources directly from compute003 and compute004; however, when your process initiates will depend on if the nodes are currently in use by the PacBio Sequencer.

Lab only
--------

+------------------+-----------------------+-------+---------------+------------------+
| Partition        | Node                  | CPUs  | RAM           | Lab              |
+==================+=======================+=======+===============+==================+
| mk-compute-1     | compute[005-008]      | 40    | 248 G         | `Konkel`_        |
+------------------+-----------------------+-------+---------------+------------------+
| kw-compute-1     | compute[009-012]	   | 48    | 1 T           | `Witt Dillon`_   |
+------------------+-----------------------+-------+---------------+------------------+
| fm-bigmem-1      | bigmem[003-004]       | 56    | 1.5 T         | `Morgante`_      |
+------------------+-----------------------+-------+---------------+------------------+
| fm-bigmem-2      | bigmem[006-007]       | 56    | 2 T           | `Morgante`_      |
+------------------+-----------------------+-------+---------------+------------------+
| fm-bigmem-3      | bigmem[005]           | 80    | 2 T (optane)  | `Morgante`_      |
+------------------+-----------------------+-------+---------------+------------------+
| fm-bigmem-4	   | bigmem[008-009]       | 128   | 4 T           | `Morgante`_      |
+------------------+-----------------------+-------+---------------+------------------+

__________

Byte conversion table
---------------------

When looking at file sizes or assessing specs, it is good to bear in mind the equivalencies between the different units. Please see the table below for some example conversions.

+---------------+---------------+-------------------------------+-----------------------+---------------+
| Name		| Symbol	| Measurement			| Bytes			| Equivalency	|
+		+		+---------------+---------------+			+		+
|		|		| Binary	| Decimal	|			|		|
+===============+===============+===============+===============+=======================+===============+
| Kilobyte	| K or KB	| |2^10|	| |10^3|	| 1,024			| 1,024 bytes	|
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Megabyte	| M or MB       | |2^20|        | |10^6|	| 1,048,576		| 1,024	K	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Gigabyte	| G or GB       | |2^30|        | |10^9|	| 1,073,741,824		| 1,024	M	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Terabyte	| T or TB       | |2^40|        | |10^12|	| 1,099,511,627,776	| 1,024	G	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Petabyte	| P or PB       | |2^50|        | |10^15|	| 1,125,899,906,842,624	| 1,024	T	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+

.. |2^10| replace:: 2\ :sup:`10`
.. |2^20| replace:: 2\ :sup:`20`
.. |2^30| replace:: 2\ :sup:`30`
.. |2^40| replace:: 2\ :sup:`40`
.. |2^50| replace:: 2\ :sup:`50`

.. |10^3| replace:: 10\ :sup:`3`
.. |10^6| replace:: 10\	:sup:`6`
.. |10^9| replace:: 10\	:sup:`9`
.. |10^12| replace:: 10\ :sup:`12`
.. |10^15| replace:: 10\ :sup:`15`

.. _Konkel: https://scienceweb.clemson.edu/chg/dr-miriam-konkel
.. _Morgante: https://scienceweb.clemson.edu/chg/dr-fabio-morgante
.. _Witt Dillon: https://scienceweb.clemson.edu/chg/dr-kelsey-witt-dillon
