"# Import all libraries needed for the tutorial\n",
    "\n",
    "# General syntax to import specific functions in a library: \n",
    "##from (library) import (specific library function)\n",
    "from pandas import DataFrame, read_csv\n",
    "\n",
    "# General syntax to import a library but no functions: \n",
    "##import (library) as (give the library a nickname/alias)\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd #this is how I usually import pandas\n",
    "import sys #only needed to determine Python version number\n",
    "import matplotlib #only needed to determine Matplotlib version number\n",
    "\n",
    "# Enable inline plotting\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python version 3.5.1 |Anaconda custom (64-bit)| (default, Feb 16 2016, 09:49:46) [MSC v.1900 64 bit (AMD64)]\n",
      "Pandas version 0.18.1\n",
      "Matplotlib version 1.5.1\n"
     ]
    }
   ],
   "source": [
    "print('Python version ' + sys.version)\n",
    "print('Pandas version ' + pd.__version__)\n",
    "print('Matplotlib version ' + matplotlib.__version__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Create Data  \n",
    "\n",
