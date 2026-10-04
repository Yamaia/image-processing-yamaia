# image-processing-yamaia

Pacote Python de processamento de imagens, criado como Desafio de Projeto da DIO sobre **empacotamento e publicação no PyPI**.

## Funcionalidades

**`image_processing_yamaia.processing`**
- `find_difference(img1, img2)`: diferença estrutural (SSIM) entre duas imagens
- `transfer_histogram(img1, img2)`: transfere o histograma de `img2` para `img1`
- `resize_image(img, proportion)`: redimensiona por proporção

**`image_processing_yamaia.utils`**
- `read_image`, `save_image`, `plot_image`, `plot_result`, `plot_histogram`

## Instalação

```bash
pip install image-processing-yamaia
```

Ou, a partir do código-fonte:

```bash
git clone https://github.com/SEU-USUARIO/image-processing-yamaia.git
cd image-processing-yamaia
pip install -e .
```

## Uso

```python
from image_processing_yamaia.utils import read_image, plot_result
from image_processing_yamaia.processing import resize_image, transfer_histogram, find_difference

img1 = read_image("foto1.jpg")
img2 = read_image("foto2.jpg")

menor = resize_image(img1, 0.5)
ajustada = transfer_histogram(img1, img2)
plot_result(img1, ajustada, titles=["Original", "Histograma transferido"])
```

## Testes

```bash
pip install pytest
pytest
```

## Empacotamento e publicação (passo a passo)

```bash
python -m pip install --upgrade setuptools wheel twine build
python setup.py sdist bdist_wheel      # ou: python -m build
twine check dist/*
twine upload --repository testpypi dist/*   # teste primeiro
twine upload dist/*                          # PyPI oficial
```

> Antes de publicar: altere `author`, `author_email` e `url` no `setup.py`, e escolha um `name` que ainda não exista no PyPI.

## Limitações e notas de versão

Bibliotecas de imagem mudam com frequência. Este pacote usa `scikit-image` com o parâmetro `channel_axis` (versões >= 0.19). Em versões antigas, o equivalente era `multichannel=True`.

## Autor

Yamaia, desenvolvedor Python focado em backend e cloud.

## Licença

MIT
