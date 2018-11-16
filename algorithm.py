import math
import sys

class Algorithm:
    def __init__(self, points, starting_point_number):
        self.available_points = points
        self.already_passed_points = []
        self.route_length = 0
        self.current_point = 0
        self.assign_starting_point(starting_point_number-1)

    def are_points_available(self):
        return len(self.available_points) > 0

    def assign_starting_point(self, starting_point_number):
        try:
            self.current_point = self.available_points.pop(starting_point_number)
            self.starting_point = self.current_point
            self.already_passed_points.append(self.current_point.id)
        except:
            print("Czy aby na pewno podałeś poprawny numer startowy?")
    
    def calculate_shortest_path(self):
        while self.are_points_available():
            shortest_distance = sys.maxsize
            nearest_point_idx = -1

            for index in range(len(self.available_points)):
                point = self.available_points[index]
                distance = self.get_distance(point)

                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_point_idx = index
                
            
            self.current_point = self.available_points.pop(nearest_point_idx)
            self.already_passed_points.append(self.current_point.id)
            self.route_length += shortest_distance
            
        
        self.go_to_starting_point()
        self.print_results()
            
    def go_to_starting_point(self):
        distance = self.get_distance(self.starting_point)
        self.already_passed_points.append(self.starting_point.id)
        self.route_length += distance

    def get_distance(self, point):
        return math.sqrt(
            (point.x - self.current_point.x)**2 + (point.y - self.current_point.y)**2
        )

    def get_route(self):
        return ''.join(str(self.already_passed_points))

    def print_results(self):
        print("---------------------------------------------------")
        print("No to policzone...")
        print("---------------------------------------------------")

        print("Długość drogi: {0}".format(self.route_length))
        print("Przebieg trasy: {0}".format(self.get_route()))