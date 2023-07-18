# SIPssert Testing Framework Asterisk AMI Client Task

Task used to run a script using the Asterisk AMI Client

## Behavior

The task is able to communicate with one or more Asterisk instances using the
Pyst2 Python Library over the Asterisk AMI interface. 
It has two different working modes: running a batch command, or
running a script, either with the `.sh` (executed with bash), either a `.py`
file (executed with python).

## Defaults

The variables overwritten by default by the task are:

* `image`: default image to run is `yaroslavonline/ami-client'

## Settings

Additional settings that can be passed to the task:

* `script`: required, a path to a `.sh` or `.py` script that can be executed;

## Example

Listen AMI Events using Asterisk AMI Client Task

```
 - name: Control call
   type: ami-client
   script: scripts/ami-client.py
```
