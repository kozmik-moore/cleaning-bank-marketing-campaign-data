from pathlib import Path
from os.path import join

# Directory paths
root_dir = Path('..')
data_dir = Path(join(root_dir, 'data'))
assets_dir = Path(join(root_dir, 'assets'))
code_dir = Path(join(root_dir, 'code'))
products_dir = Path(join(root_dir, 'products'))

# File paths
rawdata_file = join(data_dir, 'bank_marketing.csv')
campaign_file = join(data_dir, 'campaign.csv')
client_file = join(data_dir, 'client.csv')
economic_file = join(data_dir, 'economic.csv')