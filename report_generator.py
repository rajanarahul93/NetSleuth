import pandas as pd
import matplotlib.pyplot as plt

def generate_report():
    try:
        df = pd.read_csv("packet_analysis.csv")
        print("Generating report...")
        print(df)
        
        # Visualization: Bar chart of metrics
        df.plot(x="Metric", y="Count", kind="bar", figsize=(10, 6))
        plt.title("Network Traffic Analysis")
        plt.xlabel("Metric")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig("analysis_report.png")
        print("Report saved as analysis_report.png")
    except FileNotFoundError:
        print("No analysis data found! Run the sniffer first.")

if __name__ == "__main__":
    generate_report()
