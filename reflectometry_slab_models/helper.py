import numpy as np
from scipy.stats import norm

def sld_with_roughness(beta: np.ndarray, d: np.ndarray, sigma: np.ndarray):
    """
    Determine the scattering length density profile 
    shape, with roughness present.
    
    :param beta: array of scattering length densities, shape: (number_layers)
    :param d: layer thicknesses, shape: (number_layers)
    :param sigma: interfacial roughnesses, shape (number_layers-1)
    :return: z-dimension and the SLD profile
    """
    dist = np.cumsum(d[:-1])
    zstart = -5 - 4 * sigma[1]
    zend = 5 + dist[-1] + 4 * sigma[-1]
    zed = np.linspace(zstart, zend, 500)
    sld = np.ones_like(zed, dtype=float) * beta[0].real
    delta_rho = beta[1:].real - beta[:-1].real    
    def step_f(z, scale, loc):
        new_z = z - loc
        f = np.ones_like(new_z) * 0.5
        f[new_z <= -scale] = 0
        f[new_z >= scale] = 1
        return f
    erf_f = norm.cdf
    for i in range(beta.shape[0] - 1):
        f = erf_f
        if sigma[i] == 0:
            f = step_f
        sld += delta_rho[i] * f(zed, scale=sigma[i], loc=dist[i])
    return zed, sld