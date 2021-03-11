{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import some libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "sns.set_theme(style = \"darkgrid\",\n",
    "              font_scale = 1.25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "    # Method Chain 1\n",
    "    # Load Data\n",
    "    # remove Player ID column\n",
    "    # remove LS (long snappers) are typicaly never drafted as the team\n",
    "    # there are 20 Long Snappers\n",
    "    # remove 2018 data from dataset\n",
    "    # there is no draft information\n",
    "    # set all undrafted players pick 300\n",
    "    # set all undrafted players round 10\n",
    "    \n",
    "    df1 = (\n",
    "        pd.read_csv(url_or_path_to_csv_file)\n",
    "        .drop(columns=['Pfr_ID'])\n",
    "        .query('Pos != \"LS\"')\n",
    "        .query('Year != 2018')\n",
    "        .assign(Pick=lambda x: x.Pick.fillna(300))\n",
    "        .assign(Round=lambda x: x.Round.fillna(10))\n",
    "    )\n",
    "    \n",
    "    # Method Chain 2\n",
    "    # Replace position names\n",
    "    # MLB (middle line backer) and ILB (inside line backer) are the same thing\n",
    "    # LB (line backer) with ILB\n",
    "    # EDGE is the same as DE (Defense End)\n",
    "    # combine P (punter) and K (kicker) into a single position PK (Punter Kicker)\n",
    "    # G (guard) with OG (offensive guard)\n",
    "    # OL (offensive line) with OG (offensive guard)\n",
    "    # FS(free safety) with S (satefy)\n",
    "    # SS(strong safety) with S (satefy)\n",
    "    # DB (defensive back) with CB (corner back)\n",
    "    # NT (nose tackle with DT (defensive tackle)\n",
    "    \n",
    "    df1['Pos'] = (df1['Pos']\n",
    "        .replace({'MLB': 'ILB'})\n",
    "        .replace('LB', 'ILB')\n",
    "        .replace('EDGE', 'DE')\n",
    "        .replace('P', 'PK')\n",
    "        .replace('K', 'PK')\n",
    "        .replace('G', 'OG')\n",
    "        .replace('OL', 'OG')\n",
    "        .replace('FS', 'S')\n",
    "        .replace('SS', 'S')\n",
    "        .replace('DB', 'CB')\n",
    "        .replace('NT', 'DT')\n",
    "    )\n",
    "        \n",
    "    return df1"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
