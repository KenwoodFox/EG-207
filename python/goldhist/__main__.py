# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import logging
import coloredlogs

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Setup logging
    logger = logging.getLogger(__name__)
    coloredlogs.install(
        fmt='%(asctime)s,%(msecs)03d %(hostname)s %(levelname)s %(message)s',
        level=logging.DEBUG,
        logger=logger)

    logger.info("Program Started.")

    data=np.random.random((4,10))
    xaxes = ['x1','x2','x3','x4']
    yaxes = ['y1','y2','y3','y4']
    titles = ['t1','t2','t3','t4'] 

    f,a = plt.subplots(2,2)
    a = a.ravel()
    for idx,ax in enumerate(a):
        ax.hist(data[idx])
        ax.set_title(titles[idx])
        ax.set_xlabel(xaxes[idx])
        ax.set_ylabel(yaxes[idx])
    plt.tight_layout()

    plt.show()
