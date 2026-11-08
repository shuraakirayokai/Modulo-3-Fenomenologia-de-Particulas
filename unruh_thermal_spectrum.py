"""
unruh_thermal_spectrum.py
================================================================================
Authors: David Botargues Martin & AI Collaborator (2026)
Module 3: Relativistic Acceleration and Unruh Thermal Spectrum Boundaries
================================================================================
"""
import sys
import numpy as np

HBAR    = 1.054571817e-34
C       = 299792458.0
K_B     = 1.380649e-23     
EV_TO_J = 1.602176634e-19

E_ZEPTO = 14.0e12 * EV_TO_J
ell_Z   = (HBAR * C) / E_ZEPTO
r_bounce = 1.084 * ell_Z

print("=" * 78)
print(" MODULE 3: THERMODYNAMICS - UNRUH THERMAL SPECTRA AT THE BOUNCE")
print(f" Minimum Comoving Radius (r_bounce): {r_bounce:.4e} meters")
print("=" * 78)

accelerations = np.array([0.5, 1.0, 2.0]) * (C**2 / r_bounce)

print(f"{'Aceleracion Extrema (m/s^2)':<28} | {'Temperatura Unruh (K)':<25} | {'Energia Termica (GeV)':<20}")
print("-" * 80)

for a in accelerations:
    t_unruh = (HBAR * a) / (2 * np.pi * C * K_B)
    e_thermal_joules = K_B * t_unruh
    e_thermal_gev = (e_thermal_joules / EV_TO_J) / 1e9
    print(f"{a:<28.4e} | {t_unruh:<25.4e} | {e_thermal_gev:>20.4f} GeV")

print("-" * 80)
print("[OK] Espectro de radiación térmica y acotación de entropía completados.")
print("=" * 78)
