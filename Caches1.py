from m5.objects import *
class L1Cache(Cache):
    size = '64kB'
    tag_latency = 50
    data_latency = 50
    assoc = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 2
class L1_ICache(L1Cache):
    size = '32kB'
    is_read_only = True
    writeback_clean = True
class L1_DCache(L1Cache):
    size = '64kB'
    def cache_config(self, options, system):
        system.cache_line_size  =options.cache_line_size
class L2Cache(Cache):
    tag_latency = 2
    assoc = 16
    data_latency = 2
    size = '1024kB'
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 1
    write_buffers = 8
