"""Funções de processamento de imagens."""
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity
from skimage.transform import resize


def find_difference(image1, image2):
    """Retorna a imagem de diferença (SSIM) entre duas imagens de mesmo tamanho."""
    if image1.shape != image2.shape:
        raise ValueError("As imagens devem ter as mesmas dimensões.")
    gray1 = rgb2gray(image1) if image1.ndim == 3 else image1
    gray2 = rgb2gray(image2) if image2.ndim == 3 else image2
    score, difference = structural_similarity(gray1, gray2, full=True, data_range=1.0)
    print(f"Similaridade (SSIM) entre as imagens: {score:.4f}")
    return np.clip(difference, 0, 1)


def transfer_histogram(image1, image2):
    """Ajusta o histograma de image1 para casar com o de image2."""
    channel_axis = -1 if image1.ndim == 3 else None
    return match_histograms(image1, image2, channel_axis=channel_axis)


def resize_image(image, proportion):
    """Redimensiona a imagem por uma proporção (0 < proportion <= 1)."""
    if not 0 < proportion <= 1:
        raise ValueError("proportion deve estar entre 0 (exclusivo) e 1.")
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    return resize(image, (height, width), anti_aliasing=True)
