import m5
from m5.objects import *
from Caches import *
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]
system.cpu = TimingSimpleCPU()
system.cpu.icache = L1Cache()
system.cpu.dcache = L1Cache()
system.cpu.icache.cpu_side = system.cpu.icache_port
system.cpu.dcache.cpu_side = system.cpu.dcache_port
system.l2bus = L2XBar()
system.cpu.icache.mem_side = system.l2bus.slave
system.cpu.dcache.mem_side = system.l2bus.slave
system.l2cache = L2Cache()
system.l2cache.cpu_side = system.l2bus.master
system.membus = SystemXBar()
system.l2cache.mem_side = system.membus.slave
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master
system.system_port = system.membus.slave
system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master
system.cache_line_size = '64'
process = Process()
process.cmd = ['tests/test-progs/hello/bin/x86/linux/sha']
system.cpu.workload = process
system.cpu.createThreads()
root = Root(full_system = False, system = system)
m5.instantiate()
print ("Beginning simulation!")
exit_event = m5.simulate()
print ('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))
