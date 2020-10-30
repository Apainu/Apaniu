{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-1-5841830b69c3>:45: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the \"use_line_collection\" keyword argument to True.\n",
      "  plt.stem(n, step(n))\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-1-5841830b69c3>:56: UserWarning: In Matplotlib 3.3 individual lines on a stem plot will be added as a LineCollection instead of individual lines. This significantly improves the performance of a stem plot. To remove this warning and switch to the new behaviour, set the \"use_line_collection\" keyword argument to True.\n",
      "  plt.stem(n, impulse(n))\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "from PyQt5.QtCore import Qt\n",
    "from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget, QApplication, QLabel\n",
    "\n",
    "\n",
    "class WindowClass(QWidget):\n",
    "    def __init__(self, parent=None):\n",
    "        super(WindowClass, self).__init__(parent)\n",
    "        self.lb = QLabel(\"离散信号图示\")\n",
    "        self.btn_1 = QPushButton(\"阶跃信号\")\n",
    "        self.btn_2 = QPushButton(\"冲激信号\")\n",
    "        self.lb.setAlignment(Qt.AlignHCenter)\n",
    "        self.btn_1.clicked.connect(self.btn1_click)\n",
    "        self.btn_2.clicked.connect(self.btn2_click)\n",
    "        self.resize(200, 150)\n",
    "        layout = QVBoxLayout()\n",
    "        layout.addWidget(self.lb)\n",
    "        layout.addWidget(self.btn_1)\n",
    "        layout.addWidget(self.btn_2)\n",
    "        self.setLayout(layout)\n",
    "\n",
    "   \n",
    "    def btn1_click(self):\n",
    "        def step(t):\n",
    "            y = np.where(t >= 0.0, 1.0, 0.0)\n",
    "            return y\n",
    "\n",
    "        n = np.arange(-4, 8)\n",
    "        plt.ylim(0, 2)\n",
    "        plt.stem(n, step(n))\n",
    "        plt.show()\n",
    "\n",
    "   \n",
    "    def btn2_click(self):\n",
    "        def impulse(t):\n",
    "            y = np.where(t == 0.0, 1.0, 0.0)\n",
    "            return y\n",
    "\n",
    "        n = np.arange(-4, 8)\n",
    "        plt.ylim(0, 2)\n",
    "        plt.stem(n, impulse(n))\n",
    "        plt.show()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app = QApplication(sys.argv)\n",
    "    win = WindowClass()\n",
    "    win.show()\n",
    "    sys.exit(app.exec_())\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
