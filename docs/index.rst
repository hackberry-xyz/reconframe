Meet reconframe
===============

The reconframe is a Batteries included, Python Framework for performing
small scale to large scale reconnaissance by leveraging the power of the
Python Programming Language. Not every software is same. But in the end,
recon boils down to gaining information. Unlike traditional scripts,
toolsets or software, reconframe focuses on storing, parsing and gaining
information using the code provided by you.

Writing own code can be scary for many. But it shouldn't be. While reconframe
is a framework and main essence hides in writing the code, it is still
usable without actually writing code! What do we mean by that? reconframe
comes with ptpython - a user friendly Python interpreter. On the same,
helper functions are injected which are quite easy to learn and use!

Installing
==========

Presently, reconframe is heavily under development. But you can still get
a taste of it. Install using ``pip`` ::

    pip install git+https://github.com/hackberry-xyz/reconframe.git

.. warning::
    Current branch is ``develop`` which is being used for development purpose
    and is quite unstable. Code might not work as expected or sometimes
    completely broken. See `Wiki <https://github.com/hackberry-xyz/reconframe/wiki>`_
    for documentation on development process.


Contribute
==========
reconframe is a free and open source software under the `MIT license <https://github.com/hackberry-xyz/reconframe/blob/develop/LICENSE>`_. You can help by `writing code <https://github.com/hackberry-xyz/reconframe/>`_, donating or just saying a `thank you <https://twitter.com/intent/tweet?text=Thank+you+@hackberry_xyz+for+making+reconframe!&url=http://reconframe.hackberry.xyz>`_.

.. raw:: html
	
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
	<script type="text/javascript" src="https://blockchain.info/Resources/js/pay-now-button.js"></script>
	<div style="font-size:16px;margin:0 auto;width:300px" class="blockchain-btn" data-address="1Fue23nQkyn5TdsMwwgqETYLya6xcA9TWY" data-shared="false">
	  <div class="blockchain stage-begin">
	      <img src="https://blockchain.info/Resources/buttons/donate_64.png"/>
	  </div>
	  <div class="blockchain stage-loading" style="text-align:center">
	      <img src="https://blockchain.info/Resources/loading-large.gif"/>
	  </div>
	  <div class="blockchain stage-ready">
	      <p align="center">Please Donate To Bitcoin Address: <b>[[address]]</b></p>
	      <p align="center" class="qr-code"></p>
	  </div>
	  <div class="blockchain stage-paid">
	      Donation of <b>[[value]] BTC</b> Received. Thank You.
	  </div>
	  <div class="blockchain stage-error">
	      <font color="red">[[error]]</font>
	  </div>
	</div>


Documentation
=============

API Reference
-------------

If you are looking for information on a specific function, class, or
method, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   modules
