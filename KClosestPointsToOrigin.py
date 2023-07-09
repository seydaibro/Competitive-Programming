distances = []
        for point in points:
            distance = [point, point[0]**2 + point[1]**2]
            distances.append(distance)
        distances.sort(key=lambda x: x[1])
        
        closest_points = []
        for point in distances[:k]:
            closest_points.append(point[0])
        return closest_points
