import random
import math
import itertools
import cvxpy as cp
import numpy as np

def generate_random_graph(n, edge_prob):
    adj_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < edge_prob:
                adj_matrix[i][j] = adj_matrix[j][i] = 1
    return adj_matrix

def gw_maxcut(adj_matrix, num_trials=1):
    n = adj_matrix.shape[0]

    # Solve the SDP relaxation
    X = cp.Variable((n, n), symmetric=True)
    constraints = [X >> 0, cp.diag(X) == 1]
    objective = cp.Maximize(cp.sum(cp.multiply(adj_matrix, (1 - X)) / 4))
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)

    if X.value is None:
        raise ValueError("SDP did not converge or failed.")

    sdp_value = problem.value  # This is the SDP relaxation value

    # Eigen-decomposition and vector rounding
    w, v = np.linalg.eigh(X.value)
    w = np.clip(w, 0, None)
    vectors = v @ np.diag(np.sqrt(w))

    best_cut = 0
    for _ in range(num_trials):
        r = np.random.randn(vectors.shape[1])
        r /= np.linalg.norm(r)
        signs = np.sign(vectors @ r)
        mask = np.outer(signs, signs) < 0
        cut_value = np.sum(adj_matrix * mask) // 2
        best_cut = max(best_cut, cut_value)

    return best_cut, sdp_value

def brute_force_optimal_cut(adj_matrix):
    n = adj_matrix.shape[0]
    max_cut = 0

    for partition in itertools.product([0, 1], repeat=n):
        set1 = {i for i in range(n) if partition[i] == 0}
        set2 = set(range(n)) - set1
        cut_value = sum(
            adj_matrix[i][j]
            for i in set1 for j in set2
        )
        max_cut = max(max_cut, cut_value)

    return max_cut

def compute_approximation_ratio(gw_cut, opt_val, sdp_val):
    gw_opt_ratio = gw_cut / opt_val if opt_val else float('inf')
    gw_sdp_ratio = gw_cut / sdp_val if sdp_val else float('inf')
    return gw_opt_ratio, gw_sdp_ratio

def run_computations(n, num_runs, edge_prob):
    for run in range(num_runs):
        print(f"Run {run + 1}:")
        graph = generate_random_graph(n, edge_prob)

        gw_value, sdp_value = gw_maxcut(graph)
        opt_value = brute_force_optimal_cut(graph)

        gw_opt_ratio, gw_sdp_ratio = compute_approximation_ratio(gw_value, opt_value, sdp_value)

        print("Adjacency Matrix:")
        print(graph)
        print(f"GW Cut Value: {gw_value}")
        print(f"Optimal Cut Value: {opt_value}")
        print(f"SDP Relaxation Value: {sdp_value:.4f}")
        print(f"Approximation Ratio (GW/OPT): {gw_opt_ratio:.4f}")
        print(f"Approximation Ratio (GW/SDP): {gw_sdp_ratio:.4f}")
        print('-' * 60)

# User inputs
n = int(input("Enter the number of vertices: "))
num_runs = int(input("Enter the number of times to run the computation: "))
edge_prob = float(input("Enter edge probability (between 0 and 1): "))

run_computations(n, num_runs, edge_prob)
