# Upstream attribution

`src/luce_exr/piz.lucb` and `pxr24.lucb` are Base ports of OpenEXR's
BSD-3-Clause algorithms, including its Huffman, wavelet and predictor layout.
Reference version: [OpenEXR v3.3.5](https://github.com/AcademySoftwareFoundation/openexr/tree/v3.3.5).
The upstream notice is retained in [LICENSES/OpenEXR.txt](LICENSES/OpenEXR.txt).
The PIZ encoder uses a simpler valid fixed-length Huffman table and repeat codes;
it is not an equivalent-performance copy of OpenEXR's optimized writer.
