==========
Logging in
==========

Please complete Parts 1 and 2, below.

----

**PART 1**: Login
#################

For Linux / Mac
---------------

1. Open a Terminal window.
2. Type ``ssh -X [username]@secretariat-master.clemson.edu`` on the command line; Press Enter.

	*Insert your own username in the place of [username] -- you do not need the brackets.*

3. Type password on the command line; Press Enter. Your initial password will be **1234**.

Login is complete!

For Windows
-----------

1. Download `MobaXterm`_. (The 'Installer Edition' is fine.)
2. After installing, launch MobaXterm and click the 'Session' button. Select 'SSH'.
3. Type **secretariat-master.clemson.edu** in the 'Remote host' box.
4. Check the 'Specify username' box and type your aforementioned username.
5. Click 'OK'.

	*After the box closes, a new tab should appear and you will be prompted to enter your password.*

6. Type password on the command line; Press Enter. Your initial password will be **1234**.

Login is complete!

----

**PART 2**: Prepare work environment
######################################

For Linux / Mac / Windows
-------------------------

1. Type ``passwd`` on the command line; Press Enter.

	(You will be prompted to enter your current password and then your new password.)

2. Type ``ssh-keygen -t rsa`` on the command line; Continue pressing Enter until complete.

	*The process will be complete when the command line prompt returns to the* ``[username]@secretariat-master ~]$`` *format.*

3. Type ``cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys`` on the command line; Press Enter.
4. Type ``exit`` on the command line.

The session has ended!

.. _MobaXterm: https://mobaxterm.mobatek.net/
