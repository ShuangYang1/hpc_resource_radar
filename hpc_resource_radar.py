import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def hpc_resource_radar(cpu, ram, pfs_recv, pfs_send, power, image_path):
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
    ax.plot(angles, cpu, color="darkred", linestyle="-", label="CPU", linewidth=1.0)
    ax.plot(
        angles,
        list(map(lambda x: x * 100 / max(ram), ram)),
        "b-",
        label="RAM",
        linewidth=1.0,
    )
    ax.plot(
        angles,
        list(map(lambda x: x * 100 / max(pfs_recv), pfs_recv)),
        "g-",
        label="I/O read",
        linewidth=1.0,
    )
    ax.plot(
        angles,
        list(map(lambda x: x * 100 / max(pfs_send), pfs_send)),
        color="deeppink",
        linestyle="-",
        label="I/O write",
        linewidth=1.0,
    )
    ax.plot(
        angles,
        list(map(lambda x: x * 100 / max(power), power)),
        color="orange",
        linestyle="-",
        label="Power",
        linewidth=1.0,
    )

    bin = 360 // 5

    ax.set_ylim(0, 100)
    ax.grid(True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax1 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax1.patch.set_visible(False)
    ax1.grid("off")
    ax1.xaxis.set_visible(False)
    ax1.set_rlabel_position(bin * 2)
    ax1.set_yticks([20, 40, 60, 80, 100])
    ax1.set_yticklabels(
        [
            str(round(max(pfs_recv) / 5, 2)) + "GB",
            str(round(max(pfs_recv) * 2 / 5, 2)) + "GB",
            str(round(max(pfs_recv) * 3 / 5, 2)) + "GB",
            str(round(max(pfs_recv) * 4 / 5, 2)) + "GB",
            str(round(max(pfs_recv), 2)) + "GB",
        ]
    )
    ax1.tick_params(axis="y", colors="g", labelsize=7)
    ax1.set_xticklabels([])

    ax2 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax2.patch.set_visible(False)
    ax2.grid("off")
    ax2.xaxis.set_visible(False)
    ax2.set_rlabel_position(bin * 3)
    ax2.set_yticks([20, 40, 60, 80, 100])
    ax2.set_yticklabels(
        [
            str(round(max(ram) / 5, 2)) + "GB",
            str(round(max(ram) * 2 / 5, 2)) + "GB",
            str(round(max(ram) * 3 / 5, 2)) + "GB",
            str(round(max(ram) * 4 / 5, 2)) + "GB",
            str(round(max(ram), 2)) + "GB",
        ]
    )
    ax2.tick_params(axis="y", colors="b", labelsize=7)
    ax2.set_xticklabels([])

    ax3 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax3.patch.set_visible(False)
    ax3.grid("off")
    ax3.xaxis.set_visible(False)
    ax3.set_rlabel_position(bin * 1)
    ax3.set_yticks([20, 40, 60, 80, 100])
    ax3.set_yticklabels(["20%", "40%", "60%", "80%", "100%"])
    ax3.tick_params(axis="y", colors="darkred", labelsize=7)
    ax3.set_xticklabels([])

    ax4 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax4.patch.set_visible(False)
    ax4.grid("off")
    ax4.xaxis.set_visible(False)
    ax4.set_rlabel_position(bin * 0)
    ax4.set_yticks([20, 40, 60, 80, 100])
    ax4.set_yticklabels(
        [
            str(round(max(pfs_send) / 5, 2)) + "GB",
            str(round(max(pfs_send) * 2 / 5, 2)) + "GB",
            str(round(max(pfs_send) * 3 / 5, 2)) + "GB",
            str(round(max(pfs_send) * 4 / 5, 2)) + "GB",
            str(round(max(pfs_send), 2)) + "GB",
        ]
    )
    ax4.tick_params(axis="y", colors="deeppink", labelsize=7)
    ax4.set_xticklabels([])

    ax5 = fig.add_axes(rect=[0.1, 0.1, 0.8, 0.8], projection="polar")
    ax5.patch.set_visible(False)
    ax5.grid("off")
    ax5.xaxis.set_visible(False)
    ax5.set_rlabel_position(bin * 4)
    ax5.set_yticks([20, 40, 60, 80, 100])
    ax5.set_yticklabels(
        [
            str(round(max(power) / 5, 2)) + "W",
            str(round(max(power) * 2 / 5, 2)) + "W",
            str(round(max(power) * 3 / 5, 2)) + "W",
            str(round(max(power) * 4 / 5, 2)) + "W",
            str(round(max(power), 2)) + "W",
        ]
    )
    ax5.tick_params(axis="y", colors="orange", labelsize=7)
    ax5.set_xticklabels([])

    matplotlib.rcParams["agg.path.chunksize"] = 180000
    matplotlib.rcParams["path.simplify_threshold"] = 1
    ax.legend(bbox_to_anchor=(1.1, 1.1))
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
    hpc_resource_radar(cpu, ram, pfs_recv, pfs_send, power, "example.png")
