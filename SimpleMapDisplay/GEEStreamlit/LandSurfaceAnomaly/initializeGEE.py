import ee
import xee

ee.Initialize()
ee.Authenticate(
    project = 'ee-subsonic',
    opt_url = 'https://earthengine-highvolume.googleapis.com'
)