from __future__ import print_function, division

# All supported detrending methods.
# If user requests other method, an error is raised.
methods = [
    "biweight",
    "lowess",
    "andrewsinewave",
    "welsch",
    "hodges",
    "median",
    "mean",
    "trim_mean",
    "hspline",
    "cofiam",
    "supersmoother",
    "savgol",
    "medfilt",
    "gp",
    "untrendy",
    "huber",
    "winsorize",
]

# astrophysical constants
G = 6.67408e-11  # gravitational constant [m^3 / kg / s^2]
R_sun = 695508000  # radius of the Sun [m]
R_earth = 6371000  # radius of the Earth [m]
R_jup = 69911000  # radius of Jupiter [m]
M_sun = 1.989 * 10 ** 30  # mass of the Sun [kg]
SECONDS_PER_DAY = 86400

# Desired precision of the final location estimate of the `biweight`, `welsch`,
# and `andrewsinewave`. All other methods use one-step estimates. The iterative
# algorithm based on Newton-Raphson stops when the change in location becomes
# smaller than ``FTOL``. Default: `1e-6`, or 1ppm. Higher precision comes at
# greater computational expense.
FTOL = 1e-6

# Iterative Huber estimator sometimes fails to converge. Its default is 30 in:
# https://www.statsmodels.org/dev/_modules/statsmodels/robust/scale.html#Huber
# This is often not sufficient --> set MAXITER=1000 to avoid infinite loop
MAXITER = 1000

# Maximum number of sines to be fit for COFIAM
COFIAM_MAX_SINES = 100

# Lomb-Scargle periodogram frequency search grid size
LS_FREQS = 10000


# SuperSmoother span constants
# Similar to 
# https://github.com/jakevdp/supersmoother/blob/master/supersmoother/supersmoother.py
primary_span_lower = 1
primary_span_upper = 3
middle_span = 3
upper_span = 2