########################To be implemented####################################
from Analyzer import Analyzer

analyzer = Analyzer()
analyzer.read_dataset('diamonds.csv')
#analyzer.describe()
analyzer.drop_missing_data()
analyzer.plot_histograms_numeric('carat')