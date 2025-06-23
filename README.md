# 🧠 Max-Cut Approximation via Semidefinite Programming (UGP Project)

This repository contains the implementation and analysis of the Goemans-Williamson approximation algorithm for the Max-Cut problem. The project was carried out as part of my Undergraduate Research Project (UGP) at IIT Kanpur, focusing on relaxation-based approximation methods and convex optimization.

---

## 📌 Project Overview

- **Objective**: Study approximation algorithms using relaxation techniques, with a focus on semidefinite programming (SDP) and its application to the Max-Cut problem.
- **Approach**: Implement the Goemans-Williamson algorithm using convex optimization and analyze the performance with respect to brute-force and theoretical bounds.
- **Impact**: Developed a strong understanding of the trade-offs between exact and relaxed solutions, improved algorithmic efficiency by optimizing bottlenecks, and enhanced implementation skills with numerical solvers.

---

## 🧩 Algorithm Highlights

- Integer programming formulation of Max-Cut
- SDP relaxation using CVXPY and custom solver integration
- Cholesky/eigen decomposition for extracting vector embeddings
- Randomized hyperplane rounding technique
- Approximation ratio analysis (~0.878)

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Libraries**: `cvxpy`, `numpy`, `scipy`, `matplotlib`
- **Solvers**: SCS / MOSEK / CVXOPT (configurable)
- **Optional**: `networkx` for graph visualization

---

## 📈 Performance Analysis

- Comparison of GW algorithm vs brute-force on small graphs
- Approximation ratio observed empirically
- Time complexity vs input size (discussion in `report.pdf`)

---

## 📄 Files Included

| File | Description |
|------|-------------|
| `gw.py` | Driver code to run Max-Cut solver |
| `gw.py` | Goemans-Williamson implementation |
| `gw.py` | Naive Max-Cut for comparison |
| `gw.py` | Helper functions for graphs and plotting |
| `Report.pdf` | Final research report |
| `Final Presentation.pdf` | Presentation slides for the project |

---

## 📚 References

1. Goemans, M.X. and Williamson, D.P., 1995. Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems Using Semidefinite Programming. *Journal of the ACM*, 42(6), pp.1115–1145.
2. Khot, S., Kindler, G., Mossel, E., and O'Donnell, R., 2007. Optimality of semidefinite relaxations for Max-Cut and other 2-CSPs. *SIAM Journal on Computing*, 37(1), pp.319–357.

---

## 🙏 Acknowledgments

This project was conducted under the guidance of **Professor Sutanu Gayen**, Department of Computer Science and Engineering, IIT Kanpur. I am grateful for his support and valuable feedback throughout the research.
I am also greatful to my Phd guide Mr. Debjyoti Dey for his consistent effors and support with me regular meetings discussion of reading material.
---

## 📬 Contact

**Areen Mahich**  
UG Student, CSE @ IIT Kanpur  
Email: *areenm23@iitk.ac.in* 