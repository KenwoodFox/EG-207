Interface Information
=====================

.. warning::
    This section is intended for **developers**, and may be irrelevant unless
    you intend to modify or expand the functionality of :ref:`Normal Use`.


GoldPackets
###########

:ref:`GoldPackets` is a custom designed packet standard, made by Team Gold for the EG-207 CMS.

The format is call/response based and detailed below:

+-------+----------+--------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Inst  |   Byte   |       Reply        |   ACK    |   Fail    |                                                                        Note                                                                         |
+=======+==========+====================+==========+===========+=====================================================================================================================================================+
| ``v`` | ``76``   | ``v0.1_g70b...\n`` | ``ok\n`` | ``127\n`` | The "Version" Command will return the version as ascii. If it prints ``OK`` at the end it completed otherwise it may raise and print an error code. |
+-------+----------+--------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``e`` | ``0x65`` | ``127\n``          | ``ok\n`` | ``127\n`` | The "Error" command will print and remove the last error in the EEPROM, if it returns the error as a response code, the error could not be removed. |
+-------+----------+--------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``t`` | ``0x74`` | ``32.00\n``        | ``ok\n`` | ``127\n`` | Lowercase t will poll the DHT11 for its temperature value and return it at that time.                                                               |
+-------+----------+--------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+


Communication Example
---------------------

.. code-block:: shell

    > v
    CDR-RELEASE-102-gaf0e-dirty
    ok
    > p
    ?70
    ok
