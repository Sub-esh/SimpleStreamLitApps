import ee
import xarray
from config import CONFIG

# intialize and authenticate GEE
def intialize_gee():
    """Intialize GEE with account credentials"""
    try:
        ee.Authenticate()
        ee.Initialize(
            project = 'subsonic',
            opt_url = 'https://earthengine-highvolume.googleapis.com'
        )
    except Exception as e:
        raise Exception(f"Failed to intialize GEE: {str(e)}")

def get_nepal_districts():
    """Load district shapefile"""
    try:
        districts = ee.FeatureCollection(CONFIG('NEPAL_DISTRICT_ASSET'))
        return districts
    except Exception as e:
        raise Exception(f"Failed to load districts: {str(e)}")

def get_district_names():
    """Get all the district names from the feature collection"""
    districts = get_nepal_districts()
    district_names = districts.aggregate_array('DISTRICT').distinct().getInfo()
    return sorted(district_names)