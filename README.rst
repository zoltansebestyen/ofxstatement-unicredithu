~~~~~~~~~~~~~~~~~~~~~~~~~~~
UniCredit plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plugin to read UniCredit (https://www.unicreditbank.hu) exported XMLs.

The exported XMLs pretty much conform to CAMT.053 (ISO-20022), with some extra
information thrown in here and there, or some missing data in some other places.

This plugin is heavily based on https://github.com/kedder/ofxstatement-sample
with XML/CAMT.053 importer code lifted from ofxstatement-otp.

UniCredit CAMT.053 export can contain data for more than one account; in this
case we have to specify them in the configuration:

[unicredit-00]
plugin = unicredit
account = 12345678-12345678-0000000

[unicredit-01]
plugin = unicredit
account = 12345678-12345678-0000001

When running ofxstatement, we can refer to them the following way:

ofxstatement convert -t unicredit-01 ../STATEMENT_123456_20171130.xml exp01.ofx

Note that during the conversion, the last - CRC - digit and the separator
dashes are stripped.
