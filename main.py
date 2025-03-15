import os

from adsorber import Adsorber
import matplotlib.pyplot as plt

def main():
    # parameters
    C_in = 10  # mg/L (initial ciprofloxacin concentration)
    PAC = 0.5  # g (PAC dosage)
    V = 1  # L (reactor volume)
    Qmax = 100  # mg/g (maximum adsorption capacity)
    KL = 0.05  # L/mg (Langmuir constant)

    # adsorption
    adsorber = Adsorber(C_in, PAC, V, Qmax, KL)

    tspan = 100
    time, c_sol = adsorber.reactor(tspan)

    # get directory
    root = os.getcwd()
    save_dir = os.path.join(root, "projects", "waste-water-filtration-antibiotics")

    # visualize concentration
    plt.plot(time, c_sol)
    plt.xlabel("Time [-]")
    plt.ylabel("Concenctration [mg/L]")
    plt.title("C vs. T in Black Box Adsorber")

    save_fig = os.path.join(save_dir, "concentration_time.png")
    plt.savefig(save_fig)

if __name__ == '__main__':
    main()