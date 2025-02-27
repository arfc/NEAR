read -p "Are you sure you want to run this script, it will create 28 output files and take several minutes? Press Enter to continue or any other key to exit." -n 1 -r
echo
if [[ ! $REPLY =~ ^$ ]]; then
    echo "Exiting script."
    exit 1
fi

mkdir cycamore_reactor

perf record -g valgrind --tool=callgrind cyclus -i cycamore_reactor.xml -o cycamore_reactor_call_perf_out.sqlite \\

gprof2dot -s -f callgrind callgrind.out.2428639 -o cycamore_reactor_output_s.dot \\

dot -Tpng cycamore_reactor_output_s.dot -o cycamore_reactor_output_s.png \\

callgrind_annotate callgrind.out.120466 >> cycamore_reactor_callgrind_annotate.txt \\


perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out1.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out2.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out3.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out4.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out5.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out6.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out7.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out8.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\

perf stat -o cycamore_reactor/cycamore_reactor_perf_stat_out9.txt cyclus -i cycamore_reactor.xml -o cycamore_reactor/cycamore_reactor_perf_stat.sqlite \\



mkdir tod_reactor

perf record -g valgrind --tool=callgrind cyclus -i tod_reactor.xml -o tod_reactor_call_perf_out.sqlite \\

gprof2dot -s -f callgrind callgrind.out.2428639 -o tod_reactor_output_s.dot \\

dot -Tpng tod_reactor_output_s.dot -o tod_reactor_output_s.png \\

callgrind_annotate callgrind.out.120466 >> tod_reactor_callgrind_annotate.txt \\


perf stat -o tod_reactor/tod_reactor_perf_stat_out.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out1.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out2.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out3.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out4.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out5.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out6.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out7.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out8.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

perf stat -o tod_reactor/tod_reactor_perf_stat_out9.txt cyclus -i tod_reactor.xml -o tod_reactor_perf_stat.sqlite >> tod_reactor_perf_stat_out.txt \\

