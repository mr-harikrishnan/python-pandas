import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.metrics import roc_curve, roc_auc_score

passDf = pd.read_csv("./medium_large_drifted_columns_pass_datas.csv")

failDf = pd.read_csv("./medium_large_drifted_columns_fail_datas.csv")


# Target

passDf["target"] = 0
failDf["target"] = 1


# Combine data

combined_df = pd.concat([passDf, failDf], ignore_index=True)


# Get features dynamically

features = [column for column in passDf.columns if column != "target"]


# ONE LARGE FIGURE

plt.figure(figsize=(18, 14))


# Different color for every feature

colors = plt.cm.tab10(np.linspace(0, 1, len(features)))


# ROC curve for every feature

for feature, color in zip(features, colors):

    feature_df = combined_df[[feature, "target"]].dropna()

    x = feature_df[feature]
    y = feature_df["target"]

    # Convert feature to numeric

    x = pd.to_numeric(x, errors="coerce")

    # Remove invalid values

    valid_rows = x.notna()

    x = x[valid_rows]
    y = y[valid_rows]

    # Skip if only one target class exists

    if y.nunique() < 2:

        print(f"Skipping {feature}: only one target class available.")

        continue

    # ROC values

    fpr, tpr, thresholds = roc_curve(y, x)

    # AUC

    auc = roc_auc_score(y, x)

    print(f"{feature} : {auc:.4f}")

    # Plot ROC curve

    plt.plot(fpr, tpr, color=color, linewidth=1.5, label=f"{feature} (AUC = {auc:.3f})")


# Random classifier line

plt.plot(
    [0, 1], [0, 1], linestyle="--", linewidth=1, color="gray", label="Random Classifier"
)


# Axis

plt.xlim(0, 1)
plt.ylim(0, 1)


plt.xlabel("False Positive Rate", fontsize=13, fontweight="bold", labelpad=12)


plt.ylabel("True Positive Rate", fontsize=13, fontweight="bold", labelpad=12)


# Title

plt.title(
    "ROC Curves for All Manufacturing Features", fontsize=17, fontweight="bold", pad=20
)


# Grid

plt.grid(True, linestyle="--", alpha=0.35)


# Legend

plt.legend(fontsize=11, loc="lower right", frameon=True)


# Adjustable spacing

plt.subplots_adjust(left=0.08, right=0.98, bottom=0.10, top=0.90)


# Save

output_path = "./roc_threshold_plots/all_features_roc_curve.png"

os.makedirs("./roc_threshold_plots", exist_ok=True)


plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0.3)


plt.show()

plt.close()


# Correlation Matrix

correlation = combined_df[features].corr()


# Correlation Figure

plt.figure(figsize=(18, 14))


plt.imshow(correlation, cmap="RdBu_r", vmin=-1, vmax=1)


# Axis labels

plt.xticks(range(len(features)), features, rotation=90, fontsize=10)

plt.yticks(range(len(features)), features, fontsize=10)


# Color bar

cbar = plt.colorbar()

cbar.set_label("Correlation", fontsize=12, fontweight="bold")


# Title

plt.title("Feature Correlation Matrix", fontsize=17, fontweight="bold", pad=20)


# Show correlation values

for i in range(len(features)):

    for j in range(len(features)):

        value = correlation.iloc[i, j]

        plt.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=8)


# Adjustable spacing

plt.subplots_adjust(left=0.08, right=0.78, bottom=0.25, top=0.90)


# Save

correlation_output_path = "./roc_threshold_plots/feature_correlation.png"


plt.savefig(correlation_output_path, dpi=300, bbox_inches="tight", pad_inches=0.3)


plt.show()

plt.close()
