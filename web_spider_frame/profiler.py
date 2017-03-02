# import cProfile
# import hotshot
# import line_profiler
#
# # final = hotshot.Profile('/Users/zhengyichen/Documents/Python/web_spider_frame/spider_frame_1.5_FINAL.py')
# # final.start()
# h = hotshot.stats.load('/Users/zhengyichen/Documents/Python/web_spider_frame/spider_frame_1.5_FINAL.py')
# h.print_stats
#
# import line_profiler
# line_profiler.az

# @profile
def f():
    l = ['foo, foobar, char'] * 100000
    m = [x for x in l if x[:3] == 'foo']
f()

# %prun f()
