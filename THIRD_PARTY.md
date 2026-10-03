# Upstream attribution

`src/piz.lucb` and `pxr24.lucb` are Base ports of OpenEXR's
BSD-3-Clause algorithms, including its Huffman, wavelet and predictor layout.
Reference version: [OpenEXR v3.3.5](https://github.com/AcademySoftwareFoundation/openexr/tree/v3.3.5).
The upstream notice is retained in [LICENSES/OpenEXR.txt](LICENSES/OpenEXR.txt).
The PIZ encoder uses a simpler valid fixed-length Huffman table and repeat codes;
it is not an equivalent-performance copy of OpenEXR's optimized writer.

## Cryptomatte fixtures

Source: [Psyop/Cryptomatte](https://github.com/Psyop/Cryptomatte/tree/968d5e4b6171e29ba5f89d554117132a164e747e),
revision `968d5e4b6171e29ba5f89d554117132a164e747e`, `sample_images/debug_images/`.
Local copies are under `tests/fixtures/cryptomatte/`. The BSD-3-Clause fixture
license is retained in [LICENSES/Cryptomatte.txt](LICENSES/Cryptomatte.txt).

| Local file | SHA-256 |
| --- | --- |
| multichannel.exr | 41f3a864fe08cf2b981ee9ab267bd589abb9f1122a776557c6a7e493757b789e |
| special_chars.exr | a86dee943aa28dcc691b41c552b7ade871a6a40dc24098d02dacc23d49c1ed60 |
| sidecar_manifest.exr | b4ca37ae66763431b8a535b5b81552a9bcf2849f78537d445e6e2a5ab24d076e |
| sidecar_manifest.crypto_asset.json | 443727159ca176685e4fed1951576c08efaecafa9195075d81dce5b696806a13 |

Specification: [Cryptomatte 1.2.0](https://github.com/Psyop/Cryptomatte/blob/master/specification/cryptomatte_specification.pdf).
