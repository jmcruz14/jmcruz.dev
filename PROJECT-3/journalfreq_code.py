#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Import journal data into dataframe
journalentry = pd.read_csv('/Users/jccruz/Desktop/Checklists and Spreadsheets/journalentry.csv')
journalentry = journalentry.loc[:, :'STU']

# Cleaning up the journal data of any incomplete entries
journalentry.dropna(how='any',
                    subset=['Time', 'STU'],
                    inplace = True)
journalentry['STU'] = journalentry['STU'].astype(int)
journalentry.sort_values(by = 'STU', inplace=True)
journalentry['STU'] = journalentry['STU'].astype(str)
journalentry['STU'] = journalentry['STU'].apply(lambda x : x 
                                                if (len(x)==4) 
                                                else ('0'*(4-len(x)))+x)

# Creating 'Hour' and 'Minute' columns according to the STU of each entry
journalentry['Hour'] = journalentry['STU'].apply(lambda x : x[0:2])
journalentry['Minute'] = journalentry['STU'].apply(lambda x : x[2:])
journalentry['Minute'] = journalentry['Minute'].astype(int)

# Generating new dataframe from journal data sorted according to hours
je_binned = pd.DataFrame(journalentry.groupby(['Hour']).count())

# Minute and Hour data only from journalentry dataframe
je_minhr = journalentry[['Minute', 'Hour']]

# Building the seaborn visual data
sns.set_style('dark')
sns.set_theme(rc={'axes.facecolor': (0,0,0,0)}) #transparency axis background

palette = sns.cubehelix_palette(24, start=0.15, rot=0.65, light=0.7)
g = sns.FacetGrid(je_minhr, palette=palette, row='Hour',
                  hue='Hour', aspect = 13, height=2.4) 

g.map_dataframe(sns.histplot, x='Minute', fill=True, alpha=1)

def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .3, label, color='black', fontsize=60,
            ha="left", va="center", transform=ax.transAxes)

# Generating graph data and adjusting additional parameters
g.map(label, "Hour")

g.fig.subplots_adjust(hspace=-.69) #Height Space between the plots

g.set_titles('')
g.set(yticks=[], xlabel='Minutes', ylabel='') #y-ticks not needed
g.despine(left=True)

plt.suptitle('What Time Do I Usually Write?', fontsize=115, fontweight='extra bold')
plt.xlabel('Minutes', loc='center', fontsize=100)
plt.xticks(fontsize=75)