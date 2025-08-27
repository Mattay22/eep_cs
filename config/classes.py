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
        img_base64 = base64.b64encode(buf.read()).decode("utf-8")
        
        return img_base64
