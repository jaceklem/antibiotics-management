import numpy as np
import scipy.optimize as optimize
import scipy.integrate as integrate
import matplotlib.pyplot as plt

class Adsorber:
    def __init__(self, C0, PAC, Vr, Qmax, KL, k_ext, k_int, A):
        self.C0 = C0  # Initial concentration (mg/L)
        self.PAC = PAC  # PAC dosage (g)
        self.Vr = Vr  # Reactor volume (L)
        self.Qmax = Qmax  # Maximum adsorption capacity (mg/g)
        self.KL = KL  # Langmuir constant (L/mg)

        # mass transfer coeff
        self.k_ext = k_ext
        self.k_int = k_int

        self.A = A # surface area

    def reactor(self, tspan):
        t = np.linspace(0, tspan, tspan + 1)

        # Solve for Ce (outlet concentration)
        c_sol = integrate.odeint(self.mass_balance, self.C0, t)

        return t, c_sol.flatten()

    def mass_balance(self, C, tspan):
        # Calculate adsorption capacity at equilibrium
        q_ads = self.langmuir(C)

        # equilibrium concentration
        Ceq = self.langmuir_inverse(q_ads)

        # external mass transfer
        ext_mf = (self.k_ext * self.A *(C - Ceq)) / self.Vr

        # internal mass transfer
        int_mf = (self.k_int * self.A *(C - Ceq)) / self.Vr

        # dCdt
        dCdt = - ext_mf - int_mf

        return dCdt

    def langmuir(self, Ce):
        return (self.Qmax * self.KL * Ce) / (1 + self.KL * Ce)
    
    def langmuir_inverse(self, q_ads):
        return q_ads / (self.KL * self.Qmax  - q_ads)