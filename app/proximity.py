import math
from app.models import PointOfInterest


def euclidean_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def filter_by_proximity(
    pois: list[PointOfInterest], ref_x: int, ref_y: int, max_distance: float
) -> list[PointOfInterest]:
    return [
        poi for poi in pois
        if euclidean_distance(poi.x, poi.y, ref_x, ref_y) <= max_distance
    ]
