import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("twitter_training.csv")

df.columns = ["ID", "Topic", "Sentiment", "Text"]

df = df.dropna()

sentiment_count = df["Sentiment"].value_counts()

print("\n" + "="*50)
print("SOCIAL MEDIA SENTIMENT ANALYSIS")
print("="*50)

print("\nSentiment Distribution")
print("-"*30)
print(sentiment_count)

print("\nTotal Records:", len(df))

print("\nAnalysis Completed Successfully!")

plt.figure(figsize=(8,5))
sentiment_count.plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,7))
sentiment_count.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sentiment Overview")
plt.tight_layout()
plt.show()