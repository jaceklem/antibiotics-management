import os

from adsorber import Adsorber
import matplotlib.pyplot as plt

def main():
    # parameters
    C_in = 100  # initial ciprofloxacin concentration [mg/L]
    PAC = 0.5  # PAC dosage [mg]
    V = 1  # reactor volume [L]
    Qmax = 100  # maximum adsorption capacity [mg/g]
    KL = 0.05 # Langmuir constant [L/mg]
    k_ext = 1e-4 # external mf [1/s]
    k_int = 1e-6 # internal mf [1/s]
    A = 10 # surface area [m2]

    # adsorption
    adsorber = Adsorber(C_in, PAC, V, Qmax, KL, k_ext, k_int, A)

    tspan = 4000
    time, c_sol = adsorber.reactor(tspan)

    # get directory
    root = os.getcwd()
    save_dir = os.path.join(root, "projects", "waste-water-filtration-antibiotics")

    # visualize concentration
    plt.plot(time, c_sol)
    plt.xlabel("Time [-]")
    plt.ylabel("Concenctration [mg/L]")
    plt.title("C vs. t in Black Box Adsorber")

    save_fig = os.path.join(save_dir, "concentration_time.png")
    plt.savefig(save_fig)

if __name__ == '__main__':
    main()