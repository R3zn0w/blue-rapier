def argumenty(arg_list, mode):
    def decorator(rawFunction):
        def decorated(*args):
            if mode == 'suma':
                arg_count = 4
            elif mode == 'roznica':
                arg_count = 3
            args_final = []
            if len(args) < arg_count:
                for arg in args:
                    args_final.append(arg)
                for i in range(arg_count - len(args)):
                    if i >= len(arg_list):
                        break
                    args_final.append(arg_list[i])
            else:
                args_final = args
            rawFunction(*args_final)
            try:
                return arg_list[arg_count - len(args)]
            except:
                return None
        return decorated
    return decorator


class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def __setitem__(self, name, value):
        if name == "suma":
            self.argumentySuma = value

        if name == "roznica":
            self.argumentyRoznica = value

    @argumenty(argumentySuma, 'suma')
    def suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    @argumenty(argumentyRoznica, 'roznica')
    def roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')
