import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def hpc_resource_radar_split(cpu, ram, pfs_recv, pfs_send, power, image_path):
    plt.rcParams["axes.facecolor"] = "whitesmoke"
    angles = np.linspace(0.5 * np.pi, -1.5 * np.pi, len(ram), endpoint=False)
    ram = np.concatenate((ram, [ram[0]]))
    cpu = np.concatenate((cpu, [cpu[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    pfs_recv = np.concatenate((pfs_recv, [pfs_recv[0]]))
    pfs_send = np.concatenate((pfs_send, [pfs_send[0]]))
    power = np.concatenate((power, [power[0]]))

    fig = plt.figure(figsize=(7, 7), dpi=1000)
    ax = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")

    bin = 360 // 5

    ax.set_ylim(0, 100)
    ax.grid(True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines["polar"].set_color("lightgray")
    ax.spines["polar"].set_linewidth(0.5)
    ax.grid(color="lightgrey", linewidth=0.3)

    ax1 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax1.set_ylim(0, 100)
    ax1.patch.set_visible(False)
    ax1.grid("off")
    ax1.xaxis.set_visible(False)
    ax1.set_rlabel_position(90 - bin * 0)
    ax1.set_yticks([0, 20, 40, 60, 80, 100])
    ax1.yaxis.set_visible(False)
    ax1.tick_params(axis="y", colors="g", labelsize=7)
    ax1.yaxis.grid(color="lightgrey", linewidth=0.3)
    ax1.set_xticklabels([])
    ax1.spines["polar"].set_visible(False)

    ax2 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax2.set_ylim(0, 100)
    ax2.patch.set_visible(False)
    ax2.grid("off")
    ax2.xaxis.set_visible(False)
    ax2.set_rlabel_position(90 - bin * 2)
    ax2.set_yticks([0, 20, 40, 60, 80, 100])
    ax2.yaxis.set_visible(False)
    ax2.tick_params(axis="y", colors="b", labelsize=7)
    ax2.yaxis.grid(color="lightgrey", linewidth=0.3)
    ax2.set_xticklabels([])
    ax2.spines["polar"].set_visible(False)

    ax3 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax3.set_ylim(0, 100)
    ax3.patch.set_visible(False)
    ax3.grid("off")
    ax3.xaxis.set_visible(False)
    ax3.set_rlabel_position(90 - bin * 3)
    ax3.set_yticks([0, 20, 40, 60, 80, 100])
    ax3.yaxis.set_visible(False)
    ax3.tick_params(axis="y", colors="firebrick", labelsize=7)
    ax3.yaxis.grid(color="lightgrey", linewidth=0.3)
    ax3.set_xticklabels([])
    ax3.spines["polar"].set_visible(False)

    ax4 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax4.set_ylim(0, 100)
    ax4.patch.set_visible(False)
    ax4.grid("off")
    ax4.xaxis.set_visible(False)
    ax4.set_rlabel_position(90 - bin * 1)
    ax4.set_yticks([0, 20, 40, 60, 80, 100])
    ax4.yaxis.set_visible(False)
    ax4.tick_params(axis="y", colors="deeppink", labelsize=7)
    ax4.yaxis.grid(color="lightgrey", linewidth=0.3)
    ax4.set_xticklabels([])
    ax4.spines["polar"].set_visible(False)

    ax5 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax5.set_ylim(0, 100)
    ax5.patch.set_visible(False)
    ax5.grid("off")
    ax5.xaxis.set_visible(False)
    ax5.set_rlabel_position(90 - bin * 4)
    ax5.set_yticks([0, 20, 40, 60, 80, 100])
    ax5.yaxis.set_visible(False)
    ax5.tick_params(axis="y", colors="orange", labelsize=7)
    ax5.yaxis.grid(color="lightgrey", linewidth=0.3)
    ax5.set_xticklabels([])
    ax5.spines["polar"].set_visible(False)

    axtop = ax5
    axtop.plot(
        angles,
        list(map(lambda x: x * 20 / max(pfs_send) + 20, pfs_send)),
        color="deeppink",
        linestyle="-",
        label=f"I/O write(0-{round(max(pfs_send), 2)}GB)",
        linewidth=1.5,
    )
    axtop.plot(
        angles,
        list(map(lambda x: x * 20 / max(pfs_recv), pfs_recv)),
        "g-",
        label=f"I/O read(0-{round(max(pfs_recv), 2)}GB)",
        linewidth=1.5,
    )
    axtop.plot(
        angles,
        list(map(lambda x: x * 20 / max(ram) + 40, ram)),
        "b-",
        label=f"RAM(0-{round(max(ram), 2)}GB)",
        linewidth=1.5,
    )
    axtop.plot(
        angles,
        list(map(lambda x: x / 5 + 60, cpu)),
        color="firebrick",
        linestyle="-",
        label=f"CPU(0-{round(max(cpu), 2)}%)",
        linewidth=1.5,
    )
    axtop.plot(
        angles,
        list(map(lambda x: x * 20 / max(power) + 80, power)),
        color="orange",
        linestyle="-",
        label=f"Power(0-{round(max(power), 2)}W)",
        linewidth=1.5,
    )

    matplotlib.rcParams["agg.path.chunksize"] = 180000
    matplotlib.rcParams["path.simplify_threshold"] = 1
    fig.legend(fontsize=8)
    fig.savefig(image_path)
    return True


if __name__ == "__main__":
    cpu, ram, pfs_recv, pfs_send, power = [], [], [], [], []
    with open("example.txt", "r") as infile:
        for line in infile.readlines():
            if line[:3] == "ram":
                tot = line.split()[2]
                free = line.split()[4]
                used = (int(tot) - int(free)) * 4 * 1024 / 1024 / 1024 / 1024
                ram.append(used)
            elif line[:3] == "pfs":
                recv = int(line.split()[3]) / 1024 / 1024 / 1024
                send = int(line.split()[5]) / 1024 / 1024 / 1024
                pfs_recv.append(recv)
                pfs_send.append(send)
            elif line[:7] == "cpu_tot":
                total = (
                    float(line.split()[2])
                    + float(line.split()[4])
                    + float(line.split()[6])
                )
                cpu.append(total)
            elif line[:5] == "Power":
                p = int(line.split()[1])
                power.append(p)
    hpc_resource_radar_split(cpu, ram, pfs_recv, pfs_send, power, "example_split.png")
