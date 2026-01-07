def recommend_best_model(results_df):
    best_accuracy = results_df.sort_values("R2 Score", ascending=False).iloc[0]
    best_energy = results_df.sort_values("Training Time (s)").iloc[0]

    return {
        "Best Accuracy Model": best_accuracy["Model"],
        "Best Energy Efficient Model": best_energy["Model"]
    }
