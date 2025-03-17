from adsorber import Adsorber
import numpy as np

def main():
    # parameters
    C0 = 10
    qt0 = 0
    Fv = 1
    Vr = 100
    Qmax = 73
    KL = 0.1
    k2 = 3e-3
    L = 300
    Mm = 200

    tspan = 10000

    # adsorption
    adsorber = Adsorber(C0, qt0, Fv, Vr, Qmax, KL, k2, L, Mm, tspan)
    adsorber.plot_result()

if __name__ == '__main__':
    main()