"""Build the paper with its external simulation figures using local TeX."""
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
BUILD = HERE/'build'
BUILD.mkdir(exist_ok=True)
SOURCE = HERE/'reciprocal_simplex.tex'
engine = shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'
for iteration in range(2):
    result = subprocess.run([engine, '-interaction=nonstopmode', '-halt-on-error',
        '-file-line-error', '-output-directory='+str(BUILD), str(SOURCE)],
        cwd=HERE, capture_output=True, text=True)
    (BUILD/f'pass_{iteration+1}.txt').write_text(result.stdout+result.stderr)
    if result.returncode:
        print((result.stdout+result.stderr)[-9000:])
        sys.exit(result.returncode)
shutil.copyfile(BUILD/'reciprocal_simplex.pdf', HERE/'reciprocal_simplex.pdf')
log = (BUILD/'reciprocal_simplex.log').read_text(errors='replace')
warnings = [x for x in log.splitlines() if any(y in x for y in
    ('Overfull', 'Undefined', 'undefined', 'multiply defined', 'Warning'))]
print('\n'.join(warnings) if warnings else 'Two-pass LaTeX build passed without warnings.')
print(HERE/'reciprocal_simplex.pdf')
