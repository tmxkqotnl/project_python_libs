import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import platform

# for encoding

# global setting

plt.rcParams['axes.unicode_minus'] = False
print([font.name for font in fm.fontManager.ttflist]) # list installed fonts

# set font family 
# need to install Malgun Gothic 
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin': 
    plt.rcParams['font.family'] = 'AppleGothic'
else: 
    plt.rcParams['font.family'] = 'Malgun Gothic' # maybe need to fix

