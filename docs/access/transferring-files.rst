Transferring files
==================

When transferring files between external sources and Secretariat, you have a few options.

If you have a small number of small files, and you are not very comfortable working from the command line, **FileZilla** may be a good option for you. FileZilla facilitates file transfers within a graphical user interface (GUI) that may feel more familiar to novice programmers. For larger files and larger numbers of files, you should use **scp** and **rsync**. Please find instructions on how to use each of the methods, below.

FileZilla
---------

Establish the connection
^^^^^^^^^^^^^^^^^^^^^^^^

1. Download and install the `FileZilla client`_.
2. Launch the client.
3. Open the 'Site manager' -- this is usually the upper left icon on the 'Toolbar' (it resembles a cluster of three rectangular machines).
4. Create a new site: 

	a. Click 'New Site' and name it **Secretariat**.
	b. Set 'Protocol' as 'SFTP - SSH File Transfer Protocol' in the dropdown list.
	c. Type **secretariat-master.clemson.edu** in the 'Host' box. 
	d. Set 'Logon Type' as 'Ask for password' in the dropdown list.
	e. Type your username in the 'User` box.
	f. Click 'OK' at the bottom of the window.

5. Reopen the 'Site manager' and select 'Secretariat' in the list of sites in the left window. Click 'Connect.'
6. Enter your password.
7. Trust the host: An 'Unknown host key' window may pop up at this stage. It may present a message similar to the one below:

	*The server's host key is unknown. You have no guarantee that the server is the computer you think it is. [...] Trust this host and carry on connecting?*

   Click 'OK'.

8. Output should print to the 'Message log' (the pannel below the 'Toolbar' and 'Quickconnect' sections at the top of the window). When output similar to the following appears and files / directories appear for both the 'Local site' and the 'Remote site', the connection has been successfully established.

.. code-block:: bash

   Status:	Connected to secretariat-master.clemson.edu
   Status:	Retrieving directory listing...
   Status:	Listing directory /home/madonay
   Status:	Directory listing of "/home/madonay" successful

Connection established!

Transfer the files
^^^^^^^^^^^^^^^^^^



scp
---

**Local to remote**



**Remote to local**



**Remote to remote**



rsync
-----




.. _FileZilla client: https://filezilla-project.org/
