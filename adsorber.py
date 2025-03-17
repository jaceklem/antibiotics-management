import os
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

class Adsorber:
    def __init__(self, C0, qt0, Fv, Vr, Qmax, KL, k2, L, Mm, tspan):
        self.C0 = C0  # Initial concentration (mg/L)
        self.qt0 = qt0  # Initial adsorbed amount (mg/g)
        self.Fv = Fv  # Flow rate (L/min)
        self.Vr = Vr  # Reactor volume (L)
        self.Qmax = Qmax  # Max adsorption capacity (mg/g)
        self.KL = KL  # Langmuir constant (L/mg)
        self.k2 = k2  # Pseudo-second-order rate constant
        self.L = L  # Contactor length
        self.Mm = Mm  # Molecular weight or characteristic parameter
        self.tspan = tspan  # Time span for simulation

    def reactor(self):
        """Solves the mass balance ODE"""
        t = np.linspace(0, self.tspan, self.tspan + 1)
        sol = integrate.odeint(self.mass_balance, [self.C0, self.qt0], t)
        return t, sol[:, 0], sol[:, 1]  # Return time, concentration, and qt

    def mass_balance(self, cc, t):
        """Defines the system of ODEs for concentration and adsorption"""
        c, qt = cc

        qe = self.langmuir(c)

        if qe == 0:
            return [0, 0]

        # a = 1 / (self.k2 * qe)
        # initRate = 1 / a
        # rate = initRate * (1 - qt / qe)

        # pseudo second order
        dqdt = (self.k2 * qe**2) / (1 + self.k2 * qe * t)

        dcdt = self.Fv * (self.C0 - c) / self.Vr - dqdt * self.L / self.Mm
        # dqdt = rate

        return [dcdt, dqdt]

    def langmuir(self, Ce):
        """Langmuir isotherm model"""
        return (self.Qmax * self.KL * Ce) / (1 + self.KL * Ce)
    
    def plot_result(self):
        """Runs the simulation and plots results"""
        t, c_sol, qt_sol = self.reactor()
        plt.figure(figsize=(8, 5))
        plt.plot(t, c_sol, label="C (mg/L)", color='b')
        plt.plot(t, qt_sol, label="qt (mg/g)", color='r')
        plt.xlabel("Time (min)")
        plt.ylabel("Concentration & Adsorption")
        plt.legend()
        plt.title("Adsorption Process Over Time")

        save_fig = os.path.join(os.getcwd(), "concentration_time.png")
        plt.savefig(save_fig)