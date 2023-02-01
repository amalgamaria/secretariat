==========
Logging in
==========

Sequentially complete **both** Parts 1 and 2 to login, set your password, and to access the computational nodes. For Part 1, complete the instructions appropriate for your machine.

.. attention:: Do not attempt the following steps until you have been contacted regarding your username.

   If you would like an account on Secretariat, please let us know via the `Ticket Request Form`_.

----

Part 1: Login
#############

For Linux / Mac
---------------

1. Contact `Vijay`_, `John`_, or `Maria`_ for information about your intial password.
2. Open a Terminal window.
3. Type ``ssh -X [username]@130.127.173.228`` on the command line; Press Enter.

	*Insert your own username in the place of [username] -- you do not need the brackets.*

4. Type initial password (obtained from `Vijay`_, `John`_, or `Maria`_ in Step 1) on the command line; Press Enter.

        *Note: As you type the password, the cursor will not move to indicate that you have typed anything. This is a security feature. Type the entire password and press Enter.*

Login complete!

For Windows
-----------

1. Contact `Vijay`_, `John`_, or `Maria`_ for information about your intial password.
2. Download `MobaXterm`_. (The "installer" edition is fine. If this does not work, the "portabld" edition is also fine.)
3. After installing, launch MobaXterm and click the 'Session' button. Select 'SSH'.
4. Type **130.127.173.228** in the 'Remote host' box.
5. Check the 'Specify username' box and type your aforementioned username.
6. Click 'OK'.

	*After the box closes, a new tab should appear and you will be prompted to enter your password.*

7. Type initial password (obtained from `Vijay`_, `John`_, or `Maria`_ in Step 1) on the command line; Press Enter.

Login complete!

.. attention:: Remain logged in to complete Part 2.

----

Part 2: Prepare work environment
################################

For Linux / Mac / Windows
-------------------------

1. While logged in to Secretariat, Type ``passwd`` on the command line; Press Enter.

	*You will be prompted to enter your current password and then your new password. When you type your password, it will not appear as you type. This is for security reasons. Press Enter after you have typed each password.*

2. Type ``ssh-keygen -t rsa`` on the command line; Continue pressing Enter until complete.

	*The process will be complete when the command line prompt returns to the* ``[username]@secretariat-master ~]$`` *format.*

3. Type ``cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys`` on the command line; Press Enter.

4. Type ``chmod -R 700 ~/.ssh`` on the command line; Press Enter.

5. Type ``exit`` on the command line; Press Enter.

Session ended!

.. attention:: Immediately after completing Part 2, inform `Vijay`_, `John`_, or `Maria`_ so that they may finalize the status of your newly created account on Secretariat!


.. _MobaXterm: https://mobaxterm.mobatek.net/
.. _Vijay: https://scienceweb.clemson.edu/chg/dr-vijay-shankar-2/
.. _John: https://scienceweb.clemson.edu/chg/dr-john-poole/
.. _Maria: https://scienceweb.clemson.edu/chg/maria-adonay/
.. _Ticket Request Form: https://secretariat.readthedocs.io/en/latest/tickets.html#ticket-requests
