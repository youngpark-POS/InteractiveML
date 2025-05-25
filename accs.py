import numpy as np

accs1 = [90.875,91.25,90.375,90.0,90.75,90.875,89.0,93.5,92.375,92.5,91.75,90.625,92.25,92.875,92.875,90.625,90.5,92.125,90.5,91.375]
accs2 = [89.88,89.62,91.38,93.25,90.38,90.75,91.00,90.00,92.75,89.50,92.38,90.00,92.50]
all_accs = accs1 + accs2

# Print average and standard deviation of accuracies
print(f"Average accuracy over 33 iterations: {np.mean(all_accs):.2f}%")
print(f"Standard deviation of accuracies: {np.std(all_accs):.2f}%")