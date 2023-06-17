# Whatsapp Automation
This tool automates sending whatsapp messages to lots of contacts.<br>
<br>

## Prereqiusites to write a message to various numbers:
Run on python 2.X and 3.X<br>
The contacts to be texted to should be in a text file.<br>
in the `msgsender.py` file in line 15 `(FILENAME variable)` replace `client.txt` with your text file name (with the contacts)<br>
<br>
## Setting the text(s) to send
In the `whatsend/core.py` file, in line 76 under the `message` variable, <br>place the preffered message in the brackets `[ Your message goes Here ]`<br>
If you want to send multiple messages at once, put each message in double quotes (" ") separated by a comma (,)<br>
<br>

## Setting image(s) to send
In the images folder, put all the images that you would like to send in to your contacts.<br>
If there is no image in the folder then just the text message(s) will be sent<br>

## Run
To execute depending on the python versio in use, run `python msgsender.py` or `python3 msgsender.py`<br>
Whatsapp web will open automatically with the phonenumber and write a text message.<br>
<h4>The same way you can only write the message on the foreground, this Automtion does not run in the background.<br>
  This means that, for now you should let the automation run uninterupted</h4>

All successfully texted contacts will be stored in the `success_log.txt` file.

##### NOTE: The process only terminates when all contacts have been texted. This might violate whatsapp terms of service and could lead to a Ban. If you wish to terminate the process, kill the terminal

## Future
Allow text messages to be run in the background<br>
Create an interface to upload images and text


