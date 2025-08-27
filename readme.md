## Actions
### Easy Actions
* [ ] Create a new directory for the output files (currently .csv files) and move files there
* [ ] Work on linking between survey pages
* [ ] Redirect to 'Home' after completing form
* [ ] Improve documentation

### Medium Actions
* [ ] Create new form for Net Promoter Score
* [ ] Create new form for Customer Effort Score
* [ ] Add a login page for the admin/dashboard area
* [ ] Generally improve Dashboard page
* [ ] Free form text questions are not generally captured as its hard to represent in the dashboard, this needs reviewed

### Hard Actions
* [ ] Change app.py to output to JSON
* [ ] Consider Database options 
* [ ] Look at React for the forms

## How to Guides
### Test Code locally
* Get access to this repo by contacting me
* Install Python to your machine, ideally 3.11.3. Other version may or may not work
* Git clone this repository
* run "python -m pip install -r requirements.txt"
* run "python app.py" and open the link that appears in the terminal
* Create a local branch, make your changes and re-run app.py 
* Do functional testing of new code
* Raise MR and let me know

### Add a new form
* Create a new html file in the templates directory by copying and pasting onboard_survey.html
* Rename it as desired
* Look for the code nested in the ```<form method="post">...</form>``` roughly between lines 29-72
* This is the basic structure of the form, edit this as desired to create the new page.
* It should always capture the name first as so ```<h2>Personal Details</h2>
    Name: <input type="text" name="name"><br><br>```
* Each question should have a unique key with NO SPACES or SPECIAL CHARS, heres an example ```<select name="completed_onboarding">```. You would replace the word completed_onboarding for each questions and save this for later
* Once you've create the basic questions, go to the app.py file
* Create a new 'route' by copying an existing one such onboard-survey. Give it the same name as your html file, if your html file name has underscores, replace them with -
* Edit the function name one line below, this should have underscores and not -
* For each question on your new html file, you need to edit the app.py function you have just created so it gets the answers. It uses the unique key you added to the html file earlier. Go through the function and update as required.
* update the following line by replacing customer_engagement with the name of your new HTML file ```with open("customer_engagement.csv", "a") as f:```
* Note: You may need to create the .csv file at this point
* Update the next line with your unique keys you created earlier ```f.write(f"{name},{often_use},{webinar}, {satisfied}, {recommend}, {engaged}, {webinars2}, {updates}\n")```
* update this line so it now points are your new HTML file: ```return render_template("onboard_survey.html")```
* You should now test your code locally using the instructions listed above, complete full function testing by submitting the form
* NOTE: When you run the flask app locally, to find the page you just created edit the URL in your browser by adding your new route from the app.py file. Example http://127.0.0.1:5000/onboard-survey
* Once you have fully tested the new questionaire, go to the base.html file in the templates directory. Look to see if there is already a tile representing the form you have just created, if there is just edit the 'href' to point at your new app route or copy and paste an existing one and edit as desirec






