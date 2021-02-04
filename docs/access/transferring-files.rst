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
	e. Type your ``username`` in the 'User' box.
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

Once you have established a connection, you may initiate uploads and downloads between the two sites.

1. **Upload: Local-to-remote**

	a. Locate the file(s) / folder(s) to upload.

		*Within the 'Local site' window, select the file(s) / folder(s).*

	b. Locate the destination folder.

		*Within the 'Remote site' window, select the destination folder.*
	
	c. Right click the file(s) / folder(s) to upload. Select 'Upload' in the drop down list that appears.
		
		i. The transfer should initiate. You may track your progress in the 'Transfer queue'.

			*This is the panel at the bottom of the window.*

		ii. Once the files appear in the 'Successful transfers' tab of the 'Transfer queue', the file has been successfully transferred from the local site to the remote site.

	Transfer complete!

2. **Download: Remote-to-local**

	a. Locate the file(s) / folder(s) to download.

		*Within the 'Remote site' window, select the file(s) / folder(s).*

	b. Locate the destination folder.

		*Within the 'Local site' window, select the destination folder.*
	
	c. Right click the file(s) / folder(s) to download. Select 'Download' in the drop down list that appears.
		
		i. The transfer should initiate. You may track your progress in the 'Transfer queue'.

			*This is the panel at the bottom of the window.*

		ii. Once the files appear in the 'Successful transfers' tab of the 'Transfer queue', the file has been successfully transferred from the remote site to the local site.

	Transfer complete!

scp
---

``scp`` is a function used to securely copy files and is already installed on Secretariat. Please see the use-cases, below.

1. **Local to remote**

	``scp /path/to/file.txt username@secretariat-master.clemson.edu:/remote/directory/``

	where

		- ``/path/to/file.txt``: file (including full path) to upload to Secretariat
		- ``username``: your username to log in to Secretariat
		- ``/remote/directory/``: where to upload file on Secretariat

2. **Remote to local**

	``scp username@secretariat-master.clemson.edu:/path/to/file.txt /local/directory/``

	where

             	- ``/path/to/file.txt``: file (including full path) to download from Secretariat
                - ``username``: your username to log in	to Secretariat
                - ``/local/directory/``: where to download file on local machine

MobaXterm scp
-------------

If are a Windows user and followed the instructions for installing and using `MobaXterm`_ on the `Logging in`_ page, then you also have the option of using MobaXterm's built in ``scp``.

.. attention:: Note: This process is similar to using `FileZilla`_ (`above`_).

Part 1: Connect
^^^^^^^^^^^^^^^

1. Click "Session"
2. Click "SSH"
3. Click "Advanced SSH settings"
4. Select "SCP (normal speed)" as the SSH browser type
5. Enter ``secretariat-master.clemson.edu`` in the "Remote host" box
6. Check the box beside "Specify username" and type your ``username``
7. Click "OK"
8. Enter password, if prompted

Connection established!

Part 2: Transfer
^^^^^^^^^^^^^^^^

.. attention:: All of the following steps take place in the left sidebar.

1. Select the "Scp" tab
2. Enter ``/path/to/directory/`` in the search bar

	*Where you enter the specific directory to your file(s) of interest in place of ``/path/to/directory/``* 

3. Right-click the file(s) in the file list that you would like to download
4. Click "Download"
5. Select / create the local directory to receive the file(s)
6. Click "OK"

Transfer complete!

.. attention:: Another option within MobaXterm is to initiate a local session and use the `previously described`_ ``scp`` commands. To do this, either select "Start local session" after launching MobaXterm or open a new tab by clicking on the "+" icon. This second option should start a local session by default.

.. _FileZilla client: https://filezilla-project.org/
.. _above: https://secretariat.readthedocs.io/en/latest/access/transferring-files.html#filezilla
.. _MobaXterm: https://mobaxterm.mobatek.net/
.. _Logging in: https://secretariat.readthedocs.io/en/latest/access/logging-in.html#for-windows
.. _previously described: https://secretariat.readthedocs.io/en/latest/access/transferring-files.html#scp
