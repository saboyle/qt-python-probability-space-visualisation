from scipy.stats import norm


def brownian(delta=0.25, dt=0.1, x=2.0):
    while True:
        x = x + norm.rvs(scale=delta**2*dt)
        yield x


if __name__ == "__main__":
    for i in range(10):
        print(next(brownian()))
