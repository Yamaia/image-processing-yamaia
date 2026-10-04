# 🖼️ image-processing-yamaia

Pacote Python de processamento de imagens, instalável via `pip`, criado no Desafio de Projeto da DIO. O objetivo é dominar o ciclo completo de um pacote Open Source: modularização, metadados, build do Wheel e publicação no PyPI com Twine.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![scikit-image](https://img.shields.io/badge/scikit--image-0.19%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 📦 Funcionalidades

### `image_processing_yamaia.processing`
| Função | Descrição |
|---|---|
| `find_difference(img1, img2)` | Calcula a diferença estrutural (SSIM) entre duas imagens |
| `transfer_histogram(img1, img2)` | Transfere o histograma de `img2` para `img1` |
| `resize_image(img, proportion)` | Redimensiona a imagem por uma proporção entre 0 e 1 |

### `image_processing_yamaia.utils`
`read_image`, `save_image`, `plot_image`, `plot_result` e `plot_histogram`.

## 🚀 Instalação

```bash
pip install image-processing-yamaia
```

Ou a partir do código-fonte:

```bash
git clone https://github.com/SEU-USUARIO/image-processing-yamaia.git
cd image-processing-yamaia
pip install -e .
```

## 💡 Exemplo de uso

```python
from image_processing_yamaia.utils import read_image, plot_result
from image_processing_yamaia.processing import resize_image, transfer_histogram, find_difference

img1 = read_image("foto1.jpg")
img2 = read_image("foto2.jpg")

menor = resize_image(img1, 0.5)
ajustada = transfer_histogram(img1, img2)

plot_result(img1, ajustada, titles=["Original", "Histograma transferido"])
```

## 🗂️ Estrutura do projeto

```
image-processing-yamaia/
├── image_processing_yamaia/
│   ├── __init__.py
│   ├── processing.py
│   └── utils.py
├── tests/
│   └── test_processing.py
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## 🧪 Testes

```bash
pip install pytest
pytest
```

## 🛠️ Empacotamento e publicação

```bash
python -m pip install --upgrade setuptools wheel twine build
python setup.py sdist bdist_wheel
twine check dist/*
twine upload --repository testpypi dist/*   # teste primeiro
twine upload dist/*                          # PyPI oficial
```

## ⚠️ Limitações e notas de versão

Bibliotecas de imagem evoluem com frequência. Este pacote usa `scikit-image` com o parâmetro `channel_axis` (versões 0.19 ou mais novas). Em versões antigas, o equivalente era `multichannel=True`. Documentar isso faz parte de lidar com código legado.

## 👨‍💻 Autor

**Yamaia**, desenvolvedor Python com foco em backend, cloud (Azure) e arquitetura de soluções.

## 📄 Licença

Distribuído sob a licença MIT.
