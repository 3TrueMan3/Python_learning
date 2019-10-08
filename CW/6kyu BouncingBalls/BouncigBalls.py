def bouncingBall(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        count = 1
        while h * bounce > window:
            count += 2
            h = h * bounce
        return count
    return -1


print(bouncingBall(30, 0.66, 1.5))
