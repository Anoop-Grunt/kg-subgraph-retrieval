import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("results.csv")

# Separate BFS (baseline)
bfs = df[df["beam"] == "BFS"]
df = df[df["beam"] != "BFS"]

# Convert beam to int
df["beam"] = df["beam"].astype(int)

# Plot
plt.figure(figsize=(8, 6))

for hops in sorted(df["hops"].unique()):
    subset = df[df["hops"] == hops].sort_values("beam")
    
    plt.plot(
        subset["edge_reduction"],
        subset["recall"],
        marker="o",
        label=f"{hops}-hop",
    )

# BFS reference
plt.scatter(
    bfs["edge_reduction"],
    bfs["recall"],
    color="black",
    marker="x",
    s=100,
    label="BFS (baseline)",
)

plt.xlabel("Edge Reduction")
plt.ylabel("Recall")
plt.title("Recall vs Edge Reduction (TransE Beam Pruning)")
plt.legend()
plt.grid(True)

plt.tight_layout()

# ✅ Save figure
plt.savefig("result_plot.png", dpi=300)

plt.show()
