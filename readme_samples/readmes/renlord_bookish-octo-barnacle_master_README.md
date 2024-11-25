Paper: https://arxiv.org/abs/1905.00553

```python
"""How the plots are generated:
import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import concurrent.futures as conc
mpl.rc('font', size=16)

WIDTH=14
HEIGHT=10

OUTPUT_DIR="/scratch/[REDACTED]/SNB2019-PLOTS/"

datafiles = os.listdir('/scratch/[REDACTED]/muppet-ops')

fig, axes = plt.subplots(1, 1, figsize=(WIDTH,HEIGHT))
axes.set_ylabel('Density')

def plot(filename):
    fig, axes = plt.subplots(1, 1, figsize=(WIDTH,HEIGHT))
    axes.set_ylabel('Density')

    try:  
        muppetRatios = np.fromfile('/scratch/[REDACTED]/muppet-ops/{}'.format(filename),
          dtype=float, sep='\n')
        loulaRatios = np.fromfile('/scratch/[REDACTED]/loula-ops-data/{}'.format(filename),
          dtype=float, sep='\n')

        axes.set_xscale('log')
        axes.set_xlabel('{} Time-to-Gas Ratio (ns/gas)'.format(filename))
        ax = axes.twinx()
        ax.set_ylabel('Observation Count')

        muppetlogbins = np.geomspace(1, muppetRatios.max())
        loulalogbins = np.geomspace(1, loulaRatios.max())

        ax.hist(muppetRatios, bins=muppetlogbins,\
          alpha=0.3,\
          label="Machine A")
        axes.hist(muppetRatios, bins=muppetlogbins,\
          histtype='step', density=True,
               cumulative=True)
        ax.hist(loulaRatios, bins=loulalogbins,\
          alpha=0.3,\
          label="Machine B")
        axes.hist(loulaRatios, bins=loulalogbins,\
          histtype='step', density=True, cumulative=True)
        axes.axvline(1000, ls='--', color='r', label="Baseline")
        fig.legend(["Baseline", 'Machine A', 'Machine B'], loc="lower center",
        ncol=3, borderaxespad=0)
        plt.savefig(OUTPUT_DIR + "{}".format(filename[:-4] + '.png'))
    except ValueError:
        return


with conc.ProcessPoolExecutor(max_workers=32) as e:
    e.map(plot, datafiles)
"""

PLOT_DIR='/scratch/[ANON]/SNB2019-PLOTS/'

from IPython.display import Image, display
import os


plots = os.listdir(PLOT_DIR)
for i in range(0, len(plots)):
    print(plots[i])
    display(Image(filename=(PLOT_DIR+plots[i])))
```

    DUP3.png



![png](output_0_1.png)


    ORIGIN.png



![png](output_0_3.png)


    MSTORE8.png



![png](output_0_5.png)


    GT.png



![png](output_0_7.png)


    MOD.png



![png](output_0_9.png)


    CALLVALUE.png



![png](output_0_11.png)


    PUSH3.png



![png](output_0_13.png)


    AND.png



![png](output_0_15.png)


    SWAP1.png



![png](output_0_17.png)


    SWAP14.png



![png](output_0_19.png)


    ISZERO.png



![png](output_0_21.png)


    GAS.png



![png](output_0_23.png)


    POP.png



![png](output_0_25.png)


    LOG2.png



![png](output_0_27.png)


    JUMPCI.png



![png](output_0_29.png)


    BLOCKHASH.png



![png](output_0_31.png)


    SSTORE.png



![png](output_0_33.png)


    DUP10.png



![png](output_0_35.png)


    BYTE.png



![png](output_0_37.png)


    PUSH2.png



![png](output_0_39.png)


    DUP9.png



![png](output_0_41.png)


    SWAP13.png



![png](output_0_43.png)


    PUSH5.png



![png](output_0_45.png)


    SWAP2.png



![png](output_0_47.png)


    SUICIDE.png



![png](output_0_49.png)


    EQ.png



![png](output_0_51.png)


    SWAP9.png



![png](output_0_53.png)


    SUB.png



![png](output_0_55.png)


    DUP15.png



![png](output_0_57.png)


    BALANCE.png



![png](output_0_59.png)


    SWAP8.png



![png](output_0_61.png)


    GASLIMIT.png



![png](output_0_63.png)


    PUSHC.png



![png](output_0_65.png)


    MLOAD.png



![png](output_0_67.png)


    JUMPDEST.png



![png](output_0_69.png)


    JUMPI.png



![png](output_0_71.png)


    PUSH1.png



![png](output_0_73.png)


    DUP13.png



![png](output_0_75.png)


    SWAP7.png



![png](output_0_77.png)


    EXTCODESIZE.png



![png](output_0_79.png)


    DUP7.png



![png](output_0_81.png)


    SWAP4.png



![png](output_0_83.png)


    CALLDATALOAD.png



![png](output_0_85.png)


    MUL.png



![png](output_0_87.png)


    DUP14.png



![png](output_0_89.png)


    DUP16.png



![png](output_0_91.png)


    CALLER.png



![png](output_0_93.png)


    SIGNEXTEND.png



![png](output_0_95.png)


    MSTORE.png



![png](output_0_97.png)


    DUP1.png



![png](output_0_99.png)


    SWAP5.png



![png](output_0_101.png)


    DIV.png



![png](output_0_103.png)


    SWAP11.png



![png](output_0_105.png)


    GASPRICE.png



![png](output_0_107.png)


    SWAP12.png



![png](output_0_109.png)


    OR.png



![png](output_0_111.png)


    XOR.png



![png](output_0_113.png)


    CODECOPY.png



![png](output_0_115.png)


    MULMOD.png



![png](output_0_117.png)


    NUMBER.png



![png](output_0_119.png)


    DUP4.png



![png](output_0_121.png)


    PC.png



![png](output_0_123.png)


    SWAP6.png



![png](output_0_125.png)


    ADDMOD.png



![png](output_0_127.png)


    DUP12.png



![png](output_0_129.png)


    LT.png



![png](output_0_131.png)


    JUMP.png



![png](output_0_133.png)


    EXTCODECOPY.png



![png](output_0_135.png)


    COINBASE.png



![png](output_0_137.png)


    DUP2.png



![png](output_0_139.png)


    LOG0.png



![png](output_0_141.png)


    SWAP3.png



![png](output_0_143.png)


    ADDRESS.png



![png](output_0_145.png)


    SWAP16.png



![png](output_0_147.png)


    RETURN.png



![png](output_0_149.png)


    TIMESTAMP.png



![png](output_0_151.png)


    LOG3.png



![png](output_0_153.png)


    SMOD.png



![png](output_0_155.png)


    DUP11.png



![png](output_0_157.png)


    PUSH4.png



![png](output_0_159.png)


    DUP5.png



![png](output_0_161.png)


    CALLDATACOPY.png



![png](output_0_163.png)


    ADD.png



![png](output_0_165.png)


    DUP6.png



![png](output_0_167.png)


    LOG1.png



![png](output_0_169.png)


    DIFFICULTY.png



![png](output_0_171.png)


    SHA3.png



![png](output_0_173.png)


    SWAP10.png



![png](output_0_175.png)


    SGT.png



![png](output_0_177.png)


    SLT.png



![png](output_0_179.png)


    SDIV.png



![png](output_0_181.png)


    LOG4.png



![png](output_0_183.png)


    JUMPC.png



![png](output_0_185.png)


    EXP.png



![png](output_0_187.png)


    NOT.png



![png](output_0_189.png)


    SWAP15.png



![png](output_0_191.png)


    DUP8.png



![png](output_0_193.png)


    CALLDATASIZE.png



![png](output_0_195.png)


    SLOAD.png



![png](output_0_197.png)


    CODESIZE.png



![png](output_0_199.png)


    MSIZE.png



![png](output_0_201.png)



```python
print("total number of plots: " + str(len(plots)))
```

    total number of plots: 101



```python
# Traces are available at:
```
