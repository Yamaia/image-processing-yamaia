"""Funções utilitárias de leitura, gravação e visualização de imagens."""
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread, imsave


def read_image(path, is_gray=False):
    """Lê uma imagem; se is_gray=True, converte para escala de cinza (float 0-1)."""
    return imread(path, as_gray=is_gray)


def save_image(image, path):
    """Salva uma imagem (array numpy) em disco."""
    if image.dtype != np.uint8:
        if image.max() <= 1:
            image = (np.clip(image, 0, 1) * 255).astype(np.uint8)
        else:
            image = np.clip(image, 0, 255).astype(np.uint8)
    imsave(path, image)


def plot_image(image, title="", cmap=None):
    """Exibe uma imagem."""
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap=cmap or ("gray" if image.ndim == 2 else None))
    plt.title(title)
    plt.axis("off")
    plt.show()


def plot_result(*args, titles=None):
    """Exibe várias imagens lado a lado."""
    n = len(args)
    titles = titles or [f"Imagem {i + 1}" for i in range(n)]
    plt.figure(figsize=(5 * n, 4))
    for i, (img, title) in enumerate(zip(args, titles), start=1):
        plt.subplot(1, n, i)
        plt.imshow(img, cmap="gray" if img.ndim == 2 else None)
        plt.title(title)
        plt.axis("off")
    plt.show()


def plot_histogram(image, title="Histograma"):
    """Exibe o histograma de cada canal da imagem."""
    plt.figure(figsize=(8, 4))
    if image.ndim == 2:
        plt.hist(image.ravel(), bins=256, color="gray", alpha=0.7)
    else:
        for i, color in enumerate(("red", "green", "blue")):
            plt.hist(image[..., i].ravel(), bins=256, color=color, alpha=0.5)
    plt.title(title)
    plt.show()
