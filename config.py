import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL='00ef677f65e0431599c6a04edc5ba054'
    # CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='00ef677f65e0431599c6a04edc5ba054'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}