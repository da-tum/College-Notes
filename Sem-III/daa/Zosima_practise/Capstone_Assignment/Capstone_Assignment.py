'''
Capstone Assignment: Intelligent Courier Planning System

Build a prototype that, given a list of parcels and delivery 
points, generates an ordered delivery route and an optimized packing plan. 
The solution should integrate sorting, dynamic programming, graph algorithms, 
and approximation techniques to simulate an intelligent courier planning system.


Instructions:
Develop an integrated Python application that combines the 
algorithms implemented in previous lab assignments.

The system should prioritize parcels, optimize package selection, 
determine the shortest delivery routes, and compare the runtime 
performance of different algorithmic components.

Submit the complete project through file upload or an accessible GitHub 
repository with source code, documentation, sample datasets, screenshots, 
runtime charts, and execution steps.


Phase Breakdown:

| Phase | Meaningful Title | Task to be Completed | Evidence / Submission | Marks |
| :--- | :--- | :--- | :--- | :---: |
| Phase 1 | Courier Problem Design and Planning | Design the courier-planning problem, define parcel attributes, delivery points, graph format and required algorithms. Prepare a simple design showing how sorting, knapsack, shortest path and route planning will work together. | Problem clarity, algorithm selection, data design, route-planning logic and suitability of selected techniques. | 20 |
| Phase 2 | Package Prioritization and Box Filling | Sort parcels based on delivery deadlines or priority using the best sorting algorithm. Apply the Dynamic Programming to determine the optimal set of parcels for one delivery trip. | Correct parcel sorting, DP table or output evidence, selected parcel list and packing-plan result. | 20 |
| Phase 3 | Route Maker and Graph Processing | Build the customer graph, use Dijkstra’s Algorithm for individual shortest paths and apply nearest-neighbor TSP approximation for the overall delivery route. | Graph representation, shortest-path output, final route sequence and route-length calculation. | 20 |
| Phase 4 | Performance Testing and Optimization | Test the system using small and larger datasets. Record runtime of major steps and suggest improvements for future optimization. | Test cases, runtime chart, correctness evidence, optimization comments and comparison of major steps. | 20 |
| Phase 5 | Final Report and Demonstration | Present the working system with screenshots or output traces, explain the result and submit the final file or GitHub repository with proper documentation. | Result explanation, documentation quality, screenshot evidence, final demonstration and originality. | 20 |
| **Total** | | | | **100** |

'''

import heapq
import time
from dataclasses import dataclass
from typing import List, Dict, Tuple, Set


# ==================================================================================================
# Phase 1: Courier Problem Design and Data Models
# ==================================================================================================

@dataclass
class Parcel:
    """Represents a parcel to be delivered."""
    id: str
    destination: str
    weight: int       # in kg
    priority: int     # Higher integer = higher urgency/value
    deadline: int     # Hours from present (smaller = more urgent)

    def __repr__(self):
        return f"Parcel({self.id}, Dest:{self.destination}, Wt:{self.weight}kg, Pri:{self.priority}, Deadline:{self.deadline}h)"


class DeliveryGraph:
    """Adjacency list representation of customer and hub locations graph."""
    def __init__(self):
        self.adj_list: Dict[str, List[Tuple[str, float]]] = {}

    def add_location(self, loc: str):
        if loc not in self.adj_list:
            self.adj_list[loc] = []

    def add_road(self, u: str, v: str, distance: float, bidirectional: bool = True):
        self.add_location(u)
        self.add_location(v)
        self.adj_list[u].append((v, distance))
        if bidirectional:
            self.adj_list[v].append((u, distance))

    def get_locations(self) -> List[str]:
        return list(self.adj_list.keys())


# ==================================================================================================
# Phase 2: Package Prioritization and Box Filling (Sorting & 0/1 Knapsack DP)
# ==================================================================================================

def sort_parcels(parcels: List[Parcel], key: str = "priority") -> List[Parcel]:
    """
    Sorts parcels based on priority (descending) or deadline (ascending).
    Uses Merge Sort logic (Python's stable Timsort - O(N log N)).
    """
    if key == "priority":
        # Highest priority first, breaking ties with earlier deadline
        return sorted(parcels, key=lambda p: (-p.priority, p.deadline))
    elif key == "deadline":
        # Earliest deadline first, breaking ties with higher priority
        return sorted(parcels, key=lambda p: (p.deadline, -p.priority))
    return list(parcels)


def knapsack_01_packing(parcels: List[Parcel], capacity: int) -> Tuple[List[Parcel], int, List[List[int]]]:
    """
    Applies 0/1 Knapsack Dynamic Programming to determine the optimal set of parcels
    for one delivery trip without exceeding vehicle capacity.
    
    Time Complexity: O(N * W) where N = len(parcels), W = capacity
    Space Complexity: O(N * W)
    """
    n = len(parcels)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        p = parcels[i - 1]
        for w in range(1, capacity + 1):
            if p.weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - p.weight] + p.priority)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected parcels
    selected: List[Parcel] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(parcels[i - 1])
            w -= parcels[i - 1].weight

    selected.reverse()
    max_priority_score = dp[n][capacity]
    return selected, max_priority_score, dp


# ==================================================================================================
# Phase 3: Route Maker and Graph Processing (Dijkstra + Nearest-Neighbor TSP)
# ==================================================================================================

def dijkstra_shortest_paths(graph: DeliveryGraph, start_node: str) -> Dict[str, float]:
    """
    Computes shortest path distances from start_node to all reachable nodes using Dijkstra's algorithm.
    Time Complexity: O((V + E) log V)
    """
    distances: Dict[str, float] = {node: float('inf') for node in graph.get_locations()}
    distances[start_node] = 0.0
    pq = [(0.0, start_node)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > distances[u]:
            continue

        for v, weight in graph.adj_list.get(u, []):
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))

    return distances


def compute_all_pairs_distances(graph: DeliveryGraph, locations: List[str]) -> Dict[Tuple[str, str], float]:
    """Computes shortest path distances between all pairs of required locations using Dijkstra."""
    dist_matrix: Dict[Tuple[str, str], float] = {}
    for src in locations:
        all_dists = dijkstra_shortest_paths(graph, src)
        for dest in locations:
            dist_matrix[(src, dest)] = all_dists[dest]
    return dist_matrix


def tsp_nearest_neighbor(start_node: str, delivery_nodes: List[str], dist_matrix: Dict[Tuple[str, str], float]) -> Tuple[List[str], float]:
    """
    Nearest-Neighbor TSP approximation algorithm to determine ordered delivery route sequence.
    Starts at Hub (start_node), visits all unique delivery destinations, and returns to Hub.
    
    Time Complexity: O(K^2) where K is number of delivery locations.
    """
    unvisited = set(delivery_nodes)
    if start_node in unvisited:
        unvisited.remove(start_node)

    route = [start_node]
    current = start_node
    total_dist = 0.0

    while unvisited:
        next_node = min(unvisited, key=lambda loc: dist_matrix[(current, loc)])
        total_dist += dist_matrix[(current, next_node)]
        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    # Return to Hub
    total_dist += dist_matrix[(current, start_node)]
    route.append(start_node)

    return route, total_dist


# ==================================================================================================
# Phase 4: Performance Testing and Optimization Metrics
# ==================================================================================================

def run_performance_benchmarks():
    """Benchmarking suite to measure execution time of major algorithmic modules."""
    print("\n" + "=" * 80)
    print("PHASE 4: PERFORMANCE TESTING AND ALGORITHM BENCHMARKING REPORT")
    print("=" * 80)

    sizes = [10, 50, 200, 500]
    print(f"{'Input Size (N)':<16}{'Sorting (ms)':<16}{'0/1 Knapsack (ms)':<20}{'Dijkstra (ms)':<18}{'TSP NN (ms)':<15}")
    print("-" * 80)

    for n in sizes:
        # Create test dataset
        sample_parcels = [
            Parcel(id=f"P{i}", destination=f"Node_{i % 10}", weight=(i % 15) + 1, priority=(i % 50) + 1, deadline=(i % 12) + 1)
            for i in range(n)
        ]
        test_graph = DeliveryGraph()
        for i in range(10):
            for j in range(i + 1, 10):
                test_graph.add_road(f"Node_{i}", f"Node_{j}", float((i + j) % 7 + 1))

        # Benchmark Sorting
        t0 = time.perf_counter()
        _ = sort_parcels(sample_parcels, key="priority")
        t_sort = (time.perf_counter() - t0) * 1000

        # Benchmark 0/1 Knapsack
        t0 = time.perf_counter()
        _ = knapsack_01_packing(sample_parcels, capacity=100)
        t_knapsack = (time.perf_counter() - t0) * 1000

        # Benchmark Dijkstra
        t0 = time.perf_counter()
        _ = dijkstra_shortest_paths(test_graph, "Node_0")
        t_dijkstra = (time.perf_counter() - t0) * 1000

        # Benchmark TSP
        nodes = [f"Node_{i}" for i in range(10)]
        dist_mat = compute_all_pairs_distances(test_graph, nodes)
        t0 = time.perf_counter()
        _ = tsp_nearest_neighbor("Node_0", nodes[1:], dist_mat)
        t_tsp = (time.perf_counter() - t0) * 1000

        print(f"{n:<16}{t_sort:<16.4f}{t_knapsack:<20.4f}{t_dijkstra:<18.4f}{t_tsp:<15.4f}")

    print("\n[Scalability Observations]:")
    print("1. Parcel Sorting: Timsort scales cleanly at O(N log N).")
    print("2. 0/1 Knapsack DP: Time complexity depends on capacity (O(N * W)). Efficient for practical vehicle limits.")
    print("3. Dijkstra Shortest Path: O((V + E) log V) via priority queue provides optimal single-source routing.")
    print("4. Nearest-Neighbor TSP: O(K^2) fast approximation suitable for real-time courier route generation.")


# ==================================================================================================
# Phase 5: Demonstration and Execution Pipeline
# ==================================================================================================

def main():
    print("==========================================================================================")
    print("INTELLIGENT COURIER PLANNING SYSTEM — CAPSTONE DEMONSTRATION")
    print("==========================================================================================")

    # 1. Initialize Delivery Network Graph
    graph = DeliveryGraph()
    hub = "Central_Hub"
    graph.add_road(hub, "Zone_A", 4.0)
    graph.add_road(hub, "Zone_B", 6.0)
    graph.add_road(hub, "Zone_C", 8.0)
    graph.add_road("Zone_A", "Zone_B", 3.0)
    graph.add_road("Zone_B", "Zone_C", 2.0)
    graph.add_road("Zone_A", "Zone_D", 5.0)
    graph.add_road("Zone_C", "Zone_D", 4.0)
    graph.add_road("Zone_B", "Zone_D", 7.0)

    # 2. Define Incoming Parcels Pool
    all_parcels = [
        Parcel("P1", "Zone_A", weight=8, priority=40, deadline=2),
        Parcel("P2", "Zone_B", weight=12, priority=60, deadline=5),
        Parcel("P3", "Zone_C", weight=15, priority=90, deadline=1),
        Parcel("P4", "Zone_D", weight=10, priority=50, deadline=3),
        Parcel("P5", "Zone_A", weight=6, priority=30, deadline=4),
        Parcel("P6", "Zone_C", weight=7, priority=45, deadline=2),
    ]

    print("\n--- PHASE 1: INITIAL SYSTEM DATA ---")
    print(f"Depot Location: {hub}")
    print(f"Total Available Parcels: {len(all_parcels)}")
    for p in all_parcels:
        print(f"  - {p}")

    # 3. Phase 2: Prioritization & 0/1 Knapsack Packing
    print("\n--- PHASE 2: PACKAGE PRIORITIZATION & OPTIMAL BOX PACKING ---")
    sorted_parcels = sort_parcels(all_parcels, key="priority")
    print("\n[Prioritized Parcels (Sorted by Priority & Urgency)]:")
    for p in sorted_parcels:
        print(f"  - {p}")

    vehicle_capacity = 30  # Max weight vehicle can carry
    selected_parcels, max_priority, _ = knapsack_01_packing(sorted_parcels, vehicle_capacity)

    total_packed_weight = sum(p.weight for p in selected_parcels)
    print(f"\n[Vehicle Capacity Constraint]: {vehicle_capacity} kg")
    print(f"[Optimal Packed Parcels ({len(selected_parcels)} selected)]:")
    for p in selected_parcels:
        print(f"  - {p}")
    print(f"Total Weight: {total_packed_weight} / {vehicle_capacity} kg | Total Priority Score: {max_priority}")

    # 4. Phase 3: Route Maker & Graph Processing
    print("\n--- PHASE 3: ROUTE MAKER & GRAPH PROCESSING ---")
    delivery_destinations = list(set(p.destination for p in selected_parcels))
    all_route_nodes = [hub] + delivery_destinations

    dist_matrix = compute_all_pairs_distances(graph, all_route_nodes)
    optimal_route, route_length = tsp_nearest_neighbor(hub, delivery_destinations, dist_matrix)

    print(f"Unique Delivery Destinations: {delivery_destinations}")
    print(f"Optimal Delivery Sequence: {' -> '.join(optimal_route)}")
    print(f"Total Calculated Route Distance: {route_length:.2f} units")

    # 5. Phase 4: Performance Benchmarking
    run_performance_benchmarks()

    print("\n==========================================================================================")
    print("CAPSTONE ASSIGNMENT EXECUTION COMPLETE")
    print("==========================================================================================")


if __name__ == "__main__":
    main()


