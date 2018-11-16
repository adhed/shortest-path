from point import Point
from algorithm import Algorithm
        
def ask_for_points():
    points = []
    points_counter = int(input("Podaj proszę liczbę punktów jaką będziesz chciał przeliczyć: "))

    for idx in range(points_counter):
        x = int(input("Podaj współrzędną X dla punktu nr {0}: ".format(idx+1)))
        y = int(input("Podaj współrzędną Y dla punktu nr {0}: ".format(idx+1)))
        point = Point(idx+1, x, y)
        points.append(point)
    
    return points

def ask_for_starting_point():
    try:
        starting_point = int(input("Podaj numer punktu startowego: "))
    except:
        print("Czy aby na pewno podałeś numer?")

    return starting_point

def main():
    print("Witaj w algorytmie przeliczania najkrótszej ścieżki!")
    points = ask_for_points()
    starting_point_number = ask_for_starting_point()
    algorithm = Algorithm(points, starting_point_number)
    algorithm.calculate_shortest_path()

if __name__ == "__main__":
    main()