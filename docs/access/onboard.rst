==========
Onboarding
==========

Welcome to the Secretariat Community! We look forward to you joining us.

----

HPCC Basics Workshop
####################

We recommend that all Secretariat users attend the HPCC Basics Workshop, even if they already have cluster experience. `Please see this page for more information`_.

----

Account + Access
################

Once an account has been created for you on Secretariat, you can connect via command line terminal using the following command:

``ssh -X [username]@secretariat-master.clemson.edu``

	Insert your own username in the place of [username] – you do not need the brackets.

You may also connect to Secretariat via Open OnDemand internet browser (e.g. `https://secretariat-master`_), similar to `Palmetto's setup`_.

When you are not connected to the Clemson network (e.g. when you are away from campus), make sure you connect to the `Clemson Virtual Private Network (CUVPN)`_ before trying to log into Secretariat!

----

Groups
######

All Secretariat users are members of specific groups. The purpose of these group memberships is to help set specific directory and file permissions. If you have questions about how this works, please reach out! (We cover this on Day 1 of the HPCC Workshop!)

----

Directories
###########

Each Secretariat user receives a directory in /home as well as a directory for data storage and analyses in /data or /data2.

Once you sign in, you should have permission to access these directories using the `cd`_ command-line shell command. If you have trouble with this, please let us know!

----

Communications on Slack
#######################

The `#secretariat`_ `Slack`_ channel will be used to communicate things including, but not limited to, scheduled or emergency maintenance of Secretariat and new software installations. All Secretariat users are welcome to join this channel to follow updates or post questions.

----

HPCC Etiquette
##############

Resources: Because Secretariat is a much smaller cluster than `Palmetto`_, a bit more discretion is advised when it comes to requesting resources (e.g. cpus, memory, time). Generally, being on the conservative side helps manage everyone’s needs and uses. If you are unclear about how you should request resources, please reach out to us once you are ready to run analyses on Secretariat!

Home directory (/home): Make sure to keep /home/esak (<5 Gb) and clean. If you are unclear about what this means or how to monitor this once you start using Secretariat, please let us know and we can help get you started!

Data directory (/data, /data2): Your software libraries / packages / environments (e.g. R, Python, conda), data files, and related resources for analyses should be kept within your data directory. Please keep in mind that this data directory will not be backed up unless a Palmetto backup has been set up with us or you generate another copy through other means (e.g. upload to cloud storage).

Login node: Do not run analyses or resource intensive tasks on the login / head node (secretariat-master). Instead, you should submit a script to one of the computational nodes. If you would like any assistance, please let us know and we can advise you on how to do this properly!

----

.. _Please see this page for more information: https://secretariat.readthedocs.io/en/latest/additional-resources/workshops.html#hpcc-basics-workshop
.. _https://secretariat-master: https://secretariat-master
.. _Palmetto's setup: https://docs.rcd.clemson.edu/openod
.. _Clemson Virtual Private Network (CUVPN): https://secretariat.readthedocs.io/en/latest/additional-resources/vpn.html
.. _cd: https://www.geeksforgeeks.org/cd-command-in-linux-with-examples
.. _#secretariat: https://cu-chg.slack.com/archives/C0472VDJ8PL
.. _Slack: https://slack.com
.. _Palmetto: https://docs.rcd.clemson.edu/palmetto
