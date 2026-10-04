import numpy as np
import pytest
from image_processing_yamaia.processing import find_difference, resize_image, transfer_histogram


def test_resize_image():
    img = np.random.rand(100, 80, 3)
    assert resize_image(img, 0.5).shape == (50, 40, 3)


def test_resize_invalid():
    with pytest.raises(ValueError):
        resize_image(np.zeros((10, 10)), 2)


def test_find_difference_identical():
    img = np.random.rand(32, 32)
    diff = find_difference(img, img)
    assert np.allclose(diff, 1.0)


def test_transfer_histogram_shape():
    a, b = np.random.rand(20, 20, 3), np.random.rand(20, 20, 3)
    assert transfer_histogram(a, b).shape == a.shape
