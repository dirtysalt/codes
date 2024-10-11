#include <boost/context/fiber.hpp>
#include <cstdio>
#include <sstream>
#include <utility>
#include <vector>
namespace ctx = boost::context;

struct Task;
using TaskFn = std::function<void(Task*)>;

struct Task {
    int id;
    // 这个task对应的function
    TaskFn fn;
    // 这个task对应的fiber
    ctx::fiber fiber;
    // 从什么fiber切换过来的
    // 调用resume后返回suspend对象
    ctx::fiber cont;

    std::string to_string() {
        std::stringstream ss;
        ss << "Task(id=" << id << ", fiber=" << fiber << ")";
        return ss.str();
    }
};

struct Scheduler {
    std::vector<Task*> tasks;
    int active = 0;
    int index = 0;
    ctx::fiber schedule;

    void add(TaskFn&& fn) {
        Task* t = new Task();
        t->fn = std::move(fn);
        t->fiber = ctx::fiber{[t, this](ctx::fiber&& cont) {
            t->cont = std::move(cont);
            t->fn(t);
            this->active--;
            return std::move(t->cont).resume();
        }};
        tasks.push_back(t);
        active++;
    }

    Scheduler() {
        schedule = ctx::fiber([&](ctx::fiber&& cont) {
            while (active) {
                Task* task = tasks[index];
                // 这个task运行结束
                if (!task->fiber) {
                    continue;
                }
                printf("---> S: select w%d: %s run\n", index, task->to_string().c_str());
                task->fiber = std::move(task->fiber).resume();
                printf("<--- S: select w%d: %s \n", index, task->to_string().c_str());
                index = (index + 1) % tasks.size();
            }
            printf("S: ready to exit\n");
            return std::move(cont).resume();
        });
    }

    void run() { std::move(schedule).resume(); }
};

static void foo(Task* t) {
    for (int i = 0; i < 2; i++) {
        printf("W: w%d run foo with %d\n", t->id, i);
        t->cont = std::move(t->cont).resume();
    }
}
int main() {
    Scheduler scheduler;
    const int n = 2;
    for (int i = 0; i < n; i++) {
        scheduler.add([i](Task* t) {
            t->id = i;
            for (int j = 0; j < 2; j++) {
                printf("W: w%d is running\n", t->id);
                foo(t);
                t->cont = std::move(t->cont).resume();
            }
        });
    }
    scheduler.run();
}