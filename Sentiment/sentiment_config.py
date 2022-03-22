#sentiment_reddit_template.py
# use this template to generate the reddit sentiment config file which is used in the sentiment process
crypto = { 'BTC','ETH','USDT','BNB','USDC','XRP','LUNA','ADA','SOL','AVAX','DOT','BUSD','DOGE','UST','SHIB','WBTC','CRO','MATIC','DAI','LTC','STETH','ATOM','NEAR','LINK','BCH','TRX','FTT','ETC','LEO','ALGO','OKB','XLM','UNI','HBAR','AXS','EGLD','ICP','MANA','SAND','VET','XMR','FIL','FTM','WAVES','CETH','THETA','KLAY','XTZ','OSMO','FRAX','MIM','RUNE','GRT','CUSDC','HNT','EOS','FLOW','MIOTA','ZEC','AAVE','CDAI','CAKE','TFUEL','MKR','GALA','BSV','QNT','BTT','ONE','HBTC','NEO','OMI','AR','XEC','APE','JUNO','XRD','HT','KSM','KCS','STX','ENJ','CEL','TUSD','DASH','HEART','AMP','CELO','BAT','NEXO','CVX','SNX','CHZ','KDA','FXS','BIT','LRC','USDP','GT','XEM','MINA','CRV','ROSE','IOTX','XIDO','HOT','DCR','QTUM','SCRT','LN','COMP','BTG','USDN','YFI','KUB','CUSDT','ANC','LPT','NXM','OMG','SUSHI','SLP','POKT','RNDR','1INCH','ZIL','BNT','RENBTC','ANKR','AUDIO','XDC','GNO','KAVA','RVN','PAXG','MSOL','FEI','SFM','IOST','ICX','EXRD','GLMR','WAXP','WOO','ZEN','IMX','OKT','RLY','RPL','SAPP','VLX','UMA','SGB','SC','GLM','ZRX','METIS','XAUT','LOOKS','ONT','LUSD','GMT','DOME','BABYDOGE','SKL','DYDX','NFT','TEL','LDO','XDB','OHM','CVXCRV','CHSB','SYN','ENS','TWT','SPELL','ELON','GUSD','DAG','JEWEL','JST','ARRR','SYS','ILV','POLY','REN','NU','KEEP','CKB','FLUX','HIVE','KNC','PEOPLE','SRM','DESO','CTC','OGN','DGB','TOMB','LSK','UOS','FLEX','CSPR','XPRT','HUSD','TRAC','RON','XNO','TOKE','PLA','FLOKI','SXP','10SET','C98','STSOL','RACA','MBOX','WIN','ASTRO','SAFEMOON','MIMATIC','WRX','DENT','PERP','EVER','INJ','VVS','UBT','OCEAN','FET','EWT','RAY','ZNN','TRIBE','ZMT','PLEX','FX','API3','XSUSHI','MXC','CELR','XYO','MIR','HERO','SNT','MOVR','YGG','CHR','PYR','CET','CRTS','XCH','COTI','ELG','MED','EURT','DPX','POWR','ORBS','LYXE','ASTR','GMX','MDX','MASK','PUNDIX','STARS','BOBA','KNCL','RAD','CVC','TLOS','ARDR','MX','UFO','CFX','ALUSD','JASMY','DAO','IBBTC','SUPER','NPXS','ERG','YOSHI','PRCH','CTSI','JOE','BSW','RSR','MLK','ANT','BICO','MPL','MULTI','MMF','NMR','DIVI','RGT','XCM','REQ','REEF','ACH','SBTC','WMT','XSGD','ICHI','BFC','XVG','STORJ','ELF','MC','BAND','VERI','TON','MNGO','AURORA','ASD','AKT','ACA','PLT','BTSE','SURE','BETA','FEG','DG','MAGIC','VTHO','TSHARE','ARK','KOGE','USDX','QRDO','KP3R','OXT','DUSK','SPA','OUSD','STARL','FEG','BEZOGE','BDX','PROM','ION','RLC','MAID','NKN','STMX','SUN','RDPX','KISHU','RUNE','HTR','RMRK','EURS','STRAX','STEEM','HXRO','TLM','VR','FLEXUSD','META','STPT','DAWN','TRU','DODO','AGLD','BAL','IBEUR','GPX','AETHC','RIF','TITAN','DEP','SAVAX','ALPHA','SETH2','POLS','STRK','DERO','GHST','ALCX','GXC','BOO','KIRO','LAT','BTCST','KAI','AUCTION','BAKE','ORN','EPS','SOUL','XPR','SFUND','ALICE','HOO','XVS','FUN','TIME','UTK','HYDRA','C20','MSHARE','BIFI','ETN','SWP','QKC','AIOZ','SETH','TOMO','WILD','KLV','ADS','CUNI','XDG','CQT','REGEN','MINE','TORN','MTL','HEZ','AGEUR','CRA','RAIL','QI','GTC','ALPINE','SUSD','WCFG','BCD','REP','IDEX','RARE','ROOK','CBAT','FIDA','WAN','ZPAY','VRA','CDT','DVI','IQ','ATA','BOSON','XAVA','CLV','ALBT','BTRFLY','SFP','PRO','CTK','AMPL','HUNT','BZRX','CUBE','AGIX','YFII','AERGO','NSBT','MLN','ATOLO','GFARM2','KILT','DPI','CUSD','WNXM','BZZ','MAPS','LEND','BADGER','HNS','QI','ETH2X-FLI','QUICK','RBN','MFT','IRIS','NRV','OXY','AURY','FOX','AVA','EROWAN','GF','VRSC','MUSD','PRE','COVAL','ERN','PLTC','CRE','RFOX','LINA','RAI','NTVRK','SAI','TT','ARPA','PEAK','ALPACA', }

# Exclude common words used on crypto reddit that are also crypto names
blacklist = {'I', 'WSB', 'THE', 'A', 'ROPE', 'YOLO', 'TOS', 'CEO', 'DD', 'IT', 'OPEN', 'ATH', 'PM', 'IRS', 'FOR','DEC', 'BE', 'IMO', 'ALL', 'RH', 'EV', 'TOS', 'CFO', 'CTO', 'DD', 'BTFD', 'WSB', 'OK', 'PDT', 'RH', 'KYS', 'FD', 'TYS', 'US', 'USA', 'IT', 'ATH', 'RIP', 'BMW', 'GDP', 'OTM', 'ATM', 'ITM', 'IMO', 'LOL', 'AM', 'BE', 'PR', 'PRAY', 'PT', 'FBI', 'SEC', 'GOD', 'NOT', 'POS', 'FOMO', 'TL;DR', 'EDIT', 'STILL', 'WTF', 'RAW', 'PM', 'LMAO', 'LMFAO', 'ROFL', 'EZ', 'RED', 'BEZOS', 'TICK', 'IS', 'PM', 'LPT', 'GOAT', 'FL', 'CA', 'IL', 'MACD', 'HQ', 'OP', 'PS', 'AH', 'TL', 'JAN', 'FEB', 'JUL', 'AUG', 'SEP', 'SEPT', 'OCT', 'NOV', 'FDA', 'IV', 'ER', 'IPO', 'MILF', 'BUT', 'SSN', 'FIFA', 'USD', 'CPU', 'AT', 'GG', 'Mar'}


# adding crypto reddit to vader to improve sentiment analysis, score: 4.0 to -4.0. Rank each keyword
# add new key words below that you would like to rank

new_words = {
    'lambo': 4.0,
    'rekt': -4.0,
    'citron': -4.0,
    'hidenburg': -4.0,
    'moon': 4.0,
    'Elon': 2.0,
    'hodl': 2.0,
    'highs': 2.0,
    'mooning': 4.0,
    'long': 2.0,
    'short': -2.0,
    'call': 4.0,
    'calls': 4.0,
    'put': -4.0,
    'puts': -4.0,
    'break': 2.0,
    'tendie': 2.0,
    'tendies': 2.0,
    'town': 2.0,
    'overvalued': -3.0,
    'undervalued': 3.0,
    'buy': 4.0,
    'sell': -4.0,
    'gone': -1.0,
    'gtfo': -1.7,
    'fomo': 2.0,
    'paper': -1.7,
    'bullish': 3.7,
    'bearish': -3.7,
    'bagholder': -1.7,
    'stonk': 1.9,
    'green': 1.9,
    'money': 1.2,
    'print': 2.2,
    'rocket': 2.2,
    'bull': 2.9,
    'bear': -2.9,
    'pumping': 1.0,
    'sus': -3.0,
    'offering': -2.3,
    'rip': -4.0,
    'downgrade': -3.0,
    'upgrade': 3.0,
    'maintain': 1.0,
    'pump': 1.9,
    'hot': 2,
    'drop': -2.5,
    'rebound': 1.5,
    'crack': 2.5, }