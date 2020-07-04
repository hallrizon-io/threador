from threador.contrib import Executor

if __name__ == '__main__':
    parallel = Executor(tasks=(
        ['sleep', None, {'sleep': 3}],
        ['sleep', None, {'sleep': 2}],
        ['sleep', None, {'sleep': 4}],
    ))

    for i in parallel.run():
        print(i)
