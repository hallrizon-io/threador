from threador.contrib import Executor

if __name__ == '__main__':
    parallel = Executor(tasks=(
        ['sleep', None, {'timeout': 3}],
        ['sleep', None, {'timeout': 2}],
        ['sleep', None, {'timeout': 4}],
    ))

    result = parallel.run()
    print(result)
