ProPatriot - Hardening Software and Security Penetration Techniques 
=======================================================================

**CyberVideo: 5 Most Used Hacking Os's (Courtesy: Tech Koder)**

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/0Bo5NYCspPA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Penetration and Vulnerability Testing Using Burp Suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Core Knowledge:** A Burp suite is a powerful tool that many penetration testers use professionally. Learning how to use these tools effectively can make sure that the applications you are using are strong and secure from all sorts of malicious attacks. The Burp Suite community edition has much fewer features than the professional and enterprise versions, but it’s good enough that if you master the community edition then you have gained a powerful set of skills.


.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/30.jpg
   :width: 50%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/29.jpg
   :width: 50%
   :align: center
   

O&O ShutUp10++ - A Way of Hardening Windows OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you would like to block Window’s suspect spyware then definitely use this software. It works for Windows 11 too just in case you made the big mistake of “upgrading” to 11 or higher.

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/140.jpg
   :width: 51%
   :align: center


.. Note::

There are many many settings that help you increase your privacy, security, and Quality of Life (QOL)  
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/141.jpg
   :width: 50%
   :align: center
   
.. Note::

Eliminate advertising ID by Windows along with sending clipboard data to Windows’s servers along with other weird stuff. 

**Safing Portmaster - An Easy To Use Firewall For Your Computer**

If you would like to block all incoming connections on your computer and any unnecessary programs pinging the world outside, this is a fantastic piece of software.

All you need to do is flick the switch and all those nasty connections coming from Adobe Creative Cloud are all gone.

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/6c4d4fe8fc7a511a7b5609a0f53ae1e194d2f009/docs/img/image.png
   :width: 51%
   :align: center
   
Security and Hardening with Ubuntu Linux OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Recover Ubuntu Password**

There are times when we create a new Ubuntu machine and just forget the password. Instead of spending all of that time doing the guessing game, you can easily make a new password and recover your machine in just a couple minutes.

Source: https://itsfoss.com/how-to-hack-ubuntu-password/

.. image:: https://github.com/natt96z/cybersac/blob/main/docs/img/Capture.PNG?raw=true
   :width: 51%
   :align: center

.. image:: https://github.com/natt96z/cybersac/blob/main/docs/img/Capture%201.PNG?raw=true
   :width: 51%
   :align: center

.. image:: https://github.com/natt96z/cybersac/blob/main/docs/img/Capture%202.PNG?raw=true
   :width: 51%
   :align: center

.. image:: https://github.com/natt96z/cybersac/blob/main/docs/img/Capture%203.PNG?raw=true
   :width: 51%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/Capture%204.PNG
   :width: 51%
   :align: center

**Disable Ubuntu Recovery Password**

After performing the password recovery on Ubuntu you can probably tell it's a huge security vulernability in the case that someone physically gets your computer and wants to access everything inside. To protect yourself from this threat, all you have to do is delete one line in your configuration files and change your grub menu password.

Sources: https://askubuntu.com/questions/321115/how-to-remove-password-recovery-reset

https://askubuntu.com/questions/248196/how-to-password-protect-grub-menu-entry

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/Disable%20Ubuntu%20Recovery%20Password.PNG
   :width: 51%
   :align: center


.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/Change%20Grub%20Menu%20Password.PNG
   :width: 51%
   :align: center

.. Note::   

Tip: if a physical security threat is a concern, you should really consider encrypting the device from the start.


**Disabling Root Access** 

While the average user can use Linux without ever using the terminal, it is nevertheless a powerful tool that has the ability to grant attackers full access to a computer. Linux is a command-heavy operating system. "Root access" in Linux refers to the unrestricted power to execute any command. It can be safely removed because it often comes in handy. Root access can always be guarded by a password. 

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/pasted%20image%200.png
   :width: 65%
   :align: center
  
.. Note::

To lock root access behind a password, open the terminal and enter “sudo -i.”  When the next line, a # prompt, appears, enter “password.”  This will give you the prompt for setting a root password.

**Installing SSH on Ubuntu:** Just type the following apt command/apt-get command:

.. hint::
   | sudo apt-get update
   | 
   | sudo apt-get upgrade
   |
   | sudo apt-get install openssh-client
   
   
   
   
   
   
   

**Disable root Login:** This configuration will limit SSH only to users other than root.

PermitRootLogin no

**Allow Specific Users:** This line will allow you to specify which users can log into the SSH service:

AllowUsers accountName

**Change Default Port From 22:** This line will specify which port to host the SSH service on.

Port 22222

**Disable Empty Passwords:** This line ensures that no users can login with an empty password.

PermitEmptyPasswords no

**Restart Service** As always, after making changes to a service be sure to restart it!

service ssh restart


**Lynis - Security auditing tool for Linux, macOS, and UNIX-based systems**

Source: https://github.com/CISOfy/lynis

Video follow along:

<iframe width="560" height="315" src="https://www.youtube.com/embed/fUIpJJn6YaM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



**BONUS: Using RKHunter - The Rootkit Hunter project**


.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/install-and-configure-rkhunter-with-tightened-security-variables-rkhunter-logo.png
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/rkhunter-results.png
   :width: 65%
   :align: center


The package “rkhunter” is useful for doing a quick scan of your system for any known rootkits:

apt-get install rkhunter

rkhunter -C



**CyberVideo: Best Hacking Operating System! (Courtesy: zSecurity)**

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/lAnQzVqx9s4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

What is Kali Linux? - Detailed Computer Penetration Testing (Setup Image Guide)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**Core Knowledge:** Kali Linux (Formerly known as BackTrack Linux) Is an open-source, Debian-based Linux distribution aimed at advanced Penetration Testing and Security Auditing. Kali Linux contains several hundred tools targeted toward various information security tasks, such as Penetration Testing, Security Research, Computer Forensics, and Reverse Engineering. Kali Linux is a multi-platform solution, accessible and freely available to information security professionals and hobbyists.

.. Note::

 
Kali Linux was released on the 13th March 2013 as a complete, top-to-bottom rebuild of BackTrack Linux, adhering completely to Debian development standards. 

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/98.jpg
   :width: 65%
   :align: center
   
**Kali Features include:**  

    *More than 600 penetration testing tools*
    
    *Free to download*
    
    *Open-source Git tree* 
    
    *File System Hierarchy Standard*  
    
    *Wide-ranging wireless device support* 
    
    *Custom kernel, patched for injection*
    
    *Developed in a secure environment*
    
    *GPG signed packages and repositories*
    
    *Multi-language support* 
    
    *Completely customizable* 
    
    *ARMEL and ARMHF support* 
    

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/99.jpg
   :width: 65%
   :align: center

.. Note::

The site is well organized as well to aid with using on any compatible computer. There are also helpful help forums and FAQ's to troubleshoot possible issues.


How to Set Up Kali Linux OS (Virtual Box)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
**Step 1: Open Oracle Virtual Machine and install Kali Linux (Easy Image Guide)**

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/100.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/101.jpg
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/102.jpg
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/103.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/104.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/105.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/106.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/107.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/108.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/109.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/110.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/111.jpg
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/112.jpg
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/113.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/114.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/115.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/116.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/117.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/118.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/119.jpg
   :width: 65%
   :align: center
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/120.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/121.jpg
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/122.jpg
   :width: 65%
   :align: center

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/123.jpg
   :width: 65%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/124.jpg
   :width: 65%
   :align: center
   
TryHackMe – Website for Learning Cyber Security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/135.jpg
   :width: 67%
   :align: center
   
**Core Knowledge:** TryHackMe is a CTF website that uses an interactive virtual lab to teach cybersecurity. Whether you are an expert or a beginner, you will learn about theoretical and practical security features utilizing a virtual room architecture. It's an intuitive cybersecurity tool that tests individuals in a range of virtual machine rooms to find solutions to computer security issues and capture or defend computer systems.

   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/136.jpg
   :width: 65%
   :align: center
   
.. Note::

Once you create a FREE account on the website you will be able to choose from 3 learning paths. I went ahead and chose the first, which is the basics of hacking for newcomers. I've found that most of the content on the website is free so far.

   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/137.jpg
   :width: 70%
   :align: center
   
.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/138.jpg
   :width: 70%
   :align: center

The website will provide you with a live Ubuntu virtual machine and easy to follow steps on the side to accompany the hacking demonstration. In this lesson you are learning how to hack a dummy bank account website to explore its hidden directories.  

.. image:: https://raw.githubusercontent.com/natt96z/cybersac/main/docs/img/139.jpg
   :width: 70%
   :align: center

As you can see, I successfully initiated a bank transfer from the dummy users account. This website also has an Android application that allows you to practice hacking on the go.  This short example basically shows how easy it can be for a hacker to gather personal information. 

 
