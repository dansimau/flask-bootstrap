
Overview
========

This puppet module manages ferm and its rules.

Variables
=========


Classes
=======

ferm
----

The ferm class performs all steps needed to the use of ferm such as package
installation and configuration. Specific rules can be added later with 
ferm::rule or specific classes.


Defines
=======

ferm::rule
----------

Add a rule to the ferm rules.d directory

Variables used :
	$host = false, 
	$table="filter", 
	$chain="INPUT", 
	$rule, 
	$description="", 
	$prio="00", 
	$notarule=false

ferm::hook
----------

Add a hook to the ferm conf.d directory.

Example:

    ferm::hook { 'conntrack_ftp':
        description => 'Module nf_conntrack_ftp pour proftpd',
        content_hook => 'modprobe nf_conntrack_ftp'
    }

Licensing
=========

This puppet module is licensed under the GPL version 3 or later. Redistribution
and modification is encouraged.

The GPL version 3 license text can be found in the "LICENSE" file accompanying
this puppet module, or at the following URL:

http://www.gnu.org/licenses/gpl-3.0.html
