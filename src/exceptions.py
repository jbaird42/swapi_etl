class TopTenCharacterException(Exception):
    """Raised when the top ten character process fails"""
    pass


class FailedFetchingResource(Exception):
    """Raised when a get request fails to retrieve a resource"""
    pass


class FailedPOST(Exception):
    """Raised when a POST request fails"""
    pass


class FailedBuildingCSV(Exception):
    """Raised when a CSV fails to build"""
    pass
