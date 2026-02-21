import numpy as np

def generate_mixed_gaussian(mu1, sigma1, mu2, sigma2, p, size=5000):
    """生成混合高斯分布随机数 Z = X + ηY，其中η服从伯努利分布B(p)"""
    eta = np.random.binomial(n=1, p=p, size=size)
    X = np.random.normal(loc=mu1, scale=sigma1, size=size)
    Y = np.random.normal(loc=mu2, scale=sigma2, size=size)
    Z = X + eta * Y
    return Z

def generate_U_statistic(Z, EZ, DZ, n, num_groups=1000):
    """生成U统计量：U = (1/√(nDZ)) * (ΣZ_j - nEZ)"""
    U_list = []
    for _ in range(num_groups):
        sample = np.random.choice(Z, size=n, replace=True)
        sum_Z = np.sum(sample)
        U = (sum_Z - n * EZ) / (np.sqrt(n * DZ))
        U_list.append(U)
    return np.array(U_list)