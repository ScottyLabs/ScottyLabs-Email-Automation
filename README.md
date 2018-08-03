# ScottyLabs Email Automation
This is a Python script to automate sending the weekly and reminder emails for [ScottyLabs](https://scottylabs.org/) at [Carnegie Mellon University](https://www.cmu.edu).

### Dependancies
You will need the following packages installed for Python 2.7:
* `email`
* `datetime`
* `requests`
* `webbrowser`

### Installation
Update your API keys and settings in the `settings.py` file.

### Use
`python send.py` runs you through the entire script.
1. Weekly Email
	1. Update the HTML email body using Vim. (I, personally, prefer to write the body using a Markdown editor and then copy the HTML source.)
	2. Preview the email to check the formatting in the default browser.
	3. Choose a subject. 
		1. `+` is the default subject when there is a meeting scheduled.
		2. `-` is the default subject when there are no meetings scheduled.
		3. `c` is a custom subject.
2. Reminder Email
	1. Choose the reminder type from `gbm`, `hs`, and a custom message.
	2. Enter the message or choose the default message.
	3. Preview the email to check the formatting in the default browser.
	4. The reminder email will be scheduled on the day of the specific event (or immediately for custom messages).

**NOTE:** Messages cannot be scheduled more than 3 days in advanced as per Mailgun's API restrictions.

![Command Line Use](screenshots/use.jpg?raw=true)

### Template
The template used in this project was derived from a [DigitalOcean email template](https://reallygoodemails.com/punctual/terms-of-service/important-updates-on-our-gdpr-compliance/), but you can use any template and use the placeholder `[[[_markdown]]]` where you would like your content to go.

Ideally, the template should follow basic email template guidelines to be consistently displayed across all platforms. These include having all CSS inline and enclosing all the content inside a table.

![Desktop Preview](screenshots/desktop.jpg?raw=true "Desktop Preview")
