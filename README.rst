=====================
Python Command Center
=====================

GUI window to easily run your own frequently used commands

Installation
============
Install from pypi using pip::

   pip install command-center

Usage
=====
Create a ``pcc.json`` file to hold your commands.::

   {
     "test": "pytest",
     "lint": "flake8"
   }

Then simply run pcc in the terminal with your command key.::

   $ pcc test

If you want to display a button window for easy mouse use, use pcc-gui.::

   $ pcc-gui

Adding ``--help`` to pcc or pcc-gui will display helpful information.

