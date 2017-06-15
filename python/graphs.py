import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data_per_country(country_code):
    country_data = data[data[:, 1] == country_code]
    years = country_data[:, 4]
    values = country_data[:, 5]
    return years, values


def plot(country):
    x, y = get_data_per_country(country)
    plt.plot(x, y, marker='o', label=country)


def plot_indicator(indicator_name, ylabel):
    plt.figure(figsize=(6 * 1.2, 4 * 1.2))
    plt.rcParams.update({'font.size': 12})
    for country in country_codes:
        try:
            plot(country)
        except AttributeError:
            continue
    plt.legend()
    plt.title(indicator_name, fontsize=18)
    plt.xlabel('Año')
    plt.ylabel(ylabel)
    plt.show()


# ------------------------
#          MAIN
# ------------------------
indicator_codes = [
    'SP.POP.TOTL',
    'SP.URB.GROW',
    'SP.DYN.LE00.FE.IN',
    'SP.DYN.LE00.MA.IN',
    'SP.DYN.TFRT.IN',
    'SH.MED.BEDS.ZS',
    'NY.GDP.MKTP.KD',
    'EC.TAX.TOTL.GD.ZS',
    'NE.EXP.GNFS.KD',
    'EG.ELC.ACCS.ZS',
    'EG.ELC.RNEW.ZS',
    'EN.ATM.CO2E.KD.GD'
]

indicator_ylabels = {
    'SP.URB.GROW'       : 'Urban population growth',
    'SP.POP.TOTL'       : 'Population total',
    'NE.EXP.GNFS.KD'    : 'Exports',
    'SP.DYN.LE00.FE.IN' : 'Life expectancy at birth, females',
    'SP.DYN.LE00.MA.IN' : 'Life expectancy at birth, males',
    'SH.MED.BEDS.ZS'    : 'Number of hospital beds per 1000 citizens',
    'EG.ELC.ACCS.ZS'    : 'Percentage of population with access to electricity',
    'EG.ELC.RNEW.ZS'    : 'Percentage of electricity poduce from renewable sources',
    'NY.GDP.MKTP.KD'    : 'Gross Domestic Product',
    'SP.DYN.TFRT.IN'    : 'Fertility rate',
    'EC.TAX.TOTL.GD.ZS' : 'Tax revenue',
    'EN.ATM.CO2E.KD.GD' : 'CO2 emissions'
}

indicator_units = {
    'SP.URB.GROW'       : '(%)',
    'SP.POP.TOTL'       : '(n)',
    'NE.EXP.GNFS.KD'    : '($USD 2005)',
    'SP.DYN.LE00.FE.IN' : '(years)',
    'SP.DYN.LE00.MA.IN' : '(years)',
    'SH.MED.BEDS.ZS'    : '(n)',
    'EG.ELC.ACCS.ZS'    : '(%)',
    'EG.ELC.RNEW.ZS'    : '(%)',
    'NY.GDP.MKTP.KD'    : '($USD 2005)',
    'SP.DYN.TFRT.IN'    : '(births / women)',
    'EC.TAX.TOTL.GD.ZS' : '($USD 2005)',
    'EN.ATM.CO2E.KD.GD' : '(kg per 2005 $USD of GDP)'
}

file_path = "../data/general_data.scsv"
raw_data = pd.read_csv(file_path, sep=';', error_bad_lines=False)
country_codes = ["PER", "CHL", "CHN", "USA", "PRT"]
print(raw_data.shape)
raw_data = np.array(raw_data)
for code in indicator_codes:
    data = raw_data[raw_data[:, 3] == code]
    plot_indicator(indicator_ylabels[code], indicator_units[code])
