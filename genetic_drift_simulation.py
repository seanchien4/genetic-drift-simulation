import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def genetic_drift(pop_size, generations, simulations=10, start_freq=0.5, save_png=False, dpi=300):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)  # Smaller interactive plot window
    ax.set_xlim(0, generations)  # Fix x-axis to generations
    ax.set_ylim(0, 1)  # Fix y-axis between 0 and 1
    ax.set_xlabel("Generations")
    ax.set_ylabel("Allele Frequency")
    ax.set_title("Genetic Drift Simulation")

    all_simulations = [[] for _ in range(simulations)]
    lines = [ax.plot([], [])[0] for _ in range(simulations)]

    # Correct: Create the correct output folder
    output_folder = "drift_simulation"
    if save_png and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for gen in range(generations + 1):  # FIX: Ensure it reaches the final generation
        for sim in range(simulations):
            if gen == 0:
                all_simulations[sim].append(start_freq)
            else:
                new_freq = np.random.binomial(2 * pop_size, all_simulations[sim][-1]) / (2 * pop_size)
                all_simulations[sim].append(new_freq)

            lines[sim].set_xdata(range(len(all_simulations[sim])))
            lines[sim].set_ydata(all_simulations[sim])

        plt.pause(0.05)

        if save_png:  # Save each frame as a PNG file with high resolution
            filename = os.path.join(output_folder, f"frame_{gen:03d}.png")  # Ensure last frame is saved
            fig.savefig(filename, dpi=dpi)
            print(f"Saved: {filename}")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate genetic drift.")
    parser.add_argument("-p", "--pop_size", type=int, required=True, help="Population size")
    parser.add_argument("-g", "--generations", type=int, required=True, help="Number of generations")
    parser.add_argument("-s", "--simulations", type=int, default=10, help="Number of simulations (default: 10)")
    parser.add_argument("-f", "--start_freq", type=float, default=0.5, help="Starting allele frequency (default: 0.5)")
    parser.add_argument("--save_png", action="store_true", help="Save each frame as a PNG file")
    parser.add_argument("--dpi", type=int, default=300, help="DPI (resolution) for the saved plots (default: 300)")

    args = parser.parse_args()
    genetic_drift(args.pop_size, args.generations, args.simulations, args.start_freq, args.save_png, args.dpi)
