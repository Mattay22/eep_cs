from flask import Flask, render_template, request
from config.classes import Chart
import base64
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")  # Your main layout

@app.route("/onboard-survey", methods=["GET", "POST"])
def onboard_survey():
    if request.method == "POST":
        name = request.form["name"]
        completed_onboarding = request.form["completed_onboarding"]
        time_taken = request.form["time_taken"]
        confidence = request.form["confidence"]
        goals = request.form["goals"]
        rate_onboarding = request.form["rate_onboarding"]
        with open("onboard_survey.csv", "a") as f:
            f.write(f"{name},{completed_onboarding},{time_taken}, {confidence}, {goals}, {rate_onboarding}\n")
        return f"<h3>Thanks, {name}! Your feedback has been recorded.</h3>"

    return render_template("onboard_survey.html")

@app.route("/customer-engagement", methods=["GET", "POST"])
def customer_survey():
    if request.method == "POST":
        name = request.form["name"]
        often_use = request.form["often_use"]
        webinar = request.form["webinar"]
        satisfied = request.form["satisfied"]
        recommend = request.form["recommend"]
        engaged = request.form["engaged"]
        webinars2 = request.form["webinars2"]
        updates = request.form["updates"]
        with open("customer_engagement.csv", "a") as f:
            f.write(f"{name},{often_use},{webinar}, {satisfied}, {recommend}, {engaged}, {webinars2}, {updates}\n")
        return f"<h3>Thanks, {name}! Your feedback has been recorded.</h3>"

    return render_template("customer_engagement.html")

@app.route("/customer-satisfaction", methods=["GET", "POST"])
def satisfaction_survey():
    if request.method == "POST":
        name = request.form["name"]
        how_satisifed = request.form["how_satisifed"]
        would_recommend = request.form["would_recommend"]
        like_most = request.form["like_most"]
        improve = request.form["improve"]
        with open("customer_satisfaction.csv", "a") as f:
            f.write(f"{name}, {how_satisifed}, {would_recommend}, {like_most}, {improve}\n")
        return f"<h3>Thanks, {name}! Your feedback has been recorded.</h3>"

    return render_template("customer_satisfaction.html")

@app.route('/admin')
def admin():
    graph1 = Chart("responses.csv", "time_taken", "Time taken to onboard", "Time", "Number of Responses")
    graph2 = Chart("responses.csv", "confidence", "Confidence Levels", "Confidence Value", "Number of Responses")
    graph3 = Chart("responses.csv", "rate_onboarding", "Rate Onboarding 1-5", "Rating", "Number of Responses")

    chart1 = graph1.create_chart()
    chart2 = graph2.create_chart()
    chart3 = graph3.create_chart()

    return render_template("admin.html",
                           chart1=chart1,
                           chart2=chart2,
                           chart3=chart3,
                           title1=graph1.title,
                           title2=graph2.title,
                           title3=graph3.title)


if __name__ == "__main__":
    app.run(debug=True)
