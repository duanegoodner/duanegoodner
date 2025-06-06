
## About Me

I'm a systems-oriented engineer with a deep curiosity about how abstraction layers interact — from low-level physics to high-level software, and everything in between. My background spans atomic-scale materials science, semiconductor process development, and performance-focused software engineering.

After over a decade at Micron Technlogy developing novel materials and scalable fabrication processes that helped enable multiple generations of high-performance DRAM and NAND Flash memory, I shifted focus to software.

Now I work near the software-hardware boundary — building tools and infrastructure that emphasize modularity, performance, and architectural clarity. I thrive in environments where performance bottlenecks aren’t just bugs to fix, but signposts to deeper design opportunities. I'm especially interested in how these principles apply to emerging hardware and next-generation AI systems.


## Featured Projects
[**parallel-prefix-engine**](https://github.com/duanegoodner/parallel-prefix-engine)  
High-performance 2D prefix sum engine with CUDA and MPI backends. CUDA kernels are optimized to maximize shared memory usage and reduce global memory traffic, enabling tile-based parallelism and high-throughput execution at large input scales. Containerized for easy deployment; plugin-style architecture supports drop-in backend extensions.  
![C++](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/cpp-dot.svg) C++&nbsp;&nbsp;&nbsp;&nbsp;![CUDA](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/cuda-dot.svg) CUDA&nbsp;&nbsp;&nbsp;&nbsp;![MPI](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/mpi-dot.svg) MPI

[**docktuna**](https://github.com/duanegoodner/docktuna)  
Fully containerized template for running the Optuna hyperparameter tuning framework with PostgreSQL RDB storage — powered by Docker, Conda, and Poetry. Built for reproducibility, GPU support, and secure, scalable experiment tracking. Includes full test coverage and API documentation.  
![Python](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/python-dot.svg) Python&nbsp;&nbsp;&nbsp;&nbsp;![Docker](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/docker-dot.svg) Docker

[**polymorphism-compare**](https://github.com/duanegoodner/polymorphism-compare)  
Benchmarking suite comparing runtime polymorphism (virtual functions) with compile-time alternatives (CRTP, C++ Concepts) across multiple compute functions and optimization levels. Shows faster execution and lower memory access for compile-time options at max optimization, and reveals a significant CRTP advantage over C++ Concepts at the mid-range optimization commonly used in production.environments.  
![C++](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/cpp-dot.svg) C++

[**hpc-collection**](https://github.com/duanegoodner/hpc-collection)  
A set of high-performance computing (HPC) projects demonstrating memory-bound and compute-intensive workload optimization across distributed systems. Includes tiled matrix operations, Gauss-Seidel synchronization, MPI-based gas simulation, and a hybrid MPI/OpenMP histogram sort. Highlights cache locality tuning, inter-process communication strategies and scaling analysis on a production HPC cluster.  
![C++](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/cpp-dot.svg) C++&nbsp;&nbsp;&nbsp;&nbsp;![MPI](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/mpi-dot.svg) MPI&nbsp;&nbsp;&nbsp;&nbsp;![OpenMP](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/openmp-dot.svg) OpenMP&nbsp;&nbsp;&nbsp;&nbsp;![SLURM](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/slurm-dot.svg) SLURM

[**icu-deep-learning**](https://github.com/duanegoodner/icu-deep-learning)  
AI model that uses intensive care unit (ICU) lab and vital sign data to predict patient outcomes. Exhibits 90% faster data pipeline and 60% better predictive performance compared to prior studies of the same dataset. Includes a custom PyTorch module for adversarial attacks, enabling batch-mode evaluation of model vulnerabilities.  
![PyTorch](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/pytorch-dot.svg) PyTorch&nbsp;&nbsp;&nbsp;&nbsp;![SQL](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/sql-dot.svg) SQL&nbsp;&nbsp;&nbsp;&nbsp;![Docker](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/docker-dot.svg) Docker

[**xiangqigame**](https://github.com/duanegoodner/xiangqigame)  
AI engine for Xiangqi (Chinese Chess) with a C++ core, and a Python wrapper supporting a command-line interface and data analysis suite. Implements a plugin-style architecture with compile-time polymorphism for performance-critical components, achieving a 10x speedup over runtime polymorphism.  
![C++](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/cpp-dot.svg) C++&nbsp;&nbsp;&nbsp;&nbsp;![Python](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/python-dot.svg) Python

[**srepkg**](https://github.com/duanegoodner/srepkg)  
Wraps CLI-enabled Python packages with custom build system files, ensuring installation in isolated virtual environments and allowing package distributors to safeguard against downstream dependency conflicts. Includes an automated test suite with 99% code coverage to safeguard reliability. Available on [PyPI](https://pypi.org/project/srepkg/).    
![Python](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/python-dot.svg) Python

[**resticlvm**](https://github.com/duanegoodner/resticlvm)  
Configuration-driven CLI tool for atomic, incremental Linux backups using LVM snapshots and Restic. Follows a “Bash executes, Python orchestrates” model. Installable via pip and uses only the Python standard library — no external dependencies.  
![Shell](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/shell-dot.svg)Shell&nbsp;&nbsp;&nbsp;&nbsp;![Python](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/python-dot.svg) Python

[**systems-workshop**](https://github.com/duanegoodner/systems-workshop)  
A set of tools and demos exploring systems programming and infrastructure. Topics include process and signal management, low-level I/O, access control, environment conversion, and snapshot-based backup automation. Projects are organized as Git submodules for modular exploration and reuse.  
![C](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/c-dot.svg) C&nbsp;&nbsp;&nbsp;&nbsp;![Shell](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/shell-dot.svg) Shell&nbsp;&nbsp;&nbsp;&nbsp;![Python](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/python-dot.svg) Python&nbsp;&nbsp;&nbsp;&nbsp;![Assembly](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/assembly-dot.svg) Assembly

<!-- [**smallsh**](https://github.com/duanegoodner/smallsh)  
A minimalist Bash-like shell written in C, with built-in commands (`cd`, `exit`, `status`) and full support for executing other programs as subprocesses. Features include I/O redirection, background job control, custom signal handling and a foreground-only mode triggered by `SIGTSTP`.  
![C](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/c-dot.svg) C 

[**lowlevel-io-meancalc**](https://github.com/duanegoodner/lowlevel_io_meancalc)  
Low level IO and simple arithmetic in Assembly Language.  
![Assembly](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/assembly-dot.svg) Assembly

[**pygetfacl**](https://github.com/duanegoodner/pygetfacl)  
A Python wrapper for the Linux getfacl command that converts Access Control List (ACL) information into programmer-friendly Python objects.  
![Python](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/python-dot.svg) Python -->


<!-- [**ml-modeling-suite-r**](https://github.com/duanegoodner/ml-modeling-suite-r)  
A collection of machine learning projects implemented in R, covering a diverse set of modeling approaches and datasets. Emphasis on reproducible workflows, cross-validation, and a mix of from-scratch algorithm implementation and applied use of existing tools and libraries.  
![R](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/r-dot.svg) R -->

<!-- [**pet-matcher**](https://github.com/duanegoodner/pet-matcher)  
A cross-platform (iOS & Android) mobile app to match animal-loving people with animals in need of homes.  
![Dart](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/dart-dot.svg) Dart&nbsp;&nbsp;&nbsp;&nbsp;![Flutter](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/fluorescentblue-dot.svg) Flutter&nbsp;&nbsp;&nbsp;&nbsp;![Firestore](https://github.com/duanegoodner/duanegoodner/raw/main/assets/svg/firestore-dot.svg) Google Firestore -->


