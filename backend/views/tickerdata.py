import re
from stringprep import map_table_b2
from flask import Response
import requests
from flask_restful import Resource
import json

class TickerData():
    tickerMap = {'MMM': '3M', 'AOS': 'A. O. Smith', 'ABT': 'Abbott', 'ABBV': 'AbbVie', 'ABMD': 'Abiomed', 'ACN': 'Accenture', 'ATVI': 'Activision Blizzard', 'ADM': 'ADM', 'ADBE': 'Adobe', 'ADP': 'ADP', 'AAP': 'Advance Auto Parts', 'AES': 'AES', 'AFL': 'Aflac', 'A': 'Agilent Technologies', 'AIG': 'AIG', 'APD': 'Air Products', 'AKAM': 'Akamai', 'ALK': 'Alaska Air Group', 'ALB': 'Albemarle', 'ARE': 'Alexandria', 'ALGN': 'Align', 'ALLE': 'Allegion', 'LNT': 'Alliant Energy', 'ALL': 'Allstate', 'GOOGL': 'Alphabet (Class A)', 'GOOG': 'Alphabet (Class C)', 'MO': 'Altria', 'AMZN': 'Amazon', 'AMCR': 'Amcor', 'AMD': 'AMD', 'AEE': 'Ameren', 'AAL': 'American Airlines Group', 'AEP': 'American Electric Power', 'AXP': 'American Express', 'AMT': 'American Tower', 'AWK': 'American Water', 'AMP': 'Ameriprise Financial', 'ABC': 'AmerisourceBergen', 'AME': 'Ametek', 'AMGN': 'Amgen', 'APH': 'Amphenol', 'ADI': 'Analog Devices', 'ANSS': 'Ansys', 'ANTM': 'Anthem', 'AON': 'Aon', 'APA': 'APA Corporation', 'AAPL': 'Apple', 'AMAT': 'Applied Materials', 'APTV': 'Aptiv', 'ANET': 'Arista', 'AIZ': 'Assurant', 'T': 'AT&T', 'ATO': 'Atmos Energy', 'ADSK': 'Autodesk', 'AZO': 'AutoZone', 'AVB': 'AvalonBay Communities', 'AVY': 'Avery Dennison', 'BKR': 'Baker Hughes', 'BALL': 'Ball', 'BAC': 'Bank of America', 'BBWI': 'Bath & Body Works', 'BAX': 'Baxter', 'BDX': 'Becton Dickinson', 'WRB': 'Berkley', 'BRK.B': 'Berkshire Hathaway', 'BBY': 'Best Buy', 'BIO': 'Bio-Rad', 'TECH': 'Bio-Techne', 'BIIB': 'Biogen', 'BLK': 'BlackRock', 'BK': 'BNY Mellon', 'BA': 'Boeing', 'BKNG': 'Booking Holdings', 'BWA': 'BorgWarner', 'BXP': 'Boston Properties', 'BSX': 'Boston Scientific', 'BMY': 'Bristol Myers Squibb', 'AVGO': 'Broadcom', 'BR': 'Broadridge', 'BRO': 'Brown & Brown', 'BF.B': 'Brown–Forman', 'CHRW': 'C.H. Robinson', 'CDNS': 'Cadence', 'CZR': 'Caesars Entertainment', 'CPT': 'Camden', 'CPB': "Campbell's", 'COF': 'Capital One', 'CAH': 'Cardinal Health', 'KMX': 'CarMax', 'CCL': 'Carnival', 'CARR': 'Carrier', 'CTLT': 'Catalent', 'CAT': 'Caterpillar', 'CBOE': 'Cboe', 'CBRE': 'CBRE', 'CDW': 'CDW', 'CE': 'Celanese', 'CNC': 'Centene', 'CNP': 'CenterPoint Energy', 'CDAY': 'Ceridian', 'CERN': 'Cerner', 'CF': 'CF Industries', 'CRL': 'Charles River', 'SCHW': 'Charles Schwab', 'CHTR': 'Charter Communications', 'CVX': 'Chevron', 'CMG': 'Chipotle Mexican Grill', 'CB': 'Chubb', 'CHD': 'Church & Dwight', 'CI': 'Cigna', 'CINF': 'Cincinnati Financial', 'CTAS': 'Cintas', 'CSCO': 'Cisco', 'C': 'Citigroup', 'CFG': 'Citizens', 'CTXS': 'Citrix', 'CLX': 'Clorox', 'CME': 'CME Group', 'CMS': 'CMS Energy', 'KO': 'Coca-Cola', 'CTSH': 'Cognizant', 'CL': 'Colgate-Palmolive', 'CMCSA': 'Comcast', 'CMA': 'Comerica', 'CAG': 'Conagra Brands', 'COP': 'ConocoPhillips', 'ED': 'Con Edison', 'STZ': 'Constellation Brands', 'CEG': 'Constellation Energy', 'COO': 'CooperCompanies', 'CPRT': 'Copart', 'GLW': 'Corning', 'CTVA': 'Corteva', 'COST': 'Costco', 'CTRA': 'Coterra', 'CCI': 'Crown Castle', 'CSX': 'CSX', 'CMI': 'Cummins', 'CVS': 'CVS Health', 'DHI': 'D.R. Horton', 'DHR': 'Danaher', 'DRI': 'Darden', 'DVA': 'DaVita', 'DE': 'Deere & Co.', 'DAL': 'Delta Air Lines', 'XRAY': 'Dentsply Sirona', 'DVN': 'Devon', 'DXCM': 'DexCom', 'FANG': 'Diamondback', 'DLR': 'Digital Realty', 'DFS': 'Discover', 'DISH': 'Dish', 'DIS': 'Disney', 'DG': 'Dollar General', 'DLTR': 'Dollar Tree', 'D': 'Dominion Energy', 'DPZ': "Domino's", 'DOV': 'Dover', 'DOW': 'Dow', 'DTE': 'DTE', 'DUK': 'Duke Energy', 'DRE': 'Duke Realty', 'DD': 'DuPont', 'DXC': 'DXC Technology', 'EMN': 'Eastman', 'ETN': 'Eaton', 'EBAY': 'eBay', 'ECL': 'Ecolab', 'EIX': 'Edison International', 'EW': 'Edwards Lifesciences', 'EA': 'Electronic Arts', 'EMR': 'Emerson', 'ENPH': 'Enphase', 'ETR': 'Entergy', 'EOG': 'EOG Resources', 'EPAM': 'EPAM', 'EFX': 'Equifax', 'EQIX': 'Equinix', 'EQR': 'Equity Residential', 'ESS': 'Essex', 'EL': 'Estée Lauder Companies', 'ETSY': 'Etsy', 'RE': 'Everest', 'EVRG': 'Evergy', 'ES': 'Eversource', 'EXC': 'Exelon', 'EXPE': 'Expedia Group', 'EXPD': 'Expeditors', 'EXR': 'Extra Space Storage', 'XOM': 'ExxonMobil', 'FFIV': 'F5', 'FDS': 'FactSet', 'FAST': 'Fastenal', 'FRT': 'Federal Realty', 'FDX': 'FedEx', 'FITB': 'Fifth Third Bank', 'FRC': 'First Republic', 'FE': 'FirstEnergy', 'FIS': 'FIS', 'FISV': 'Fiserv', 'FLT': 'Fleetcor', 'FMC': 'FMC', 'F': 'Ford', 'FTNT': 'Fortinet', 'FTV': 'Fortive', 'FBHS': 'Fortune Brands', 'FOXA': 'Fox Corporation (Class A)', 'FOX': 'Fox Corporation (Class B)', 'BEN': 'Franklin Templeton', 'FCX': 'Freeport-McMoRan', 'AJG': 'Gallagher', 'GRMN': 'Garmin', 'IT': 'Gartner', 'GE': 'GE', 'GNRC': 'Generac', 'GD': 'General Dynamics', 'GIS': 'General Mills', 'GPC': 'Genuine Parts', 'GILD': 'Gilead', 'GL': 'Globe Life', 'GPN': 'Global Payments', 'GM': 'GM', 'GS': 'Goldman Sachs', 'GWW': 'Grainger', 'HAL': 'Halliburton', 'HIG': 'Hartford (The)', 'HAS': 'Hasbro', 'HCA': 'HCA Healthcare', 'PEAK': 'Healthpeak', 'HSIC': 'Henry Schein', 'HSY': "Hershey's", 'HES': 'Hess', 'HPE': 'Hewlett Packard Enterprise', 'HLT': 'Hilton', 'HOLX': 'Hologic', 'HD': 'Home Depot', 'HON': 'Honeywell', 'HRL': 'Hormel', 'HST': 'Host Hotels & Resorts', 'HWM': 'Howmet Aerospace', 'HPQ': 'HP', 'HUM': 'Humana', 'HII': 'Huntington Ingalls Industries', 'HBAN': 'Huntington National Bank', 'IEX': 'IDEX', 'IDXX': 'Idexx Laboratories', 'ITW': 'Illinois Tool Works', 'ILMN': 'Illumina', 'INCY': 'Incyte', 'IR': 'Ingersoll Rand', 'INTC': 'Intel', 'ICE': 'Intercontinental Exchange', 'IBM': 'IBM', 'IP': 'International Paper', 'IPG': 'Interpublic Group', 'IFF': 'International Flavors & Fragrances', 'INTU': 'Intuit', 'ISRG': 'Intuitive Surgical', 'IVZ': 'Invesco', 'IPGP': 'IPG Photonics', 'IQV': 'IQVIA', 'IRM': 'Iron Mountain', 'JBHT': 'J.B. Hunt', 'JKHY': 'Jack Henry & Associates', 'J': 'Jacobs', 'JNJ': 'Johnson & Johnson', 'JCI': 'Johnson Controls', 'JPM': 'JPMorgan Chase', 'JNPR': 'Juniper Networks', 'K': "Kellogg's", 'KEY': 'KeyCorp', 'KEYS': 'Keysight', 'KMB': 'Kimberly-Clark', 'KIM': 'Kimco Realty', 'KMI': 'Kinder Morgan', 'KLAC': 'KLA', 'KHC': 'Kraft Heinz', 'KR': 'Kroger', 'LHX': 'L3Harris', 'LH': 'LabCorp', 'LRCX': 'Lam Research', 'LW': 'Lamb Weston', 'LVS': 'Las Vegas Sands', 'LDOS': 'Leidos', 'LEN': 'Lennar', 'LLY': 'Lilly', 'LNC': 'Lincoln Financial', 'LIN': 'Linde', 'LYV': 'Live Nation Entertainment', 'LKQ': 'LKQ Corporation', 'LMT': 'Lockheed Martin', 'L': 'Loews Corporation', 'LOW': "Lowe's", 'LUMN': 'Lumen', 'LYB': 'LyondellBasell', 'MTB': 'M&T Bank', 'MRO': 'Marathon Oil', 'MPC': 'Marathon Petroleum', 'MKTX': 'MarketAxess', 'MAR': 'Marriott International', 'MMC': 'Marsh & McLennan', 'MLM': 'Martin Marietta', 'MAS': 'Masco', 'MA': 'Mastercard', 'MTCH': 'Match Group', 'MKC': 'McCormick', 'MCD': "McDonald's", 'MCK': 'McKesson', 'MDT': 'Medtronic', 'MRK': 'Merck', 'FB': 'Meta', 'MET': 'MetLife', 'MTD': 'Mettler Toledo', 'MGM': 'MGM Resorts', 'MCHP': 'Microchip', 'MU': 'Micron', 'MSFT': 'Microsoft', 'MAA': 'Mid-America Apartments', 'MRNA': 'Moderna', 'MHK': 'Mohawk Industries', 'MOH': 'Molina Healthcare', 'TAP': 'Molson Coors', 'MDLZ': 'Mondelez International', 'MPWR': 'Monolithic Power Systems', 'MNST': 'Monster Beverage', 'MCO': "Moody's", 'MS': 'Morgan Stanley', 'MOS': 'Mosaic', 'MSI': 'Motorola Solutions', 'MSCI': 'MSCI', 'NDAQ': 'Nasdaq', 'NTAP': 'NetApp', 'NFLX': 'Netflix', 'NWL': 'Newell Brands', 'NEM': 'Newmont', 'NWSA': 'News Corp (Class A)', 'NWS': 'News Corp (Class B)', 'NEE': 'NextEra Energy', 'NLSN': 'Nielsen', 'NKE': 'Nike', 'NI': 'NiSource', 'NDSN': 'Nordson', 'NSC': 'Norfolk Southern', 'NTRS': 'Northern Trust', 'NOC': 'Northrop Grumman', 'NLOK': 'NortonLifeLock', 'NCLH': 'Norwegian Cruise Line Holdings', 'NRG': 'NRG Energy', 'NUE': 'Nucor', 'NVDA': 'Nvidia', 'NVR': 'NVR', 'NXPI': 'NXP', 'ORLY': "O'Reilly Automotive", 'OXY': 'Occidental Petroleum', 'ODFL': 'Old Dominion', 'OMC': 'Omnicom Group', 'OKE': 'Oneok', 'ORCL': 'Oracle', 'OGN': 'Organon', 'OTIS': 'Otis', 'PCAR': 'Paccar', 'PKG': 'Packaging Corporation of America', 'PARA': 'Paramount', 'PH': 'Parker', 'PAYX': 'Paychex', 'PAYC': 'Paycom', 'PYPL': 'PayPal', 'PENN': 'Penn National Gaming', 'PNR': 'Pentair', 'PEP': 'PepsiCo', 'PKI': 'PerkinElmer', 'PFE': 'Pfizer', 'PM': 'Philip Morris International', 'PSX': 'Phillips 66', 'PNW': 'Pinnacle West', 'PXD': 'Pioneer Natural Resources', 'PNC': 'PNC Financial Services', 'POOL': 'Pool Corporation', 'PPG': 'PPG Industries', 'PPL': 'PPL', 'PFG': 'Principal', 'PG': 'Procter & Gamble', 'PGR': 'Progressive', 'PLD': 'Prologis', 'PRU': 'Prudential', 'PEG': 'PSEG', 'PTC': 'PTC', 'PSA': 'Public Storage', 'PHM': 'PulteGroup', 'PVH': 'PVH', 'QRVO': 'Qorvo', 'PWR': 'Quanta', 'QCOM': 'Qualcomm', 'DGX': 'Quest Diagnostics', 'RL': 'Ralph Lauren', 'RJF': 'Raymond James', 'RTX': 'Raytheon Technologies', 'O': 'Realty Income', 'REG': 'Regency Centers', 'REGN': 'Regeneron', 'RF': 'Regions', 'RSG': 'Republic Services', 'RMD': 'ResMed', 'RHI': 'Robert Half', 'ROK': 'Rockwell Automation', 'ROL': 'Rollins', 'ROP': 'Roper', 'ROST': 'Ross', 'RCL': 'Royal Caribbean Group', 'SPGI': 'S&P Global', 'CRM': 'Salesforce', 'SBAC': 'SBA Communications', 'SLB': 'Schlumberger', 'STX': 'Seagate', 'SEE': 'Sealed Air', 'SRE': 'Sempra Energy', 'NOW': 'ServiceNow', 'SHW': 'Sherwin-Williams', 'SBNY': 'Signature Bank', 'SPG': 'Simon', 'SWKS': 'Skyworks', 'SJM': 'Smucker', 'SNA': 'Snap-on', 'SEDG': 'SolarEdge', 'SO': 'Southern Company', 'LUV': 'Southwest Airlines', 'SWK': 'Stanley Black & Decker', 'SBUX': 'Starbucks', 'STT': 'State Street', 'STE': 'Steris', 'SYK': 'Stryker', 'SIVB': 'SVB Financial', 'SYF': 'Synchrony', 'SNPS': 'Synopsys', 'SYY': 'Sysco', 'TMUS': 'T-Mobile', 'TROW': 'T. Rowe Price', 'TTWO': 'Take-Two Interactive', 'TPR': 'Tapestry', 'TGT': 'Target', 'TEL': 'TE Connectivity', 'TDY': 'Teledyne', 'TFX': 'Teleflex', 'TER': 'Teradyne', 'TSLA': 'Tesla', 'TXN': 'Texas Instruments', 'TXT': 'Textron', 'TMO': 'Thermo Fisher Scientific', 'TJX': 'TJX Companies', 'TSCO': 'Tractor Supply', 'TT': 'Trane Technologies', 'TDG': 'TransDigm', 'TRV': 'Travelers', 'TRMB': 'Trimble', 'TFC': 'Truist', 'TWTR': 'Twitter', 'TYL': 'Tyler Technologies', 'TSN': 'Tyson', 'USB': 'U.S. Bank', 'UDR': 'UDR', 'ULTA': 'Ulta Beauty', 'UAA': 'Under Armour (Class A)', 'UA': 'Under Armour (Class C)', 'UNP': 'Union Pacific', 'UAL': 'United Airlines', 'UNH': 'UnitedHealth Group', 'UPS': 'United Parcel Service', 'URI': 'United Rentals', 'UHS': 'Universal Health Services', 'VLO': 'Valero', 'VTR': 'Ventas', 'VRSN': 'Verisign', 'VRSK': 'Verisk', 'VZ': 'Verizon', 'VRTX': 'Vertex', 'VFC': 'VF Corporation', 'VTRS': 'Viatris', 'V': 'Visa', 'VNO': 'Vornado Realty Trust', 'VMC': 'Vulcan Materials', 'WAB': 'Wabtec', 'WMT': 'Walmart', 'WBA': 'Walgreens Boots Alliance', 'WBD': 'Warner Bros. Discovery', 'WM': 'Waste Management', 'WAT': 'Waters', 'WEC': 'WEC Energy Group', 'WFC': 'Wells Fargo', 'WELL': 'Welltower', 'WST': 'West Pharmaceutical Services', 'WDC': 'Western Digital', 'WRK': 'WestRock', 'WY': 'Weyerhaeuser', 'WHR': 'Whirlpool', 'WMB': 'Williams', 'WTW': 'Willis Towers Watson', 'WYNN': 'Wynn Resorts', 'XEL': 'Xcel Energy', 'XYL': 'Xylem', 'YUM': 'Yum! Brands', 'ZBRA': 'Zebra', 'ZBH': 'Zimmer Biomet', 'ZION': 'Zions Bancorp', 'ZTS': 'Zoetis'}
    
    tickerLogo = {
        "AMCR":"https://api.polygon.io/v1/reference/company-branding/d3d3LmFtY29yLmNvbQ/images/2022-05-01_logo.png?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",
        "URI":"https://api.polygon.io/v1/reference/company-branding/d3d3LnVuaXRlZHJlbnRhbHMuY29t/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",
        "NSC":"https://api.polygon.io/v1/reference/company-branding/d3d3Lm5vcmZvbGtzb3V0aGVybi5jb20/images/2022-01-10_icon.jpeg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",

        "JNJ":"https://api.polygon.io/v1/reference/company-branding/d3d3Lmpuai5jb20/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",
        "SNA":"https://api.polygon.io/v1/reference/company-branding/d3d3LnNuYXBvbi5jb20/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",
        "GLW":"https://api.polygon.io/v1/reference/company-branding/d3d3LmNvcm5pbmcuY29t/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",


        "LHX":"https://api.polygon.io/v1/reference/company-branding/d3d3LmwzaGFycmlzLmNvbQ/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",
        "RL":"https://api.polygon.io/v1/reference/company-branding/d3d3LnJhbHBobGF1cmVuLmNvbQ/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on",
        "WY":"https://api.polygon.io/v1/reference/company-branding/d3d3LndleWVyaGFldXNlci5jb20/images/2022-01-10_logo.svg?apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on"
    }
    def __init__(self):
        pass

    def parseData(self, data):
        myData = []
        for eachResult in data["results"]:
            if(eachResult["T"] in self.tickerMap):
                eachResult["name"] = self.tickerMap[eachResult["T"]]
                myData.append(eachResult)
        myData = myData[:8]
        result = []
        for eachData in myData:
            id = eachData["T"]
            eachData["image_url"] = self.tickerLogo[id]
            result.append(eachData)
        return json.dumps(myData)

    def convert2JSON(self, data):
        myDump = json.dumps(data)
        return myDump


class TickerDataListEndpoint(Resource):
    def __init__(self):
        pass
    
    def get(self):
        res = requests.get("https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2022-05-27?adjusted=false&apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on")
        tickerHelper = TickerData()
        result = tickerHelper.parseData(res.json())
        return Response(result, mimetype="application/json", status=200)

    def post(self):
        # create a new "bookmark" based on the data posted in the body 
        return Response(json.dumps({"message": "Post id invalid. It must be of type: int"}), mimetype="application/json",status=400)

class TickerDataDetailEndpoint(Resource):

    def __init__(self):
        pass

    def get(self, id):
        url = f"https://api.polygon.io/v1/open-close/{id}/2022-05-27?adjusted=true&apiKey=V2qYytgYXBSkWEqSld0oy545Ywuea6on"
        res = requests.get(url)
        # g = trial.TickerData()
        # result = g.parseData(res.json())
        print(res.json())
        # return Response(result, mimetype="application/json", status=200)

        return Response(json.dumps({"message":  "Post id={0} successfully deleted".format(id)}), mimetype="application/json", status=200)


def initialize_routes(api, firebase):
    api.add_resource(
        TickerDataListEndpoint, 
        '/tickerdata'
    )

    api.add_resource(
        TickerDataDetailEndpoint, 
        '/tickerdata/<string:id>' 
    )
