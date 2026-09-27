#!/usr/bin/env python3
"""luce-exr's gate: every module's tests on the native and C backends, then the
Cryptomatte Luce API and Psyop's upstream fixtures, whose extracted masks are
compared with OpenEXR's own reading of the files."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def modules():
    """The modules holding tests."""
    return [p for p in sorted((ROOT / 'src/luce_exr').glob('*.lucb')) if ('\n' + p.read_text()).count('\ntest "')]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', type=Path, default=Path(os.environ.get('LUCE_BASE_COMPILER', ROOT / 'build/toolchain/luce-base')))
    parser.add_argument('--luce', type=Path, default=Path(os.environ.get('LUCE_COMPILER', ROOT / 'build/toolchain/luce')))
    args = parser.parse_args()
    for dependency in ['numpy', 'OpenEXR']:
        try:
            __import__(dependency)
        except ImportError:
            raise SystemExit(f'Missing {dependency}; install tests/requirements.txt in a virtual environment and run with that Python.')
    if not args.base.is_file() or not args.luce.is_file():
        raise SystemExit('Build isolated compilers with python3 tools/bootstrap.py, or supply --base and --luce.')
    env = dict(os.environ, LUCE_BASE=str(args.base.resolve()), LUCE_STD=str(ROOT.parent / 'luce-base/src/std'),
               LUCE_CACHE=str(ROOT / 'build/cache'))
    (ROOT / 'build').mkdir(exist_ok=True)

    def run(command, timeout=300):
        subprocess.run([str(x) for x in command], check=True, cwd=ROOT, env=env, timeout=timeout)
    for backend in ['--native', '--backend=c']:
        for module in modules():
            run([args.base.resolve(), 'test', module, backend])
    # The Luce consumers are rebuilt for each backend; no stale binary can pass.
    for flags in [['--native'], ['--backend=c']]:
        print('MODE ' + ' '.join(flags), flush=True)
        with tempfile.TemporaryDirectory(prefix='luce-exr-tests-') as tmp:
            for source, target in [('crypto_api', 'cryptomatte'), ('crypto_fixture', 'crypto_fixture')]:
                run([args.luce.resolve(), 'build', ROOT / f'tests/{source}.luc', *flags, '-o', ROOT / f'build/{target}'])
            run([ROOT / 'build/cryptomatte', tmp])
            run([sys.executable, ROOT / 'tests/check_cryptomatte.py'])
    print('PASS luce-exr', flush=True)


if __name__ == '__main__':
    main()
