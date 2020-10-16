Computational nodes
===================

You may submit jobs to two types of partitions on Secretariat. 

Secretariat specs
-----------------

+---------------+---------------+-----------------------+-----------------------+---------------+
| Cluster	| Partition	| Node			| Compute cores (CPUs)	| RAM		|
+===============+===============+=======================+=======================+===============+
|		|		| compute001		| 40			| 192 GB	|
+		+		+-----------------------+-----------------------+---------------+
|		| compute	| compute002		| 40			| 192 GB	|
+		+		+-----------------------+-----------------------+---------------+
|		|		| compute003 ``*``	| 40			| 192 GB	|
+		+		+-----------------------+-----------------------+---------------+
|		|		| compute004 ``*``	| 40			| 192 GB	|
+		+---------------+-----------------------+-----------------------+---------------+
| Secretariat	|		| bigmem001		| 40			| 1.54 TB	|
+		+		+-----------------------+-----------------------+---------------+
|		| bigmem	| bigmem002		| 40			| 1.54 TB	|
+---------------+---------------+-----------------------+-----------------------+---------------+

.. note:: ``*`` These compute nodes also belong to another partition called *PBC* (**do not** submit jobs to this partition). Periodic, automatic data transfers from the PacBio Sequencer will be given priority and will use resources on these two compute nodes, only. Secretariat may assign jobs to these nodes when resources are requested of the ``compute`` partition, but this will only occur when they are not being used to transfer data. Likewise, you may request resources directly from ``compute003`` and ``compute004``; however, when your process initiates will depend on if the nodes are currently in use by the PacBio Sequencer.

When looking at file sizes or assessing specs, it is good to bear in mind the equivalencies between the different units. Please see the table below for some example conversions.

Byte conversion table
---------------------

+---------------+---------------+-------------------------------+-----------------------+---------------+
| Name		| Symbol	| Measurement			| Bytes			| Equivalency	|
+		+		+---------------+---------------+			+		+
|		|		| Binary	| Decimal	|			|		|
+===============+===============+===============+===============+=======================+===============+
| Kilobyte	| KB		| |2^10|	| |10^3|	| 1,024			| 1,024 bytes	|
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Megabyte	| MB	        | |2^20| 	| |10^6|	| 1,048,576		| 1,024	KB	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Gigabyte	| GB	        | |2^30| 	| |10^9|	| 1,073,741,824		| 1,024	MB	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Terabyte	| TB	        | |2^40| 	| |10^12|	| 1,099,511,627,776	| 1,024	GB	|        
+---------------+---------------+---------------+---------------+-----------------------+---------------+
| Petabyte	| PB	        | |2^50| 	| |10^15|	| 1,125,899,906,842,624	| 1,024	TB	|        
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
