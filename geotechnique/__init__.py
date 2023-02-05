from os.path import isfile
from os.path import dirname
from fonctions import plot_foundation

version_file = '{}/version.txt'.format(dirname(__file__))

if isfile(version_file):
    with open(version_file) as version_file:
        __version__ = version_file.read().strip()
        
fichier = open("input.txt", "r")
all_lines = fichier.readlines()

h_couche = eval(all_lines[4].split('\t')[0])
color_couche = eval(all_lines[5].split('\t')[0])
symbol_couche = eval(all_lines[6].split('\t')[0])
name_couche = eval(all_lines[7].split('\t')[0])
name_fondation = eval(all_lines[8].split('\t')[0])
name_mur = eval(all_lines[9].split('\t')[0])
Titre = eval(all_lines[10].split('\t')[0])
h_mur = eval(all_lines[11].split('\t')[0])
d_mur = eval(all_lines[12].split('\t')[0])
deb_fond = eval(all_lines[13].split('\t')[0])
h_fond = eval(all_lines[14].split('\t')[0])
fond_fouille = eval(all_lines[15].split('\t')[0])
cote = eval(all_lines[16].split('\t')[0])
color_fond = eval(all_lines[17].split('\t')[0])
symbol_fond = eval(all_lines[18].split('\t')[0])
font = eval(all_lines[19].split('\t')[0])
font_title = eval(all_lines[20].split('\t')[0])
font_measure = eval(all_lines[21].split('\t')[0])

plot_foundation(Titre, cote, h_couche,color_couche, symbol_couche, name_couche, name_fondation, d_mur, h_mur, name_mur, deb_fond,h_fond,fond_fouille, color_fond,symbol_fond,font,font_title, font_measure)

