"""Profiling example using cProfile and pstats"""
def work(n):
    s = 0
    for i in range(n):
        s += i*i
    return s

if __name__ == '__main__':
    import cProfile, pstats, io
    pr = cProfile.Profile()
    pr.enable()
    work(200000)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats(10)
    print(s.getvalue())
