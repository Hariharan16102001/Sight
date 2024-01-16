import os
os.path.join('usr', 'bin', 'spam')

from pathlib import Path
print(Path('usr').joinpath('bin').joinpath('spam'))

from pathlib import Path
print(Path('usr') / 'bin' / 'spam')
