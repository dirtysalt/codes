#include <boost/context/fiber.hpp>
#include <cstdio>
#include <utility>
#include <vector>
namespace ctx = boost::context;

struct Task {
    std::function<void()> fn;
    ctx::fiber fiber;
};

struct Scheduler {
    std::vector<Task*> tasks;
    int active = 0;
    int index = 0;
    ctx::fiber schedule;

    void add(std::function<void()>&& fn) {
        Task* t = new Task();
        t->fn = std::move(fn);
        t->fiber = ctx::fiber{[t, this](ctx::fiber&& cont) {
            for (int i = 0; i < 3; i++) {
                t->fn();
                // this->schedule = std::move(this->schedule).resume();
                cont = std::move(cont).resume();
            }
            this->active--;
            return std::move(cont).resume();
        }};
        tasks.push_back(t);
        active++;
    }

    Scheduler() {
        schedule = ctx::fiber([&](ctx::fiber&& cont) {
            while (active) {
                Task* task = tasks[index];
                if (!task->fiber) {
                    continue;
                }
                printf("S: select w%d to run\n", index);
                index = (index + 1) % tasks.size();
                task->fiber = std::move(task->fiber).resume();
            }
            printf("S: ready to exit\n");
            return std::move(cont).resume();
        });
    }

    void run() { std::move(schedule).resume(); }
};
int main() {
    Scheduler scheduler;
    const int n = 2;
    for (int i = 0; i < n; i++) {
        scheduler.add([i]() { printf("W: w%d running\n", i); });
    }
    scheduler.run();
}