# luce-exr

An OpenEXR reader and writer for Luce/Base: scanline and tiled images, none/RLE/ZIP/PIZ/PXR24 compression, half and float channels, and [Cryptomatte 1.2](docs/CRYPTOMATTE.md) layers.

## Modules

- `exr` (exported): `probe`, `decode_chunk` and `encode` over luce-raster's `Raster`.
- `cryptomatte` (exported): `Cryptomatte.open(path, layer)`, `extract`/`extract_ids`
  into a `Matte`, `pick`/`pick_name`, manifests embedded or in sidecars,
  `layer_count`/`layer_name`, and `CryptomatteBuilder` (weighted samples, `save`).
  It moved here from luce-image (2026-09-27): Cryptomatte only exists in EXR.
- `manifest`: the bounded JSON object parser for manifests; `crypto_hash`:
  MurmurHash3_x86_32, seed zero, over UTF-8 bytes.

Split out of luce-image on 2026-09-22 so every file format is its own package, like luce-svg and luce-psd. luce-image depends on it for `Image.open`/`save`; it depends on luce-raster, luce-compress.

```sh
python3 tools/bootstrap.py                      # the pinned compilers, into build/toolchain
python3 -m venv build/test-env
build/test-env/bin/python -m pip install -r tests/requirements.txt
./test.sh    # module tests native and C, the Cryptomatte Luce API, Psyop fixtures against OpenEXR
```

The Cryptomatte fixtures keep their BSD-3-Clause notice
([LICENSES/Cryptomatte.txt](LICENSES/Cryptomatte.txt)); see [THIRD_PARTY.md](THIRD_PARTY.md).
