def calc_EZ_DZ(mu1, sigma1, mu2, sigma2, p):
    """计算混合高斯分布的理论期望EZ和方差DZ
    公式推导：
    E[Z] = E[X + ηY] = E[X] + p·E[Y]
    D[Z] = E[Z²] - (E[Z])²，其中E[Z²] = E[X² + 2ηXY + η²Y²] = E[X²] + p·E[Y²]
    """
    EX, EY = mu1, mu2
    VarX, VarY = sigma1 ** 2, sigma2 ** 2

    EZ = EX + p * EY

    EX2 = VarX + EX ** 2
    EY2 = VarY + EY ** 2
    EZ2 = EX2 + p * EY2
    DZ = EZ2 - EZ ** 2

    return EZ, DZ