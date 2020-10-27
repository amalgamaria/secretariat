Transferring files
==================

When transferring files between external sources and Secretariat, you have a few options.

If you have a small number of small files and you are not very comfortable working from the command line, **FileZilla** may be a good option for you. FileZilla facilitates file transfers within a graphical user interface (GUI) that may feel more familiar to novice programmers. For larger files or larger numbers of files, you should use **scp** and **rsync**. 

Please find instructions on how to use each of the methods, below.

FileZilla
---------

Part 1: Connect
^^^^^^^^^^^^^^^

1. Download and install the `FileZilla client`_.
2. Launch the client.
3. Open the 'Site manager' -- this is usually the upper left icon on the 'Toolbar'.

	*It resembles a cluster of three rectangular machines.*

4. Create a new site: 

	a. Click 'New Site' and name it **Secretariat**.
	b. Set 'Protocol' as 'SFTP - SSH File Transfer Protocol' in the dropdown list.
	c. Type **secretariat-master.clemson.edu** in the 'Host' box. 
	d. Set 'Logon Type' as 'Ask for password' in the dropdown list.
	e. Type your `username` in the 'User` box.
	f. Click 'OK' at the bottom of the window.

5. Reopen the 'Site manager' and select 'Secretariat' in the list of sites in the left window.
6. Click 'Connect' and enter your password.
7. Trust the host: An 'Unknown host key' window may appear with a message similar to the one below. Click 'OK'.

.. code-block:: bash

   The server's host key is unknown. You have no guarantee that the server is the computer you think it is. 
   
   [...] 
   
   Trust this host and carry on connecting?

8. Output should print to the 'Message log'.

	*This is the pannel below the 'Toolbar' and 'Quickconnect' sections at the top of the window.*

   When output similar to the following appears and files / directories are present in both the 'Local site' and the 'Remote site' panels, the connection has been successfully established.

.. code-block:: rst

   Status:	Connected to secretariat-master.clemson.edu
   Status:	Retrieving directory listing...
   Status:	Listing directory /home/[`username`]
   Status:	Directory listing of "/home/[`username`]" successful

Connection established!

Part 2: Transfer
^^^^^^^^^^^^^^^^



scp
---

**Local to remote**



**Remote to local**



**Remote to remote**



rsync
-----




.. _FileZilla client: https://filezilla-project.org/
