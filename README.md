# chia-plot-deduplicator

A script that scans directories for duplicated and non "full size" (108gb ish) Chia Blockchain plots.

## How to run
1. ```git clone https://github.com/pogacic/chia-plot-deduplicator```

2. ```cd chia-plot-deduplicator```

3. ```pip3 install -r requirements.txt```

4. Modify ```config.yml``` with absolute paths of your Chia Plot directories.

5. ```python3 plot_deduplicator.py```
