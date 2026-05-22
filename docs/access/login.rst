==========
Logging in
==========

.. _tip-contact:

.. tip::

   **Contact** `Secretariat System Administrators`_ **with HPC Questions!**

   +------------------+----------------+--------------------+
   | `Vijay Shankar`_ | `John Poole`_  | `Maria E. Adonay`_ |
   +------------------+----------------+--------------------+

   .. code-block:: text

      vshanka@clemson.edu,jopoole@clemson.edu,madonay@clemson.edu

   .. raw:: html

      <hr>

   **Contact** `IHG Research Cores`_ **with Research Questions!**

   .. code-block:: text

      ihgcores@clemson.edu

----

Sequentially complete **both** Parts 1 and 2 to login, set your password, and to submit jobs to nodes. For Part 1, complete the instructions appropriate for your machine.

.. attention:: Do not attempt the following steps until you have been contacted regarding your username.

   If you would like an account on Secretariat, please let us know!.

When you plan to connect to Secretariat while **away** from campus, **you must first connect** to the `Clemson Virtual Private Network (CUVPN)`_! 

----

Part 1: Login
#############

.. tab-set::

   .. tab-item:: Linux / Mac

      1. Contact Vijay, John, and Maria (see :ref:`above email list <tip-contact>`.) for information about your intial password if you have lost it.

      2. Open a Terminal window.

      3. Type ``ssh [username]@130.127.173.136`` on the command line; Press Enter.

         *Insert your own username in the place of* ``[username]`` -- *you do not need the brackets.*

      4. Type initial password; Press Enter.

         *Note: As you type the password on the command line, the cursor will not move to indicate that you have typed anything. This is a security feature. Type the entire password and press Enter.*

      5. Select your method of Duo Two-Factor Authenication.

         *Mobile device users should enter the number associated with their preferred Duo authentication method* (commonly ``1``) *to trigger a push notification. Users with alternative methods will get a second prompt for a passcode or token key.*

         `Click here for more information about Duo`_.

         *The process will be complete when the command line prompt shows to the* ``[username]@secretariat-master ~]$`` *format.*

      Login complete!

      .. attention:: Remain logged in to complete Part 2.

   .. tab-item:: Windows

      1. Contact Vijay, John, and Maria (see :ref:`above email list <tip-contact>`.) for information about your intial password if you have lost it.

      2. Open your preferred terminal emulator.

         *As of 2025, Clemson had a license for* `StarNet X-Win32`_, *which could be installed on Windows from* `Company Portal`_. *However, many Windows machines come equipped with* `Windows PowerShell`_, *which should also work!*

      3. Type ``ssh [username]@130.127.173.136`` on the command line; Press Enter.

         *Some terminal emulators provide separate fields for connection information rather than a command-line prompt. In these cases, make sure to use* ``130.127.173.136`` *as the "remote host" or "server address".*

      4. Type initial password; Press Enter.

         *Note: When you type your password from the command line, the cursor will not move to indicate that you have typed anything. This is a security feature. Type the entire password and press Enter.*

      5. Select your method of Duo Two-Factor Authenication.

         *Mobile device users should enter the number associated with their preferred Duo authentication method* (commonly ``1``) *to trigger a push notification. Users with alternative methods will get a second prompt for a passcode or token key.*

         `Click here for more information about Duo`_.

         *The process will be complete when the command line prompt shows to the* ``[username]@secretariat-master ~]$`` *format.*

      Login complete!

      .. attention:: Remain logged in to complete Part 2.

..

	Note: **130.127.173.136** is often interchangable with **secretariat-master.clemson.edu**

----

Part 2: Prepare work environment
################################

.. tab-set::

   .. tab-item:: Linux / Mac / Windows

      1. While logged in to Secretariat, Type ``passwd`` on the command line; Press Enter.

         *You will be prompted to enter your current password and then your new password twice. When you type your password, it will not appear as you type. This is for security reasons. Press Enter after you have typed each password.*

      2. Type ``ssh-keygen -t rsa`` on the command line; Continue pressing Enter until complete.

         *The process will be complete when the command line prompt returns to the* ``[username]@secretariat-master ~]$`` *format.*

      3. Type ``cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys`` on the command line; Press Enter.

      4. Type ``chmod -R 700 ~/.ssh`` on the command line; Press Enter.

      5. Type ``exit`` on the command line; Press Enter.

      Session ended!

.. attention:: Immediately after completing Part 2, inform Vijay, John, and Maria (see :ref:`above email list <tip-contact>`.) so that they may finalize the status of your newly created account on Secretariat!

.. _Clemson Virtual Private Network (CUVPN): https://secretariat.readthedocs.io/en/latest/additional-resources/vpn.html
.. _Click here for more information about Duo: https://2fa.app.clemson.edu/
.. _StarNet X-Win32: https://www.starnet.com/xwin32/
.. _Company Portal: https://hdkb.clemson.edu/phpkb/article.php?id=1835
.. _Windows Powershell: https://learn.microsoft.com/en-us/powershell/
.. _Vijay Shankar: https://scienceweb.clemson.edu/chg/dr-vijay-shankar-2/
.. _John Poole: https://scienceweb.clemson.edu/chg/dr-john-poole/
.. _Maria E. Adonay: https://scienceweb.clemson.edu/chg/maria-adonay/
.. _Secretariat System Administrators: https://scienceweb.clemson.edu/ihg/research-cores/bsc-core/
.. _IHG Research Cores: https://scienceweb.clemson.edu/ihg/research-cores/
