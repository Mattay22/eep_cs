from flask import Flask,render_template_string
import pandas as pd
from matplotlib.figure import Figure
import io
import base64

class Chart:
    """Class to make charts"""
    def __init__(self, source, column, title, xlabel, ylabel):
        self.source = source
        self.column = column
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def create_chart(self):
        df = pd.read_csv(self.source)
        counts = df[self.column].value_counts().sort_index()
        fig = Figure()
        ax = fig.subplots()
        counts.plot(kind="bar", color="skyblue", ax=ax)
        ax.set_title(self.title)
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode("ascii")

        return f"""
            <h2>Survey Results</h2>
            <img src="data:image/png;base64,{img_base64}" alt="Chart">
        """

graph1 = Chart("responses.csv", "time_taken", "Time taken to onboard", "Time", "Number of Responses")
graph2 = Chart("responses.csv", "confidence", "Confidence Levels", "Confidence Value", "Number of Responses")

app = Flask(__name__)

@app.route("/")

def dashboard():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>GitLab Metrics Dashboard</title>
      <style>
        body {
          background-color: #2c2c2c;
          color: #f0f0f0;
          font-family: 'Segoe UI', sans-serif;
          padding: 40px;
        }
        h1 {
          color: #fc6d26;
          text-align: center;
        }
        .metric-box {
          background-color: #3c3c3c;
          border-left: 6px solid #fc6d26;
          padding: 20px;
          margin: 20px auto;
          max-width: 600px;
          border-radius: 8px;
        }
        .metric-title {
          font-size: 1.2em;
          margin-bottom: 10px;
        }
        .metric-value {
          font-size: 2em;
          font-weight: bold;
        }
        .chart {
          margin-top: 40px;
          text-align: center;
        }
        .bar {
          display: inline-block;
          width: 40px;
          margin: 0 5px;
          background-color: #fc6d26;
          border-radius: 4px 4px 0 0;
        }
        .bar-label {
          margin-top: 5px;
          font-size: 0.9em;
        }
      </style>
    </head>
    <body>
      <h1>🚀 GitLab Metrics Dashboard</h1>

      <div class="metric-box">
        <div class="metric-title">Pipeline Success Rate</div>
        <div class="metric-value">92.4%</div>
      </div>

      <div class="metric-box">
        <div class="metric-title">Total Commits This Week</div>
        <div class="metric-value">134</div>
      </div>

      <div class="chart">
        <h2>📊 Commits Per Day</h2>
        <div style="height: 150px;">
          <div class="bar" style="height: 80px;"></div>
          <div class="bar" style="height: 120px;"></div>
          <div class="bar" style="height: 100px;"></div>
          <div class="bar" style="height: 60px;"></div>
          <div class="bar" style="height: 140px;"></div>
          <div class="bar" style="height: 90px;"></div>
          <div class="bar" style="height: 70px;"></div>
        </div>
        <div class="bar-label">Mon Tue Wed Thu Fri Sat Sun</div>
      </div>
    </body>
    </html>
    """
    return render_template_string(html)
@app.route("/")
def display_chart():
    chart1_html = graph1.create_chart()
    chart2_html = graph2.create_chart()
    return f"""
        <html>
            <head><title>Survey Dashboard</title></head>
            <body>
                {chart1_html}
                <hr>
                {chart2_html}
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
