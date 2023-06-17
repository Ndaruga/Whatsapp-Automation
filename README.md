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
All successfully texted contacts will be stored in the `success_log.txt` file.


## Future
Allow text messages to be run in the background
Create an interface to upload images and text


