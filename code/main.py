from data_generation import generate_mixed_gaussian, generate_U_statistic
from statistics_calc import calc_EZ_DZ
from visualization import plot_histogram
import os

# 确保同级目录下的picture文件夹存在（不存在则创建）
os.makedirs('picture', exist_ok=True)

# ---------------------- Task 1: Mixed Gaussian Distribution & Histogram ----------------------
# Set parameters (adjustable)
mu1, sigma1 = 0, 1  # Mean and standard deviation of X
mu2, sigma2 = 5, 2  # Mean and standard deviation of Y
p = 0.5  # Probability parameter of Bernoulli distribution
sample_size = 5000  # Number of samples

# Generate mixed Gaussian distribution data Z = X + ηY
Z = generate_mixed_gaussian(mu1, sigma1, mu2, sigma2, p, sample_size)

# 保存图片到同级的picture文件夹
plot_histogram(
    data=Z,
    title=f'Histogram of Mixed Gaussian Distribution (μ₁={mu1}, σ₁={sigma1}, μ₂={mu2}, σ₂={sigma2}, p={p})',
    xlabel='Value of Z',
    ylabel='Frequency Density',
    save_path='picture/mixed_gaussian_hist.png'  # 路径改为picture文件夹
)

# ---------------------- Task 2: U-statistic & Central Limit Theorem Verification ----------------------
# Calculate theoretical expectation (EZ) and variance (DZ)
EZ, DZ = calc_EZ_DZ(mu1, sigma1, mu2, sigma2, p)
print(f"Theoretical Expectation E[Z] = {EZ:.4f}")
print(f"Theoretical Variance D[Z] = {DZ:.4f}")

# Different values of n (sample size per group, adjustable)
n_values = [2, 3, 4, 5, 10, 20, 50, 100, 5000]

for n in n_values:
    # Generate U-statistic: U = (ΣZ_j - n·EZ) / √(n·DZ)
    U_statistic = generate_U_statistic(Z, EZ, DZ, n)

    # 保存图片到同级的picture文件夹
    plot_histogram(
        data=U_statistic,
        title=f'Histogram of U-statistic (n={n})',
        xlabel='Value of U',
        ylabel='Frequency Density',
        save_path=f'picture/U_statistic_n{n}.png'  # 路径改为picture文件夹
    )