import numpy as np
import scipy.optimize as optimize
import scipy.integrate as integrate
import matplotlib.pyplot as plt

class Adsorber:
    def __init__(self, C0, PAC, Vr, Qmax, KL):
        self.C0 = C0  # Initial concentration (mg/L)
        self.PAC = PAC  # PAC dosage (g)
        self.Vr = Vr  # Reactor volume (L)
        self.Qmax = Qmax  # Maximum adsorption capacity (mg/g)
        self.KL = KL  # Langmuir constant (L/mg)


    def reactor(self, tspan):
        t = np.linspace(0, tspan, tspan + 1)

        # Solve for Ce (outlet concentration)
        c_sol = integrate.odeint(self.mass_balance, self.C0, t)
        return t, c_sol.flatten()

    def mass_balance(self, C, tspan):
        # Calculate adsorption capacity at equilibrium
        q_ads = self.langmuir(C)

        return - (q_ads * self.PAC / self.Vr)

    def langmuir(self, Ce):
        return (self.Qmax * self.KL * Ce) / (1 + self.KL * Ce)