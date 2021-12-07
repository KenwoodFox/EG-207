Interface Information
=====================

.. warning::
    Warning! This section is intended for **developers**, and may be irrelevant to the :ref:`Normal Use`
    expected.


GoldPackets
###########

:ref:`GoldPackets` is a custom designed packet standard, made by Team Gold for the EG-207 CMS.

The format is call/response based and detailed below:

+-------+--------+---------------------------------+--------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Inst  |  Byte  |              Reply              |  ACK   |  Fail   |                                                                        Note                                                                         |
+=======+========+=================================+========+=========+=====================================================================================================================================================+
| ``v`` | ``76`` | ``CDR-RELEASE-93-g70ba682f\n``` | ``OK`` | ``127`` | The "Version" Command will return the version as ascii. If it prints ``OK`` at the end it completed otherwise it may raise and print an error code. |
+-------+--------+---------------------------------+--------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``e`` |        | ``127``                         | ``OK`` | ``127`` | The "Error" command will print and remove the last error in the EEPROM, if it returns the error as a response code, the error could not be removed. |
+-------+--------+---------------------------------+--------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------+