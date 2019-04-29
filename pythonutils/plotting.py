import os
import random
import string

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import pythonutils.path


def smart_save_fig(fig: matplotlib.figure.Figure,
                   ident: str) -> str:
    # format = 'pgf'
    # format = 'png'
    format = 'jpg'

    paths = pythonutils.path.get_paths()
    work_dir = paths['work']

    filename = "{}.{}".format(ident, format)
    filepath = work_dir

    os.makedirs(filepath, exist_ok=True)
    fullfilename = os.path.join(filepath, filename)
    fig.savefig(fullfilename)
    fig_path = fullfilename
    return fig_path


def plot_random_data() -> matplotlib.figure.Figure:
    x = np.random.rand(100)
    y = np.random.rand(100)
    tit = ''.join(random.choices(string.ascii_uppercase, k=10))

    scale = .2
    fig = plt.figure(figsize=(12 * scale, 4 * scale))
    plt.plot(x, y)
    plt.title(tit)
    return fig


def subplot_random_data() -> matplotlib.figure.Figure:
    x = np.random.rand(100)
    y = np.random.rand(100)

    scale = .2
    fig, axs = plt.subplots(1, 3, figsize=(12 * scale, 4 * scale))

    suptitle = "suptitle"
    st = fig.suptitle(suptitle)
    ax0 = axs[0]
    ax0.plot(x, y)
    ax0.set_title("title")
    ax0.axis('off')

    ax1 = axs[1]
    ax1.plot(x, y)
    ax1.set_title("title")
    ax1.axis('off')

    ax2 = axs[2]
    ax2.plot(x, y)
    ax2.set_title('difference')

    st.set_y(0.95)
    fig.subplots_adjust(top=0.70, left=.05, right=.95, wspace=.01)
    return fig


if __name__ == "__main__":
    fig = plot_random_data()
    ident = 'ident'
    fig_path = smart_save_fig(fig, ident)
    plt.close(fig)



