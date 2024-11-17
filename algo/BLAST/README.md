# BLAST

To compile and run the program:

```bash
make blst_main
./blst_main <SEQ> <SCORE_MATRIX> <WORD_SIZE> <THRESHOLD> <THREADS>
```

To test the program:

```bash
make blst_test
./blst_test
```

> [!NOTE]
> The compilation uses `-fopenmp` to enable parallelization.
> This is not supported by all compilers, e.g. by Mac's GCC.
