#include <boost/context/continuation.hpp>
#include <boost/context/continuation_fcontext.hpp>
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
    bool started = false;
    // 这个task对应的fiber
    ctx::continuation cc;
    // 从什么fiber切换过来的
    // 调用resume后返回suspend对象
    ctx::continuation cont;

    std::string to_string() {
        std::stringstream ss;
        ss << "Task(id=" << id << ", cc=" << cc << ")";
        return ss.str();
    }
};

struct Scheduler {
    std::vector<Task*> tasks;
    int active = 0;
    int index = 0;

    void add(TaskFn&& fn) {
        Task* t = new Task();
        t->fn = std::move(fn);
        tasks.push_back(t);
        active++;
    }

    void run() {
        ctx::continuation cc = ctx::callcc([&](ctx::continuation&& cont) {
            while (active) {
                Task* task = tasks[index];
                // 这个task运行结束
                if (task->started && !task->cc) {
                    continue;
                }
                printf("---> S: select w%d: %s run\n", index, task->to_string().c_str());
                if (!task->started) {
                    task->started = true;
                    task->cc = ctx::callcc([task, this](ctx::continuation&& cont) {
                        task->cont = std::move(cont);
                        task->fn(task);
                        this->active--;
                        return task->cont.resume();
                    });
                } else {
                    task->cc = task->cc.resume();
                }
                printf("<--- S: select w%d: %s \n", index, task->to_string().c_str());
                index = (index + 1) % tasks.size();
            }
            printf("S: ready to exit\n");
            return cont.resume();
        });
    }
};

static void foo(Task* t) {
    for (int i = 0; i < 2; i++) {
        printf("W: w%d run foo with %d\n", t->id, i);
        t->cont = t->cont.resume();
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
                t->cont = t->cont.resume();
            }
        });
    }
    scheduler.run();
}