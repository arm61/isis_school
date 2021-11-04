from typing import Tuple
import numpy as np
from scipy.stats import norm


def step_f(z: np.ndarray, scale: float, loc: float) -> np.ndarray:
    """    
    :param z: z-dimension
    :param scale: width of step function, always 0
    :param loc: position of step
    :return: positioned step function
    """
    new_z = z - loc
    f = np.ones_like(new_z) * 0.5
    f[new_z <= -scale] = 0
    f[new_z >= scale] = 1
    return f


def sld_with_roughness(beta: np.ndarray, d: np.ndarray, sigma: np.ndarray) -> Tuple[np.ndarray]:
    """
    Determine the scattering length density profile shape, with roughness present.
    
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
    erf_f = norm.cdf
    for i in range(beta.shape[0] - 1):
        f = erf_f
        if sigma[i] == 0:
            f = step_f
        sld += delta_rho[i] * f(zed, scale=sigma[i], loc=dist[i])
    return zed, sld


def microslicing(beta: np.ndarray, d: np.ndarray, sigma: np.ndarray, slice_size: float=0.5) -> Tuple[np.ndarray]:
    """
    Creates a microslab representation of the scattering length density profile.
    
    :param beta: scattering length densitys, shape: (number_layers)
    :param d: layer thicknesses, shape: (number_layers)
    :param sigma: interfacial roughnesses, shape: (number_layers-1)
    :param slice_size: Thickness of each slab in the micro-slab representation
    Returns
    -------
    micro_slabs : np.ndarray
        The micro-slab representation of the model. See the
        `Structure.slabs` method for a description of the array.
    """
    dist = np.cumsum(d[:-1])
    zstart = -20.0 - 8 * sigma[0]
    zend = 20.0 + dist[-1] + 8 * sigma[0]
    nsteps = int((zend - zstart) / slice_size + 1)
    zed = np.linspace(zstart, zend, num=nsteps)
    sld = np.ones_like(zed, dtype=float) * beta[0].real
    delta_rho = beta[1:].real - beta[:-1].real
    for i in range(len(d) - 1):
        f = norm.cdf
        if sigma[i] == 0:
            f = step_f
        p = f(zed, scale=sigma[i], loc=dist[i])
        sld += delta_rho[i] * p
    return zed + 0.5 * slice_size, sld


def normal_wavevectors(q: np.ndarray, beta: np.ndarray) -> np.ndarray:
    """
    :param q: array of q-wavevectors, shape: (number_q)
    :param beta: array of scattering length densities, shape: (number_layers)
    :return: wavevectors normal to surface, shape: (number_q, number_layers)
    """
    k0 = 0.5 * q[:, np.newaxis] 
    kn = np.sqrt(k0 ** 2 - 4.0 * np.pi * (beta - beta[0]))
    return kn


def fresnel_reflectance(kn: np.ndarray) -> np.ndarray:
    """
    :param kn: wavevectors normal to surface, shape: (number_q, number_layers)
    :return: fresnel reflectance between layers, shape: (number_q, number_layers-1)
    """
    return (kn[:, :-1] - kn[:, 1:]) / (kn[:, :-1] + kn[:, 1:])


def fresnel_reflectance_with_roughness(kn: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    """
    :param kn: wavevectors normal to surface, shape: (number_q, number_layers)
    :param sigma: interfacial roughness widths, shape: (number_layers-1)
    :return: fresnel reflectance between layers, shape: (number_q, number_layers-1)
    """
    return (kn[:, :-1] - kn[:, 1:]) / (kn[:, :-1] + kn[:, 1:]) * np.exp(-2 * kn[:, :-1] * kn[:, 1:] * sigma ** 2)


def phase_factor(kn:np.ndarray, d: np.ndarray) -> np.ndarray:
    """
    :param kn: wavevectors normal to surface, shape: (number_q, number_layers)
    :param d: layer thicknesses, shape: (number_layers)
    :return: phase factor, shape: (number_q, number_layers)
    """
    phi_t = kn * d
    phi_t[:, 0] = np.zeros(kn.shape[0])
    return phi_t


def characteristic_matrices(r: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """
    :param r: Fresnel reflectances, shape: (number_q, number_layers-1)
    :param phi: phase factors, shape: (number_q, number_layers-1)
    :returns: characteristic matrices, shape: (2, 2, number_q, number_layers-1)
    """
    M = np.ones((2, 2, *r.shape), dtype=complex)
    M[0, 0, :, 1:] = np.exp(1j * phi[:, 1:-1])
    M[1, 1, :, 1:] = np.exp(-1j * phi[:, 1:-1])
    M[1, 0] = r * M[0, 0]
    M[0, 1] = r * M[1, 1]
    return M


def resultant_matrix(M: np.ndarray) -> np.ndarray:
    """
    :param M: characteristic matrices, shape: (2, 2, number_q, number_layers-1)
    :return: resultant matrix, shape: (2, 2, number_q)
    """
    B = M[:, :, :, 0]
    for i in range(1, M.shape[-1]):
        p0 = B[0, 0] * M[0, 0, :, i] + B[1, 0] * M[0, 1, :, i]
        p1 = B[0, 0] * M[1, 0, :, i] + B[1, 0] * M[1, 1, :, i]
        B[0, 0] = p0
        B[1, 0] = p1

        p0 = B[0, 1] * M[0, 0, :, i] + B[1, 1] * M[0, 1, :, i]
        p1 = B[0, 1] * M[1, 0, :, i] + B[1, 1] * M[1, 1, :, i]
        B[0, 1] = p0
        B[1, 1] = p1
    return B


def reflectivity(B: np.ndarray) -> np.ndarray:
    """
    :param B: resultant matrix, shape: (2, 2, number_q)
    :return: reflectivity, shape: (number_q)
    """
    r = B[0, 1] / B[0, 0]
    return np.real(r * np.conj(r))


def abeles(q: np.ndarray, beta: np.ndarray, d: np.ndarray) -> np.ndarray:
    """
    Use Abeles to find reflectometry data. 
    
    :param q: array of q-wavevectors, shape: (number_q)
    :param beta: array of scattering length densities, shape: (number_layers)
    :param d: layer thicknesses, shape: (number_layers)
    :returns: calculated reflectivity, shape: (number_q)
    """
    kn = normal_wavevectors(q, beta)
    phi = phase_factor(kn, d)
    r = fresnel_reflectance(kn)
    M = characteristic_matrices(r, phi)
    B = resultant_matrix(M)
    return reflectivity(B)


def abeles_with_roughness(q: np.ndarray, beta: np.ndarray, d: np.ndarray, sigma:np.ndarray) -> np.ndarray:
    """
    Use Abeles with some interfacial roughness to find reflectometry data.
    
    :param q: array of q-wavevectors, shape: (number_q)
    :param beta: array of scattering length densities, shape: (number_layers)
    :param d: layer thicknesses, shape: (number_layers)
    :param sigma: interfacial roughnesses, shape: (number_layers-1)
    :returns: calculated reflectivity, shape: (number_q)
    """
    kn = normal_wavevectors(q, beta)
    phi = phase_factor(kn, d)
    r = fresnel_reflectance_with_roughness(kn, sigma)
    M = characteristic_matrices(r, phi)
    B = resultant_matrix(M)
    return reflectivity(B)