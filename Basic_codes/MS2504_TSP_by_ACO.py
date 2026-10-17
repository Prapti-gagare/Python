import math
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

DATA_FILE = Path(__file__).with_name('india_cities.txt')
ANTS = 30
ITERATIONS = 100
ALPHA = 1.0
BETA = 4.0
EVAPORATION = 0.5
Q = 100.0
SEED = 42


def read_cities(filename):
    """Read lines: CityName latitude longitude (commas also accepted)."""
    names, coordinates = [], []
    with open(filename, encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split(',')] if ',' in line else line.split()
            if len(parts) != 3:
                raise ValueError(f'Invalid line {line_number}: {line}')
            name, lat, lon = parts
            names.append(name)
            coordinates.append((float(lat), float(lon)))
    if len(names) < 2 or len(set(names)) != len(names):
        raise ValueError('Provide at least two cities with unique names.')
    return names, np.array(coordinates, dtype=float)


def haversine(lat1, lon1, lat2, lon2):
    radius = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))
    a = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    return 2 * radius * math.asin(math.sqrt(min(1.0, a)))


def distance_matrix(coordinates):
    n = len(coordinates)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            distances[i, j] = distances[j, i] = haversine(*coordinates[i], *coordinates[j])
    return distances


def route_length(route, distances):
    return sum(distances[route[i], route[(i + 1) % len(route)]] for i in range(len(route)))


def make_route(pheromone, heuristic, rng):
    n = len(pheromone)
    start = rng.randrange(n)
    route = [start]
    unvisited = set(range(n)) - {start}
    while unvisited:
        current = route[-1]
        choices = sorted(unvisited)
        weights = np.array([(pheromone[current, j] ** ALPHA) * (heuristic[current, j] ** BETA) for j in choices])
        probabilities = weights / weights.sum() if weights.sum() > 0 else np.full(len(choices), 1 / len(choices))
        next_city = rng.choices(choices, weights=probabilities, k=1)[0]
        route.append(next_city)
        unvisited.remove(next_city)
    return route


def draw_route(route, names, coordinates, length, title, filename):
    plt.figure(figsize=(11, 7))
    closed_route = route + [route[0]]
    xs = coordinates[closed_route, 1]  # longitude
    ys = coordinates[closed_route, 0]  # latitude
    plt.plot(xs, ys, 'b-o', linewidth=1.8, markersize=6)
    for step, city_index in enumerate(route):
        lon, lat = coordinates[city_index, 1], coordinates[city_index, 0]
        plt.annotate(f'{step + 1}. {names[city_index]}', (lon, lat), xytext=(5, 7), textcoords='offset points', fontsize=9)
    plt.scatter([xs[0]], [ys[0]], color='red', s=110, zorder=5, label='Start / End')
    plt.title(f'{title}\nTotal distance: {length:.2f} km')
    plt.xlabel('Longitude (degrees)')
    plt.ylabel('Latitude (degrees)')
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=160)
    plt.show()
    plt.close()


def solve_tsp(names, coordinates):
    rng = random.Random(SEED)
    distances = distance_matrix(coordinates)
    n = len(names)
    pheromone = np.ones((n, n), dtype=float)
    heuristic = np.zeros((n, n), dtype=float)
    nonzero = distances > 0
    heuristic[nonzero] = 1 / distances[nonzero]
    # Identical coordinates still represent different cities: give them a tiny distance.
    for i in range(n):
        for j in range(n):
            if i != j and distances[i, j] == 0:
                distances[i, j] = 1e-6
                heuristic[i, j] = 1e6

    best_route = None
    best_distance = float('inf')
    history = []
    stages = sorted({1, max(1, ITERATIONS // 4), max(1, ITERATIONS // 2), ITERATIONS})

    for iteration in range(1, ITERATIONS + 1):
        ant_routes = []
        for _ in range(ANTS):
            route = make_route(pheromone, heuristic, rng)
            length = route_length(route, distances)
            ant_routes.append((route, length))
            if length < best_distance:
                best_distance = length
                best_route = route.copy()

        pheromone *= (1 - EVAPORATION)
        for route, length in ant_routes:
            deposit = Q / max(length, 1e-9)
            for i in range(n):
                a, b = route[i], route[(i + 1) % n]
                pheromone[a, b] += deposit
                pheromone[b, a] += deposit

        history.append(best_distance)
        print(f'Iteration {iteration:3d}: Best distance = {best_distance:.2f} km')
        if iteration in stages:
            print('Route:', ' -> '.join(names[i] for i in best_route + [best_route[0]]))
            draw_route(best_route, names, coordinates, best_distance,
                       f'ACO route at iteration {iteration}', f'ACO_stage_{iteration}.png')

    print('\nFINAL BEST ROUTE:')
    print(' -> '.join(names[i] for i in best_route + [best_route[0]]))
    print(f'Minimum distance found: {best_distance:.2f} km')
    draw_route(best_route, names, coordinates, best_distance, 'Final best ACO route', 'ACO_final_route.png')

    plt.figure(figsize=(9, 5))
    plt.plot(range(1, ITERATIONS + 1), history)
    plt.xlabel('Iteration')
    plt.ylabel('Best distance so far (km)')
    plt.title('ACO convergence for Traveling Salesman Problem')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('ACO_convergence.png', dpi=160)
    plt.show()
    plt.close()


if __name__ == '__main__':
    city_names, city_coordinates = read_cities(DATA_FILE)
    solve_tsp(city_names, city_coordinates)